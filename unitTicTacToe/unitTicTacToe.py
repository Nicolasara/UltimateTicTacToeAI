from abc import abstractmethod
from unitTicTacToe.ruleBook import RuleBook, defaultRuleBook
from unitTicTacToe.boardStateUtils import get_threes_in_a_row, is_wining_three_in_a_row
from unitTicTacToe.unitTicTacToeTypes import BoardState, Move, CellState, PlayerType, Result

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

    def winner(self) -> PlayerType | None:
        """Determines the winner of the game.

        Returns:
            PlayerType | None: Returns the winner of the game if there is one, otherwise returns None.
        """
        pass

    def result(self) -> Result | None:
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

    def get_turn(self) -> PlayerType:
        raise Exception("This implementation does not have a turn.")
    
    def get_board_copy(self) -> BoardState:
        return [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]]
        ]
    
    def make_move(self, move: Move, player: PlayerType):
        if (self.ruleBook.is_valid(self.get_board_copy(), move)):
            self.board[move[0]][move[1]] = player
        else:
            raise Exception("Invalid move.")

    def possible_moves(self) -> list[Move]:
        moves = []
        for i in range(3):
            for j in range(3):
                move: Move = (i, j)
                if self.ruleBook.is_valid(self.get_board_copy(), move):
                    moves.append(move)
        return moves
    
    def has_someone_won(self) -> bool:
        return self.winner() != None

    def is_game_over(self) -> bool:
        hasSomeoneWon = self.has_someone_won()
        boardFull = self.is_board_full()
        return hasSomeoneWon or boardFull
    
    def winner(self) -> PlayerType | None:
        xThreesInARow = 0
        oThreesInARow = 0
        threesInARow = get_threes_in_a_row(self.get_board_copy())
        for cells in threesInARow:
            if is_wining_three_in_a_row(cells):
                if cells[0] == CellState.X:
                    xThreesInARow += 1
                else:
                    oThreesInARow += 1
        
        if xThreesInARow == 0 and oThreesInARow == 0:
            return None
        elif xThreesInARow == 0:
            return PlayerType.O
        elif oThreesInARow == 0:
            return PlayerType.X
        else:
            raise Exception("There should only be one winner, but the board seems to have multiple winners.")

    def result(self) -> Result | None:
        if not self.is_game_over():
            return None
        elif self.winner() == PlayerType.X:
            return Result.X
        elif self.winner() == PlayerType.O:
            return Result.O
        else:
            return Result.DRAW


        
    def is_board_full(self) -> bool:
        for row in self.board:
            for cell in row:
                if cell == CellState.EMPTY:
                    return False
        return True
    
    
    def toString(self) -> str:
        boardString = ""

        #if there is winner, print it surrounded by spaces
        if self.is_game_over():
            winner = self.winner() if self.winner() != None else "-"
            for t in range(5):
                if t == 2:
                    boardString += " " * 5 + winner.value + " " * 5 + "\n"
                else:
                    boardString += " " * 11 + "\n"
            return boardString
        
        #else, print each row
        for r in range(3):
            row = self.board[r]
            #print each column in the row
            for c in range(3):
                col = row[c]
                if col == CellState.EMPTY:
                    col = " "
                else:
                    col = col.value
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
        emptyBoard = [
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
        ]
        return TurnLessTicTacToe(emptyBoard, defaultRuleBook)