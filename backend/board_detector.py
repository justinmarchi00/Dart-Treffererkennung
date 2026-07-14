import cv2
import numpy as np


class BoardDetector:
    def __init__(self):
        self.center = None
        self.radius = None

    def detect(self, frame):
        """
        Erkennt das Dartboard und gibt Mittelpunkt und Radius zurück.
        """

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 2)

        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=300,
            param1=120,
            param2=40,
            minRadius=180,
            maxRadius=450
        )

        output = frame.copy()

        if circles is not None:

            circles = np.round(circles[0]).astype(int)

            # größten Kreis wählen
            circle = max(circles, key=lambda c: c[2])

            x, y, r = circle

            self.center = (x, y)
            self.radius = r

            # Kreis zeichnen
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)

            # Mittelpunkt
            cv2.circle(output, (x, y), 5, (0, 0, 255), -1)

            # Fadenkreuz
            cv2.line(output, (x - 20, y), (x + 20, y), (255, 0, 0), 2)
            cv2.line(output, (x, y - 20), (x, y + 20), (255, 0, 0), 2)

            cv2.putText(
                output,
                f"Center: {x},{y}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            cv2.putText(
                output,
                f"Radius: {r}px",
                (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        return output