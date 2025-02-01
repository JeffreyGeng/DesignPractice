import enum

class Cell(enum.Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2


class Grid:
    def __init__(self, rows, cols, connectN):
        self.rows = rows
        self.cols = cols
        self.connectN = connectN
        self.grid = [[Cell.EMPTY for _ in range(cols)] for _ in range(rows)]

    def GetGrid(self):
        return self.grid

    def insertCol(self, col, cell):
        if col < 0 or col > self.cols:
            raise ValueError("Col is out of bounds")
        if cell == Cell.EMPTY:
            raise ValueError("Game cell cannot be Empty")
        for row in range(self.rows-1,-1,-1):
            if self.grid[row][col] == Cell.EMPTY:
                self.grid[row][col] = cell
                return row
    
    def CheckWin(self, row, col, cell):
        curCount = 0
        # Check Horizontal
        for r in range(self.rows):
            if self.grid[r][col] == cell:
                curCount += 1
            else:
                curCount = 0
            if curCount == self.connectN:
                return True
            
        # Check Vertical
        curCount = 0
        for c in range(self.cols):
            if self.grid[row][c] == cell:
                curCount += 1
            else:
                curCount = 0
            if curCount == self.connectN:
                return True
            
        # Check Diagonal
        curCount = 0
        df

        # Check Other Diagonal
    