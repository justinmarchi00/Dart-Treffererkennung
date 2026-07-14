import cv2
import numpy as np


class DartDetector:

    def __init__(self):
        self.reference = None
        self.min_area = 150

    def set_reference(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.reference = cv2.GaussianBlur(gray, (5, 5), 0)

    def detect(self, frame):

        if self.reference is None:
            return None, frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        diff = cv2.absdiff(self.reference, gray)

        _, mask = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)

        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.dilate(mask, kernel, iterations=2)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_NONE
        )

        debug = frame.copy()

        if not contours:
            return None, debug

        contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(contour) < self.min_area:
            return None, debug

        cv2.drawContours(debug, [contour], -1, (0, 255, 0), 2)

        # PCA
        data = contour.reshape(-1, 2).astype(np.float32)

        mean, eigenvectors = cv2.PCACompute(data, mean=None)

        center = mean[0]

        direction = eigenvectors[0]

        projections = np.dot(data - center, direction)

        p1 = data[np.argmin(projections)]
        p2 = data[np.argmax(projections)]

        board_center = np.array([500, 500], dtype=np.float32)

        if np.linalg.norm(p1 - board_center) < np.linalg.norm(p2 - board_center):
            tip = p1
        else:
            tip = p2

        tip = tuple(np.int32(tip))

        cv2.circle(debug, tip, 6, (0, 0, 255), -1)

        cv2.line(
            debug,
            tuple(np.int32(p1)),
            tuple(np.int32(p2)),
            (255, 0, 0),
            2
        )

        return tip, debug