import cv2


class Camera:

    def __init__(self, index=0):

        self.cap = cv2.VideoCapture(index)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def read(self):

        ok, frame = self.cap.read()

        if not ok:
            return None

        return frame

    def release(self):

        self.cap.release()