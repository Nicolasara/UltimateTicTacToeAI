from ultimateTicTacToe.ultimateTicTacToeBase import StrictUltimateTicTacToe
from unitTicTacToe.unitTicTacToeBase import PlayerType
from ultimateTicTacToe.ultimateRuleBook import defaultUltimateRuleBook
from examples import oneUnitBoardWonUltimateTicTacToeBoard, gameWonUltimateTicTacToeBoard, gameWithThreeWinOptions
from ultimateTicTacToe.ultimateHeuristic import moveSendsOpponentToAnyBoard, playerHasWonUltimateBoard, opponentHasWonUltimateBoard, playerUltimateTwoInARows, opponentUltimateTwoInARows, blockedOpponentWins, playerUltimateOneInARows, opponentUltimateOneInARows

### Heuristic Tests
print("Testing Ultimate Heuristics")

### Test moveSendsOpponentToAnyBoard
game1 = StrictUltimateTicTacToe(oneUnitBoardWonUltimateTicTacToeBoard, defaultUltimateRuleBook)
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((0,0), (0,0)), PlayerType.X) == 1
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((0,0), (1,1)), PlayerType.O) == 0
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((0,0), (2,1)), PlayerType.X) == 0
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((1,1), (0,0)), PlayerType.O) == 1
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((1,1), (1,1)), PlayerType.X) == 0
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((1,1), (1,2)), PlayerType.X) == 0
assert moveSendsOpponentToAnyBoard(oneUnitBoardWonUltimateTicTacToeBoard, ((2,2), (0,0)), PlayerType.X) == 1


### Test hasWonUltimateBoard
diagonal_won_game = StrictUltimateTicTacToe(gameWonUltimateTicTacToeBoard, defaultUltimateRuleBook)
print(diagonal_won_game.toString())
assert playerHasWonUltimateBoard(gameWonUltimateTicTacToeBoard, ((0,0), (0,0)), PlayerType.X) == 1
assert playerHasWonUltimateBoard(gameWonUltimateTicTacToeBoard, ((0,0), (1,1)), PlayerType.O) == 0
assert opponentHasWonUltimateBoard(gameWonUltimateTicTacToeBoard, ((0,0), (0,0)), PlayerType.X) == 0
assert opponentHasWonUltimateBoard(gameWonUltimateTicTacToeBoard, ((0,0), (1,1)), PlayerType.O) == 1


### Test 2-in-a-row, blocked wins, and 1-in-a-row
winnable_game = StrictUltimateTicTacToe(gameWithThreeWinOptions, defaultUltimateRuleBook)
print(winnable_game.toString())
assert playerUltimateTwoInARows(gameWithThreeWinOptions, ((0,0), (0,0)), PlayerType.X) == 2
assert opponentUltimateTwoInARows(gameWithThreeWinOptions, ((0,0), (0,0)), PlayerType.X) == 0
assert playerUltimateTwoInARows(gameWithThreeWinOptions, ((0,0), (1,1)), PlayerType.O) == 0
assert opponentUltimateTwoInARows(gameWithThreeWinOptions, ((0,0), (1,1)), PlayerType.O) == 2
assert blockedOpponentWins(gameWithThreeWinOptions, ((0,0), (0,0)), PlayerType.X) == 1
assert playerUltimateOneInARows(gameWithThreeWinOptions, ((0,0), (0,0)), PlayerType.X) == 2
assert opponentUltimateOneInARows(gameWithThreeWinOptions, ((0,0), (0,0)), PlayerType.X) == 1
assert playerUltimateOneInARows(gameWithThreeWinOptions, ((0,0), (1,1)), PlayerType.O) == 1
assert opponentUltimateOneInARows(gameWithThreeWinOptions, ((0,0), (1,1)), PlayerType.O) == 2
