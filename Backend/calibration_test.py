import cv2
import numpy as np
import json
import os

cam = cv2.VideoCapture(2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

clicked_points = []

CALIBRATION_FILE = "calibration.json"

# -----------------------------
# MAUSKLICK
# -----------------------------

def mouse_click(event, x, y, flags, param):

    global clicked_points

    if event == cv2.EVENT_LBUTTONDOWN:

        if len(clicked_points) < 4:

            clicked_points.append((x, y))

            print(
                f"Punkt {len(clicked_points)}: {x}, {y}"
            )

# -----------------------------
# KALIBRIERUNG SPEICHERN
# -----------------------------

def save_calibration():

    if len(clicked_points) != 4:
        print("Bitte zuerst 4 Punkte setzen!")
        return

    data = {
        "cam1": {
            "top_left": list(clicked_points[0]),
            "top_right": list(clicked_points[1]),
            "bottom_right": list(clicked_points[2]),
            "bottom_left": list(clicked_points[3])
        }
    }

    with open(CALIBRATION_FILE, "w") as f:
        json.dump(
            data,
            f,
            indent=4
        )

    print("Kalibrierung gespeichert!")

# -----------------------------
# KALIBRIERUNG LADEN
# -----------------------------

def load_calibration():

    global clicked_points

    if not os.path.exists(
        CALIBRATION_FILE
    ):
        return

    with open(
        CALIBRATION_FILE,
        "r"
    ) as f:

        data = json.load(f)

    if "cam1" not in data:
        return

    clicked_points = [

        tuple(data["cam1"]["top_left"]),
        tuple(data["cam1"]["top_right"]),
        tuple(data["cam1"]["bottom_right"]),
        tuple(data["cam1"]["bottom_left"])

    ]

    print("Kalibrierung geladen!")

# -----------------------------
# START
# -----------------------------

load_calibration()

cv2.namedWindow(
    "Kalibrierung"
)

cv2.setMouseCallback(
    "Kalibrierung",
    mouse_click
)

while True:

    ret, frame = cam.read()

    if not ret:
        continue

    display = frame.copy()

    # Punkte anzeigen

    for i, point in enumerate(clicked_points):

        cv2.circle(
            display,
            point,
            8,
            (0, 255, 0),
            -1
        )

        cv2.putText(
            display,
            str(i + 1),
            (
                point[0] + 10,
                point[1] - 10
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Perspektive

    if len(clicked_points) == 4:

        pts_src = np.array([
            clicked_points[0],
            clicked_points[1],
            clicked_points[2],
            clicked_points[3]
        ], dtype=np.float32)

        size = 800

        pts_dst = np.array([
            [0, 0],
            [size, 0],
            [size, size],
            [0, size]
        ], dtype=np.float32)

        matrix = cv2.getPerspectiveTransform(
            pts_src,
            pts_dst
        )

        warped = cv2.warpPerspective(
            frame,
            matrix,
            (size, size)
        )

        cv2.imshow(
            "Draufsicht",
            warped
        )

    cv2.imshow(
        "Kalibrierung",
        display
    )

    key = cv2.waitKey(1)

    # S = speichern

    if key == ord('s'):

        save_calibration()

    # R = reset

    if key == ord('r'):

        clicked_points = []

        print(
            "Punkte zurückgesetzt!"
        )

    # Q = beenden

    if key == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()