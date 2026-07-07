from flask import Flask, Response, send_file, request
from flask_cors import CORS
import cv2

from cameras.manager import CameraManager
from cameras.stream import generate
from vision.board_detector import BoardDetector
from game.game import Game

app = Flask(__name__)
CORS(app)

camera_manager = CameraManager()
camera_manager.scan_cameras()

board_detector = BoardDetector()
game = Game()


@app.route("/")
def index():
    return {
        "name": "DartVision Backend",
        "status": "running"
    }


# -----------------------------
# Kameras
# -----------------------------

@app.route("/api/cameras")
def cameras():
    return camera_manager.get_camera_information()


@app.route("/api/camera/<int:camera_id>/stream")
def stream(camera_id):

    camera = camera_manager.get_camera(camera_id)

    if camera is None:
        return {"error": "Camera not found"}, 404

    return Response(
        generate(camera),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/api/camera/<int:camera_id>/snapshot")
def snapshot(camera_id):

    camera = camera_manager.get_camera(camera_id)

    if camera is None:
        return {"error": "Camera not found"}, 404

    frame = camera.get_frame()

    if frame is None:
        return {"error": "No frame available"}, 500

    processed = board_detector.process(frame)

    cv2.imwrite("snapshot.jpg", processed)

    return send_file(
        "snapshot.jpg",
        mimetype="image/jpeg"
    )


# -----------------------------
# Spiel
# -----------------------------

@app.route("/api/game/new", methods=["POST"])
def new_game():

    data = request.get_json()

    players = data.get("players", [])

    game.players.clear()
    game.current_player = 0

    for player in players:
        game.add_player(player)

    return game.game_state()


@app.route("/api/game/throw", methods=["POST"])
def throw():

    data = request.get_json()

    points = int(data["points"])

    game.throw(points)

    return game.game_state()


@app.route("/api/game/next", methods=["POST"])
def next_player():

    game.next_player()

    return game.game_state()


@app.route("/api/game/state")
def state():

    return game.game_state()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)