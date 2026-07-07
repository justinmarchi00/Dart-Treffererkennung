from game.player import Player


class Game:

    def __init__(self):

        self.players = []
        self.current_player = 0

    def add_player(self, name):

        self.players.append(Player(name))

    def get_current_player(self):

        return self.players[self.current_player]

    def next_player(self):

        self.current_player += 1

        if self.current_player >= len(self.players):
            self.current_player = 0

    def throw(self, points):

        player = self.get_current_player()

        player.throw(points)

        if player.score < 0:
            player.undo()

    def game_state(self):

        result = []

        for player in self.players:

            result.append({
                "name": player.name,
                "score": player.score,
                "average": round(player.average, 2),
                "history": player.history
            })

        return {
            "currentPlayer": self.current_player,
            "players": result
        }