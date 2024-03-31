from unitTicTacToe.unitTicTacToeTypes import BoardState, Move
from unitTicTacToe.unitTicTacToeBase import TicTacToe

UltimateBoardState = list[list[BoardState]]

# A UltimateMove is a tuple of two Moves where the first Move is the unit board to play on and the second Move is the move to make on that unit board.
UltimateMove = tuple[Move, Move]

# A UnitGames is a list of 3 lists consisting of 3 TicTacToe games each
UnitGames = list[list[TicTacToe]]