import cv2

from vision.background import BackgroundDetector

cam = cv2.VideoCapture(0)

detector = BackgroundDetector()

print("R = Referenz")
print("ESC = Ende")

while True:

    ret, frame = cam.read()

    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        detector.set_reference(frame)
        print("Referenz gespeichert")

    mask, contours = detector.detect(frame)

    debug = frame.copy()

    if contours is not None:

        for contour in contours:

            if cv2.contourArea(contour) < 200:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                debug,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    cv2.imshow("Debug", debug)

    if mask is not None:
        cv2.imshow("Mask", mask)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()