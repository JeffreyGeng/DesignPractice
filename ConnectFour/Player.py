class Player:
    def __init__(self, username, pieceColor):
        self._username = username
        self._pieceColor = pieceColor

    def getName(self):
        return self._username
    
    def getPieceColor(self):
        return self._pieceColor