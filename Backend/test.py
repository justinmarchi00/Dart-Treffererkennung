from flask import Flask, jsonify, Response, request
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)

# =====================================
# KAMERAS
# =====================================

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cam3 = cv2.VideoCapture(2)

for cam in [cam1, cam2, cam3]:

    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    
print("Cam1:", cam1.isOpened())
print("Cam2:", cam2.isOpened())
print("Cam3:", cam3.isOpened())

# =====================================
# KALIBRIERUNG
# =====================================

calibration = {
    "center_x": None,
    "center_y": None,
    "radius": None
}

# =====================================
# MJPEG STREAM
# =====================================

def generate(camera):

    while True:

        success, frame = camera.read()

        if not success:
            continue

        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame_bytes +
            b'\r\n'
        )

# =====================================
# STATUS
# =====================================

@app.route('/status')
def status():

    return jsonify({
        "message": "Backend verbunden"
    })

# =====================================
# KAMERA STATUS
# =====================================

@app.route('/cameras')
def cameras():

    return jsonify({
        "cam1": cam1.isOpened(),
        "cam2": cam2.isOpened(),
        "cam3": cam3.isOpened()
    })

# =====================================
# LIVE STREAMS
# =====================================

@app.route('/camera/1')
def camera1():

    return Response(
        generate(cam1),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/camera/2')
def camera2():

    return Response(
        generate(cam2),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/camera/3')
def camera3():

    return Response(
        generate(cam3),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# =====================================
# KALIBRIERUNG SPEICHERN
# =====================================

@app.route('/calibrate', methods=['POST'])
def calibrate():

    global calibration

    data = request.json

    calibration["center_x"] = data.get("center_x")
    calibration["center_y"] = data.get("center_y")
    calibration["radius"] = data.get("radius")

    print("Kalibrierung gespeichert:")
    print(calibration)

    return jsonify({
        "success": True,
        "calibration": calibration
    })

# =====================================
# KALIBRIERUNG AUSLESEN
# =====================================

@app.route('/calibration')
def get_calibration():

    return jsonify(calibration)

# =====================================
# SPÄTERE DART ERKENNUNG
# =====================================

@app.route('/detect')
def detect():

    return jsonify({
        "status": "noch nicht implementiert"
    })

# =====================================
# START
# =====================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5050,
        threaded=True
    )