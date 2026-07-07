from vision.preprocessor import ImagePreprocessor
from vision.circle_detector import CircleDetector
from vision.overlay import Overlay


class BoardDetector:

    def __init__(self):
        print("BoardDetector gestartet")

    def process(self, frame):

        gray = ImagePreprocessor.preprocess(frame)

        circles = CircleDetector.detect(gray)

        output = Overlay.draw(frame, circles)

        return output