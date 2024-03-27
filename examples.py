from unitTicTacToe.unitTicTacToeTypes import CellState

### Example of a empty board
emptyUnitBoard = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]

### Example of a tied board
tiedUnitBoard = [
    [CellState.X, CellState.O, CellState.X],
    [CellState.O, CellState.X, CellState.O],
    [CellState.O, CellState.X, CellState.O]
]

### Example of a won game
wonUnitBoard = [
    [CellState.X, CellState.O, CellState.X],
    [CellState.O, CellState.X, CellState.O],
    [CellState.X, CellState.EMPTY, CellState.EMPTY]
]

### Example of a lost game
lostUnitBoard = [
    [CellState.O, CellState.O, CellState.X],
    [CellState.O, CellState.X, CellState.O],
    [CellState.O, CellState.X, CellState.O]
]

emptyUnitBoard1 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard2 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard3 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard4 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard5 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard6 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard7 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard8 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUnitBoard9 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
emptyUltimateTicTacToeBoard = [
    [emptyUnitBoard1, emptyUnitBoard2, emptyUnitBoard3],
    [emptyUnitBoard4, emptyUnitBoard5, emptyUnitBoard6],
    [emptyUnitBoard7, emptyUnitBoard8, emptyUnitBoard9]
]

# Example of a board with some moves
ticTacToeBoard1 = [
    [CellState.X, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.O, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard2 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.X, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard3 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard4 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard5 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard6 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard7 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard8 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ticTacToeBoard9 = [
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
    [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
]
ultimateTicTacToeBoard = [
    [ticTacToeBoard1, ticTacToeBoard2, ticTacToeBoard3],
    [ticTacToeBoard4, ticTacToeBoard5, ticTacToeBoard6],
    [ticTacToeBoard7, ticTacToeBoard8, ticTacToeBoard9]
]   

oneUnitBoardWonUltimateTicTacToeBoard = [
    [wonUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, emptyUnitBoard]
]

gameWonUltimateTicTacToeBoard = [
    [wonUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, wonUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, wonUnitBoard]
]

gameWithThreeWinOptions = [
    [wonUnitBoard, emptyUnitBoard, wonUnitBoard],
    [emptyUnitBoard, wonUnitBoard, lostUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, lostUnitBoard]
]

