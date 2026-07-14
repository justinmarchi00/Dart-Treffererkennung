import cv2
import numpy as np


class MotionDetector:

    def detect(self,diff):

        _,mask = cv2.threshold(
            diff,
            18,
            255,
            cv2.THRESH_BINARY
        )

        kernel = np.ones((5,5),np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel
        )

        return mask