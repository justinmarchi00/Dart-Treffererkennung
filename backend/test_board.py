import cv2

from board_detector import BoardDetector


cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = BoardDetector()

while True:

    ret, frame = cam.read()

    if not ret:
        break

    result = detector.detect(frame)

    cv2.imshow("Board Detection", result)

    key = cv2.waitKey(1)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()