import math

# -----------------------------
# Offizielle Reihenfolge der Felder
# (beginnend bei der 20, im Uhrzeigersinn)
# -----------------------------

SEGMENTS = [
    20, 1, 18, 4, 13,
    6, 10, 15, 2, 17,
    3, 19, 7, 16, 8,
    11, 14, 9, 12, 5
]

# -----------------------------
# Offizielle Maße eines Dartboards
# (Millimeter)
# -----------------------------

INNER_BULL = 6.35
OUTER_BULL = 15.9

TRIPLE_INNER = 99
TRIPLE_OUTER = 107

DOUBLE_INNER = 162
DOUBLE_OUTER = 170


class Geometry:

    def __init__(self, center=(500, 500), radius_px=450):

        self.cx = center[0]
        self.cy = center[1]

        # äußerer Doppelring = 170 mm
        self.scale = radius_px / DOUBLE_OUTER

    def pixel_to_mm(self, x, y):

        dx = x - self.cx
        dy = self.cy - y      # Y-Achse umdrehen

        return (
            dx / self.scale,
            dy / self.scale
        )

    def get_radius(self, x, y):

        x, y = self.pixel_to_mm(x, y)

        return math.sqrt(x * x + y * y)

    def get_angle(self, x, y):

        x, y = self.pixel_to_mm(x, y)

        angle = math.degrees(math.atan2(y, x))

        # 0° liegt rechts
        angle = (90 - angle) % 360

        return angle

    def get_multiplier(self, radius):

        if radius <= INNER_BULL:
            return "DBULL"

        if radius <= OUTER_BULL:
            return "SBULL"

        if TRIPLE_INNER <= radius <= TRIPLE_OUTER:
            return "T"

        if DOUBLE_INNER <= radius <= DOUBLE_OUTER:
            return "D"

        if radius > DOUBLE_OUTER:
            return "MISS"

        return "S"

    def get_segment(self, angle):

        index = int((angle + 9) // 18) % 20

        return SEGMENTS[index]

    def get_hit(self, x, y):

        radius = self.get_radius(x, y)

        multiplier = self.get_multiplier(radius)

        if multiplier == "MISS":
            return {
                "field": "MISS",
                "score": 0
            }

        if multiplier == "DBULL":
            return {
                "field": "DBULL",
                "score": 50
            }

        if multiplier == "SBULL":
            return {
                "field": "SBULL",
                "score": 25
            }

        segment = self.get_segment(
            self.get_angle(x, y)
        )

        factor = {
            "S": 1,
            "D": 2,
            "T": 3
        }[multiplier]

        return {
            "field": f"{multiplier}{segment}",
            "score": segment * factor
        }