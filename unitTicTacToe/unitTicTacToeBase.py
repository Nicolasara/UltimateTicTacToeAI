from abc import abstractmethod
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from unitTicTacToe.ruleBook import RuleBook, defaultRuleBook
from unitTicTacToe.boardStateUtils import get_threes_in_a_row, is_wining_three_in_a_row
from unitTicTacToe.unitTicTacToeTypes import BoardState, Move, CellState, PlayerType, Result

BoardSize = 3

# TicTacToe interface
class TicTacToe:
    @abstractmethod
    
    def get_turn(self) -> PlayerType:
        """Get the player whose turn it is to move.

        Returns:
            PlayerType: Returns a PlayerType representing the player whose turn it is to move.
        """
        pass

    @abstractmethod
    def get_board_copy(self) -> BoardState:
        """Makes a deep copy of the current board state.

        Returns:
            BoardState: A deep copy of the current board state.
        """
        pass

    @abstractmethod
    def make_move(self, move: Move, player: PlayerType):
        """Makes a move on the board.

        Args:
            move (Move): The move to be made on the board.
            player (PlayerType): The player making the move.
        """
        pass

    def possible_moves(self) -> list[Move]:
        """Finds all possible moves that can be made on the board.

        Returns:
            list[Move]: A list of all possible moves that can be made on the board.
        """
        pass

    def has_someone_won(self) -> bool:
        """Determines if either player has won the game.

        Returns:
            bool: True if either player has won the game, False otherwise.
        """
        pass

    def is_game_over(self) -> bool:
        """Determines if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        pass

    def winner(self) -> PlayerType:
        """Determines the winner of the game.

        Returns:
            PlayerType | None: Returns the winner of the game if there is one, otherwise returns None.
        """
        pass

    def result(self) -> Result:
        """Determines the result of the game.

        Returns:
            Result | None: Returns the result of the game if there is one, otherwise returns None.
        """
        pass

    def toString(self) -> str:
        pass

class TurnLessTicTacToe(TicTacToe):
    """A turn-less implementation of the TicTacToe interface which enforces the rules of the game using a RuleBook.
    """

    def __init__(self, board: BoardState, ruleBook: RuleBook):
        super().__init__()
        self.board = board
        self.ruleBook = ruleBook
        self.cached_winner = "Null"
        self.cached_is_board_full = None
        self.cached_possible_moves = None

    def get_turn(self) -> PlayerType:
        raise Exception("This implementation does not have a turn.")
    
    def get_board_copy(self) -> BoardState:
        return np.copy(self.board)
    
    def make_move(self, move: Move, player: PlayerType):
        if (self.move_valid(move)):
            if (player == PlayerType.X):
                cellState = CellState.X.value
            else:   
                cellState = CellState.O.value
            self.board[move[0]][move[1]] = cellState
            self.cached_winner = "Null"
            self.cached_is_board_full = None
            self.cached_possible_moves = None
        else:
            raise Exception("Invalid move.")

    def move_valid(self, move: Move) -> bool:
        onEmptyCell = self.board[move[0]][move[1]] == CellState.EMPTY.value
        gameNotOver = not self.is_game_over()
        return onEmptyCell and gameNotOver

    def possible_moves(self) -> list[Move]:
        if self.cached_possible_moves != None:
            return self.cached_possible_moves
        moves = np.array(np.meshgrid(np.arange(BoardSize), np.arange(BoardSize))).T.reshape(-1, 2)
        validMoves = [move for move in moves if self.move_valid(move)]
        return validMoves
    
    def has_someone_won(self) -> bool:
        return self.winner() != None

    def is_game_over(self) -> bool:
        hasSomeoneWon = self.has_someone_won()
        boardFull = self.is_board_full()
        return hasSomeoneWon or boardFull
    
    def winner(self) -> PlayerType:
        if self.cached_winner != "Null":
            return self.cached_winner
        xThreesInARow = 0
        oThreesInARow = 0
        threesInARow = get_threes_in_a_row(self.get_board_copy())
        for cells in threesInARow:
            if is_wining_three_in_a_row(cells):
                if cells[0] == CellState.X.value:
                    xThreesInARow += 1
                else:
                    oThreesInARow += 1
        if xThreesInARow == 0 and oThreesInARow == 0:
            self.cached_winner = None
            return None
        elif xThreesInARow == 0:
            self.cached_winner = PlayerType.O
            return PlayerType.O
        elif oThreesInARow == 0:
            self.cached_winner = PlayerType.X
            return PlayerType.X
        else:
            raise Exception("There should only be one winner, but the board seems to have multiple winners.")

    def result(self) -> Result:
        if not self.is_game_over():
            return None
        elif self.winner() == PlayerType.X:
            return Result.X
        elif self.winner() == PlayerType.O:
            return Result.O
        else:
            return Result.DRAW

    def is_board_full(self) -> bool:
        if self.cached_is_board_full != None:
            return self.cached_is_board_full
        boardFull = CellState.EMPTY.value not in self.board
        self.cached_is_board_full = boardFull
        return boardFull
    
    def toString(self) -> str:
        boardString = ""

        #if there is winner, print it surrounded by spaces
        if self.is_game_over():
            winner = self.winner() if self.winner() != None else "-"
            for t in range(5):
                if t == 2:
                    boardString += " " * 5 + winner.value + " " * 5 + "\n"
                elif t == 4:
                    boardString += " " * 11
                else:
                    boardString += " " * 11 + "\n"
            return boardString
        
        #else, print each row
        for r in range(3):
            row = self.board[r]
            #print each column in the row
            for c in range(3):
                col = row[c]
                if col == CellState.EMPTY.value:
                    col = " "
                elif col == CellState.X.value:
                    col = "X"
                elif col == CellState.O.value:
                    col = "O"
                else:
                    raise Exception("Invalid cell state.")
                boardString += " " + col + " "
                #divider
                if c != 2:
                    boardString += "|"
            #horizontal divider
            if r != 2:
                boardString += "\n---|---|---\n"
        return boardString 
    

# class lenientTicTacToe(TicTacToe):
#     """A lenient implementation of the TicTacToe interface which does not enforce the rules of the game.
#     """

#     def __init__(self, board: BoardState, turn: PlayerType):
#         super().__init__()

#     def get_turn(self) -> PlayerType:
#         return self.turn
        
class TicTacToeFactory:
    @staticmethod
    def empty_turn_less_game() -> TicTacToe:
        emptyBoard = np.full((3,3), CellState.EMPTY.value)
        return TurnLessTicTacToe(emptyBoard, defaultRuleBook)
    
    @staticmethod
    def turn_less_game_from_board(board: BoardState) -> TicTacToe:
        return TurnLessTicTacToe(board, defaultRuleBook)

# def format_board(board) -> BoardState:
#     formatted_board = np.full((3,3), CellState.EMPTY.value)
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == CellState.X.value:
#                 formatted_board[i][j] = CellState.X.value
#             elif board[i][j] == CellState.O.value:
#                 formatted_board[i][j] = CellState.O.value
#     return formatted_board