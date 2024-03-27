from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove, UnitGames
from ultimateTicTacToe.ultimateTicTacToe import UltimateTicTacToe, UltimateTicTacToeFactory

strictUltimateTicTacToe = UltimateTicTacToeFactory.emptyStrictGame()

strictUltimateTicTacToe.make_move(((0, 0), (0, 0)))
assert len(strictUltimateTicTacToe.possible_moves()) == 8

