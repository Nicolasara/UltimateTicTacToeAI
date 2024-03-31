from unitTicTacToe.unitHeuristic import three_in_line, fork
from unitTicTacToe.unitTicTacToeTypes import PlayerType
from examples import oneUnitBoardWonUltimateTicTacToeBoard, twoUnitBoardWonUltimateTicTacToeBoard, twoUnitBoardFork

assert(three_in_line(oneUnitBoardWonUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 1
assert(three_in_line(twoUnitBoardWonUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 2

assert(fork(twoUnitBoardFork, ((0, 0), (0, 1)), PlayerType.X)) == 2