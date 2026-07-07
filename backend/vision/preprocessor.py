import cv2


class ImagePreprocessor:

    @staticmethod
    def to_gray(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def blur(gray):
        return cv2.GaussianBlur(gray, (5, 5), 0)

    @staticmethod
    def preprocess(frame):
        gray = ImagePreprocessor.to_gray(frame)
        blur = ImagePreprocessor.blur(gray)
        return blur