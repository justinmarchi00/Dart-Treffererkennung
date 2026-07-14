import cv2
import json
import numpy as np

# Kalibrierung laden
with open("calibration/board_calibration.json", "r") as f:
    data = json.load(f)

H = np.array(data["homography"], dtype=np.float32)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    warped = cv2.warpPerspective(
        frame,
        H,
        (1000, 1000)
    )

    cv2.imshow("Original", frame)
    cv2.imshow("Warped Board", warped)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()