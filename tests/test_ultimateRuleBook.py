from ultimateTicTacToe.ultimateRuleBook import defaultUltimateRuleBook, move_on_correct_unit_board
from examples import emptyUltimateTicTacToeBoard, oneUnitBoardWonUltimateTicTacToeBoard

### Rule Tests 
print("Testing Rules")

## Move on Correct Unit Board with Empty Board

for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                assert move_on_correct_unit_board(emptyUltimateTicTacToeBoard, ((i, j), (k, l)))

print(" + move_on_correct_unit_board passed on empty board")

## Move on Correct Unit Board with one unit board won

unitBoardsNotWon = [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

for i in range(3):
    for j in range(3):
        for unitBoardNotWon in unitBoardsNotWon:
            assert move_on_correct_unit_board(oneUnitBoardWonUltimateTicTacToeBoard, ((i, j), ((0, 0), unitBoardNotWon)))
