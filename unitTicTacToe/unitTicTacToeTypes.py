from enum import Enum

# A PlayerType is one of  
#  - 'X' 
#  - 'O'
class PlayerType(Enum):
    X = 'X'
    O = 'O'

# A CellState is one of
# - 'X'
# - 'O'
# - ''
class CellState(Enum):
    X = 1
    O = 5
    EMPTY = 0

# A Result is one of
# - 'X'
# - 'O'
# - 'draw'
class Result(Enum):
    X = 'X'
    O = 'O'
    DRAW = 'draw'

# A Move is a:
#  - a tuple of (int, int)
# 
# Represents a move on the board. The first element of the tuple is the row of the move, and the second element is the column of the move.
Move = tuple[int, int]

# A BoardState is a list of 3 lists consisting of 3 CellStates each
BoardState = list[list[CellState]]