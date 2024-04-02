from unitTicTacToe.unitHeuristic import three_in_line, fork, opp_three_in_line, unblocked_two_in_line, block_opp_three_in_line, unblocked_one_in_line
from unitTicTacToe.unitTicTacToeTypes import PlayerType
from examples import oneUnitBoardWonUltimateTicTacToeBoard, twoUnitBoardWonUltimateTicTacToeBoard, twoUnitBoardFork, twoUnitWinOneUnitLostUltimateTicTacToeBoard, ultimateTicTacToeBoard

assert(three_in_line(oneUnitBoardWonUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 1
assert(three_in_line(twoUnitBoardWonUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 2
assert(three_in_line(twoUnitBoardWonUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.O)) == 0

assert(opp_three_in_line(twoUnitWinOneUnitLostUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 1
assert(opp_three_in_line(twoUnitWinOneUnitLostUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.O)) == 2

assert(unblocked_two_in_line(twoUnitBoardFork, ((0, 0), (0, 1)), PlayerType.X)) == 4
assert(unblocked_two_in_line(twoUnitBoardFork, ((0, 0), (0, 1)), PlayerType.O)) == 0

# 1 in each won board, 5 in lost 
assert(block_opp_three_in_line(twoUnitWinOneUnitLostUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 7
# 2 in each won board, 2 in lost 
assert(block_opp_three_in_line(twoUnitWinOneUnitLostUltimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.O)) == 6

# 4 in board 2, 1 in board 1
assert(unblocked_one_in_line(ultimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.X)) == 6
assert(unblocked_one_in_line(ultimateTicTacToeBoard, ((0, 0), (0, 1)), PlayerType.O)) == 3

assert(fork(twoUnitBoardFork, ((0, 0), (0, 1)), PlayerType.X)) == 2
assert(fork(twoUnitBoardFork, ((0, 0), (0, 1)), PlayerType.O)) == 0