import cv2
import json
import numpy as np

# -------- Einstellungen --------
CAMERA_INDEX = 0
OUTPUT_FILE = "board_calibration.json"
BOARD_SIZE = 1000

clicked_points = []

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Kamera konnte nicht geöffnet werden.")
    exit()


def mouse(event, x, y, flags, param):
    global clicked_points

    if event == cv2.EVENT_LBUTTONDOWN:

        if len(clicked_points) < 4:
            clicked_points.append((x, y))
            print(f"Punkt {len(clicked_points)}: {(x, y)}")


cv2.namedWindow("Kalibrierung")
cv2.setMouseCallback("Kalibrierung", mouse)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    display = frame.copy()

    # Punkte zeichnen
    for i, p in enumerate(clicked_points):

        cv2.circle(display, p, 8, (0, 255, 0), -1)

        cv2.putText(
            display,
            str(i + 1),
            (p[0] + 10, p[1]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

    cv2.putText(
        display,
        "Klicke: OBEN -> RECHTS -> UNTEN -> LINKS",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2,
    )

    cv2.imshow("Kalibrierung", display)

    key = cv2.waitKey(1)

    # ESC
    if key == 27:
        break

    # ENTER
    if key == 13 and len(clicked_points) == 4:

        destination = np.float32([
            [500, 0],
            [1000, 500],
            [500, 1000],
            [0, 500]
        ])

        source = np.float32(clicked_points)

        H, _ = cv2.findHomography(source, destination)

        warped = cv2.warpPerspective(frame, H, (BOARD_SIZE, BOARD_SIZE))

        cv2.imshow("Entzerrt", warped)

        with open(OUTPUT_FILE, "w") as f:

            json.dump(
                {
                    "points": clicked_points,
                    "homography": H.tolist()
                },
                f,
                indent=4,
            )

        print("Kalibrierung gespeichert.")

cap.release()
cv2.destroyAllWindows()