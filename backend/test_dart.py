import cv2

from vision.dart_detector import DartDetector

cam = cv2.VideoCapture(0)

detector = DartDetector()

while True:

    ret, frame = cam.read()

    if not ret:
        break

    key = cv2.waitKey(1)

    if key == ord("r"):
        detector.set_reference(frame)
        print("Referenz gespeichert")

    tip, debug = detector.detect(frame)

    if tip is not None:
        print(tip)

    cv2.imshow("Detector", debug)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()