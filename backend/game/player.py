class Player:

    def __init__(self, name):

        self.name = name
        self.score = 501

        self.average = 0
        self.total_points = 0
        self.total_darts = 0

        self.history = []

    def throw(self, points):

        self.history.append(points)

        self.score -= points

        self.total_points += points
        self.total_darts += 1

        if self.total_darts > 0:
            self.average = (self.total_points / self.total_darts) * 3

    def undo(self):

        if not self.history:
            return

        last = self.history.pop()

        self.score += last
        self.total_points -= last
        self.total_darts -= 1

        if self.total_darts > 0:
            self.average = (self.total_points / self.total_darts) * 3
        else:
            self.average = 0