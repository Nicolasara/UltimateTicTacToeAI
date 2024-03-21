from simpleTicTacToeTypes import BoardState, Move
from simpleTicTacToe import TicTacToe

UltimateBoardState = list[list[BoardState]]

# A UltimateMove is a tuple of two Moves where the first Move is the simple board to play on and the second Move is the move to make on that simple board.
UltimateMove = tuple[Move, Move]

# A SimplGame is a list of 3 lists consisting of 3 TicTacToe games each
SimpleGames = list[list[TicTacToe]]