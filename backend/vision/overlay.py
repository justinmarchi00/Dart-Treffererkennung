import cv2


class Overlay:

    @staticmethod
    def draw(frame, circles):

        output = frame.copy()

        if circles is None:
            return output

        for circle in circles:

            x, y, r = circle

            cv2.circle(
                output,
                (x, y),
                r,
                (0, 255, 0),
                3
            )

            cv2.circle(
                output,
                (x, y),
                4,
                (0, 0, 255),
                -1
            )

        return output