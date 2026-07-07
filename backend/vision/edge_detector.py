import cv2


class EdgeDetector:

    @staticmethod
    def detect(image):
        return cv2.Canny(
            image,
            80,
            160
        )