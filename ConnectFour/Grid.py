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

    # Returns the grid
    def GetGrid(self):
        return self.grid

    # Returns the row the piece is inserted to
    def insertCol(self, col, cell):
        if col < 0 or col > self.cols:
            raise ValueError("Col is out of bounds")
        if cell == Cell.EMPTY:
            raise ValueError("Game cell cannot be Empty")
        for row in range(self.rows-1,-1,-1):
            if self.grid[row][col] == Cell.EMPTY:
                self.grid[row][col] = cell
                return row
    
    # Returns True if there is a win, False otherwise
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
        r,c = 0,0
        while r < self.rows and c < self.cols:
            if self.grid[r][c] == cell:
                curCount += 1
            else:
                curCount = 0
            if curCount == self.connectN:
                return True
            r += 1
            c += 1

        # Check Other Diagonal
        curCount = 0
        r,c = 0, self.cols-1
        while r < self.rows and c > 0:
            if self.grid[r][c] == cell:
                curCount += 1
            else:
                curCount = 0
            if curCount == self.connectN:
                return True
            r += 1
            c -= 1
        
        return False