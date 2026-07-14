import cv2

from vision.camera import Camera
from vision.homography import Homography
from vision.background import Background
from vision.motion_detector import MotionDetector

camera = Camera()

warp = Homography(
    "calibration/board_calibration.json"
)

background = Background()

motion = MotionDetector()

print("R = Referenz")
print("ESC = Ende")

while True:

    frame = camera.read()

    warped = warp.warp(frame)

    key = cv2.waitKey(1)

    if key == ord("r"):

        background.update(warped)

        print("Referenz gespeichert")

    diff = background.difference(warped)

    if diff is not None:

        mask = motion.detect(diff)

        cv2.imshow(
            "Mask",
            mask
        )

    cv2.imshow(
        "Board",
        warped
    )

    if key == 27:
        break

camera.release()

cv2.destroyAllWindows()