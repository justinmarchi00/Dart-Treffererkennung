import cv2


class Background:

    def __init__(self):

        self.reference = None

    def update(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (7,7),
            0
        )

        self.reference = gray

    def difference(self, frame):

        if self.reference is None:
            return None

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (7,7),
            0
        )

        return cv2.absdiff(
            self.reference,
            gray
        )