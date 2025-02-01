import Player
import Grid
class Game:
    def __init__(self, grid, n, winScore):
        self._grid = grid
        self._n = n
        self._winScore = winScore
        self._players = [
            Player("Player1", Grid.Cell.RED),
            Player("Player2", Grid.Cell.YELLOW),
        ]
        self._Score = {}
        for player in self._players:
            self._Score[player.getName()] = 0

    # plays a whole game
    def play(self):
        
        