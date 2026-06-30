import cv2
import numpy as np
import json

# ==========================
# KALIBRIERUNG LADEN
# ==========================

with open("Backend/calibration.json", "r") as f:
    calibration = json.load(f)

# ==========================
# KAMERA
# ==========================

cam = cv2.VideoCapture(2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# ==========================
# HAUPTSCHLEIFE
# ==========================

while True:

    ret, frame = cam.read()

    if not ret:
        continue

    pts_src = np.array([
        calibration["cam1"]["top_left"],
        calibration["cam1"]["top_right"],
        calibration["cam1"]["bottom_right"],
        calibration["cam1"]["bottom_left"]
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

    center_x = 410
    center_y = 290

    # Mittelpunkt

    cv2.circle(
        warped,
        (center_x, center_y),
        6,
        (0, 0, 255),
        -1
    )

    # Bull

    cv2.circle(
        warped,
        (center_x, center_y),
        30,
        (0, 255, 255),
        2
    )

    # Triple Ring

    cv2.circle(
        warped,
        (center_x, center_y),
        190,
        (255, 0, 0),
        2
    )

    # Double Ring

    cv2.circle(
        warped,
        (center_x, center_y),
        300,
        (255, 255, 0),
        2
    )

    # Außenring

    cv2.circle(
        warped,
        (center_x, center_y),
        320,
        (0, 255, 0),
        2
    )

    cv2.putText(
        warped,
        "DartVision Calibration",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Draufsicht",
        warped
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()