import cv2
import threading
import time


class Camera:
    def __init__(self, camera_id):
        self.camera_id = camera_id

        self.capture = None
        self.frame = None

        self.running = False
        self.thread = None

        self.width = 0
        self.height = 0
        self.fps = 0

    def start(self):
        self.capture = cv2.VideoCapture(self.camera_id, cv2.CAP_AVFOUNDATION)

        if not self.capture.isOpened():
            return False

        self.width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)

        self.running = True

        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

        return True

    def update(self):
        while self.running:
            success, frame = self.capture.read()

            if success:
                self.frame = frame
            else:
                time.sleep(0.01)

    def get_frame(self):
        return self.frame

    def stop(self):
        self.running = False

        if self.thread:
            self.thread.join()

        if self.capture:
            self.capture.release()