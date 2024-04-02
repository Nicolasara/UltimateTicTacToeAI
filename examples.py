from unitTicTacToe.unitTicTacToeTypes import CellState

### Example of a empty board
emptyUnitBoard = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]

### Example of a tied board
tiedUnitBoard = [
    [CellState.X.value, CellState.O.value, CellState.X.value],
    [CellState.O.value, CellState.X.value, CellState.O.value],
    [CellState.O.value, CellState.X.value, CellState.O.value]
]

### Example of a won game
wonUnitBoard = [
    [CellState.X.value, CellState.O.value, CellState.X.value],
    [CellState.O.value, CellState.X.value, CellState.O.value],
    [CellState.X.value, CellState.EMPTY.value, CellState.EMPTY.value]
]

### Example of a lost game
lostUnitBoard = [
    [CellState.O.value, CellState.O.value, CellState.X.value],
    [CellState.O.value, CellState.X.value, CellState.O.value],
    [CellState.O.value, CellState.X.value, CellState.O.value]
]

forkUnitBoard = [
    [CellState.X.value, CellState.EMPTY.value, CellState.X.value],
    [CellState.EMPTY.value, CellState.O.value, CellState.EMPTY.value],
    [CellState.X.value, CellState.EMPTY.value, CellState.O.value]
]

emptyUnitBoard1 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard2 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard3 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard4 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard5 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard6 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard7 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard8 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUnitBoard9 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
emptyUltimateTicTacToeBoard = [
    [emptyUnitBoard1, emptyUnitBoard2, emptyUnitBoard3],
    [emptyUnitBoard4, emptyUnitBoard5, emptyUnitBoard6],
    [emptyUnitBoard7, emptyUnitBoard8, emptyUnitBoard9]
]

# Example of a board with some moves
ticTacToeBoard1 = [
    [CellState.X.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.O.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard2 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.X.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard3 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard4 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard5 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard6 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard7 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard8 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
ticTacToeBoard9 = [
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
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

twoUnitBoardWonUltimateTicTacToeBoard = [
    [wonUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, wonUnitBoard]
]

twoUnitWinOneUnitLostUltimateTicTacToeBoard = [
    [wonUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, lostUnitBoard],
    [wonUnitBoard, emptyUnitBoard, emptyUnitBoard]
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

twoUnitBoardFork = [
    [forkUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [emptyUnitBoard, emptyUnitBoard, emptyUnitBoard],
    [forkUnitBoard, emptyUnitBoard, emptyUnitBoard]
]
