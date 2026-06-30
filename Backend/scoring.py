import cv2
import numpy as np
import json
import math

# ==================================
# EINSTELLUNGEN
# ==================================

BOARD_CENTER_X = 385
BOARD_CENTER_Y = 527

BULL_INNER = 10
BULL_OUTER = 22

TRIPLE_INNER = 150
TRIPLE_OUTER = 170

DOUBLE_INNER = 250
DOUBLE_OUTER = 275

# ==================================
# KALIBRIERUNG LADEN
# ==================================

with open("Backend/calibration.json", "r") as f:
    calibration = json.load(f)

# ==================================
# KAMERA
# ==================================

cam = cv2.VideoCapture(2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# ==================================
# SEGMENTE
# ==================================

segments = [
    20, 1, 18, 4, 13,
    6, 10, 15, 2, 17,
    3, 19, 7, 16, 8,
    11, 14, 9, 12, 5
]

last_score = "Klick auf die Scheibe"

# ==================================
# SCORE BERECHNUNG
# ==================================

def get_score(x, y):

    dx = x - BOARD_CENTER_X
    dy = BOARD_CENTER_Y - y

    radius = math.sqrt(dx * dx + dy * dy)

    angle = math.degrees(
        math.atan2(dy, dx)
    )

    angle = (90 - angle) % 360

    segment_index = int(
        (angle + 9) // 18
    ) % 20

    segment = segments[segment_index]

    # Bull

    if radius <= BULL_INNER:
        return "BULL", 50

    if radius <= BULL_OUTER:
        return "25", 25

    # Miss

    if radius > DOUBLE_OUTER:
        return "MISS", 0

    # Double

    if DOUBLE_INNER <= radius <= DOUBLE_OUTER:
        return f"D{segment}", segment * 2

    # Triple

    if TRIPLE_INNER <= radius <= TRIPLE_OUTER:
        return f"T{segment}", segment * 3

    # Single

    return str(segment), segment

# ==================================
# MAUSKLICK
# ==================================

def mouse_click(event, x, y, flags, param):

    global last_score

    if event == cv2.EVENT_LBUTTONDOWN:

        field, points = get_score(x, y)

        last_score = f"{field} ({points})"

        print(last_score)

# ==================================
# WINDOW
# ==================================

cv2.namedWindow("Scoring")
cv2.setMouseCallback(
    "Scoring",
    mouse_click
)

# ==================================
# LOOP
# ==================================

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

    # Kamera 3 richtig herum

    warped = cv2.rotate(
        warped,
        cv2.ROTATE_180
    )

    # Mittelpunkt

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        5,
        (0, 0, 255),
        -1
    )

    # Bull

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        BULL_INNER,
        (0, 255, 255),
        2
    )

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        BULL_OUTER,
        (0, 255, 255),
        2
    )

    # Triple

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        TRIPLE_INNER,
        (255, 0, 0),
        2
    )

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        TRIPLE_OUTER,
        (255, 0, 0),
        2
    )

    # Double

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        DOUBLE_INNER,
        (255, 255, 0),
        2
    )

    cv2.circle(
        warped,
        (BOARD_CENTER_X, BOARD_CENTER_Y),
        DOUBLE_OUTER,
        (255, 255, 0),
        2
    )

    cv2.putText(
        warped,
        last_score,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Scoring",
        warped
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()