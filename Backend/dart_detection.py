import cv2
import numpy as np
import json

# -------------------------
# KALIBRIERUNG LADEN
# -------------------------

with open("calibration.json", "r") as f:
    calibration = json.load(f)

# -------------------------
# KAMERA
# -------------------------

cam = cv2.VideoCapture(2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

before_frame = None

print("")
print("SPACE = Referenzbild aufnehmen")
print("D = Dart erkennen")
print("Q = Beenden")
print("")

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

    pts_dst = np.array([
        [0, 0],
        [800, 0],
        [800, 800],
        [0, 800]
    ], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(
        pts_src,
        pts_dst
    )

    warped = cv2.warpPerspective(
        frame,
        matrix,
        (800, 800)
    )

    warped = cv2.rotate(
        warped,
        cv2.ROTATE_180
    )

    display = warped.copy()

    cv2.putText(
        display,
        "SPACE = Referenz | D = Dart erkennen",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # -------------------------
    # DART SUCHEN
    # -------------------------

    if before_frame is not None:

        diff = cv2.absdiff(
            before_frame,
            warped
        )

        gray = cv2.cvtColor(
            diff,
            cv2.COLOR_BGR2GRAY
        )

        blur = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        _, thresh = cv2.threshold(
            blur,
            25,
            255,
            cv2.THRESH_BINARY
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area < 100:
                continue

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(
                display,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            dart_x = x + w // 2
            dart_y = y + h // 2

            cv2.circle(
                display,
                (dart_x, dart_y),
                6,
                (0, 0, 255),
                -1
            )

            cv2.putText(
                display,
                f"{dart_x},{dart_y}",
                (dart_x + 10, dart_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

    cv2.imshow(
        "Dart Detection",
        display
    )

    key = cv2.waitKey(1)

    # -------------------------
    # REFERENZ AUFNEHMEN
    # -------------------------

    if key == ord(" "):

        before_frame = warped.copy()

        print("Referenzbild gespeichert")

    # -------------------------
    # DART ERKENNEN
    # -------------------------

    if key == ord("d"):

        print("Dartsuche aktiviert")

    # -------------------------
    # ENDE
    # -------------------------

    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()