import cv2
import numpy as np


class CircleDetector:

    @staticmethod
    def detect(image):

        circles = cv2.HoughCircles(
            image,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=300,
            param1=120,
            param2=40,
            minRadius=150,
            maxRadius=700
        )

        if circles is None:
            return None

        circles = np.uint16(np.around(circles))

        return circles[0]