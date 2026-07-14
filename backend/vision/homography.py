import cv2
import json
import numpy as np


class Homography:

    def __init__(self, filename):

        with open(filename) as f:

            data = json.load(f)

        self.H = np.array(
            data["homography"],
            dtype=np.float32
        )

    def warp(self, frame):

        return cv2.warpPerspective(
            frame,
            self.H,
            (1000,1000)
        )