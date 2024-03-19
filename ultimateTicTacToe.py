from abc import abstractmethod

PlayerType = 'X' | 'O'

BoardState = PlayerType

# TicTacToe interface
class TicTacToe:
    @abstractmethod
    def get_turn(self) -> PlayerType:
        pass

    @abstractmethod
    def get_board_copy(self) -> BoardState:
        pass

    @abstractmethod
    def make_move(self, move: Move):
        pass

# UltimateTicTacToe interface
class UltimateTicTacToe:
    @abstractmethod
    def get_turn(self) -> PlayerType:
        pass

    @abstractmethod
    def get_board_copy(self) -> BoardState:
        pass

    @abstractmethod
    def make_move(self, move: TwoDimensionalMove):
        pass

    @abstractmethod
    def possible_moves(self) -> TwoDimensionalMove[]:
        pass

    def  has_someone_won() -> bool:
        pass
    
    @abstractmethod
    def is_game_over() -> bool:
        pass
    
    def winner() -> PlayerType | None:
        pass
  
    def result() -> Result | None:
        pass

# min max algorithm
# evaluation function 
    
### Example of a empty board
emptyTicTacToeBoard1 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard2 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard3 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard4 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard5 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard6 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard7 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard8 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyTicTacToeBoard9 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
emptyUltimateTicTacToeBoard = [
    [emptyTicTacToeBoard1, emptyTicTacToeBoard2, emptyTicTacToeBoard3],
    [emptyTicTacToeBoard4, emptyTicTacToeBoard5, emptyTicTacToeBoard6],
    [emptyTicTacToeBoard7, emptyTicTacToeBoard8, emptyTicTacToeBoard9]
]

# Example of a board with some moves
ticTacToeBoard1 = [
    ['X', '', ''],
    ['', 'O', ''],
    ['', '', '']
]
ticTacToeBoard2 = [
    ['', '', ''],
    ['', 'X', ''],
    ['', '', '']
]
ticTacToeBoard3 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ticTacToeBoard4 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ticTacToeBoard5 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ticTacToeBoard6 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ticTacToeBoard7 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ticTacToeBoard8 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ticTacToeBoard9 = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
ultimateTicTacToeBoard = [
    [ticTacToeBoard1, ticTacToeBoard2, ticTacToeBoard3],
    [ticTacToeBoard4, ticTacToeBoard5, ticTacToeBoard6],
    [ticTacToeBoard7, ticTacToeBoard8, ticTacToeBoard9]
]   