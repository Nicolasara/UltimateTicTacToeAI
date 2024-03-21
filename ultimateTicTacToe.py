from abc import abstractmethod
from simpleTicTacToe import PlayerType, Result, TicTacToe, TurnLessTicTacToe
from ruleBook import defaultRuleBook as defaultSimpleRuleBook
from ultimateRuleBook import UltimateRuleBook, defaultUltimateRuleBook
from ultimateTicTacToeTypes import UltimateBoardState, UltimateMove, SimpleGames

# UltimateTicTacToe interface
class UltimateTicTacToe:
    @abstractmethod
    def get_turn(self) -> PlayerType:
        pass

    @abstractmethod
    def get_board_copy(self) -> UltimateBoardState:
        pass

    @abstractmethod
    def make_move(self, move: UltimateMove):
        pass

    @abstractmethod
    def possible_moves(self) -> list[UltimateMove]:
        pass

    def has_someone_won() -> bool:
        pass
    
    @abstractmethod
    def is_game_over() -> bool:
        pass

    def toString() -> str:
        pass
    
    def winner() -> PlayerType | None:
        pass
  
    def result() -> Result | None:
        pass

class StrictUltimateTicTacToe(UltimateTicTacToe):
    """A UltimateTicTacToe game that enforces the rules of the game using a passed in RuleBook.
    """
    def __init__(self, board: UltimateBoardState, ruleBook: UltimateRuleBook):
        super().__init__()  
        self.simpleGames = ultimate_board_state_to_simple_games(board)
        self.ruleBook = ruleBook
        self.turn = PlayerType.X
        self.pastMove = None

    def get_turn(self) -> PlayerType:
        return self.turn
    
    def get_board_copy(self) -> UltimateBoardState:
        row1Copy = self.get_ultimate_board_row_copy(0)
        row2Copy = self.get_ultimate_board_row_copy(1)
        row3Copy = self.get_ultimate_board_row_copy(2)
        return [row1Copy, row2Copy, row3Copy]
    
    def make_move(self, move: UltimateMove):
        if (self.ruleBook.is_valid(self.get_board_copy(), move, self.pastMove)):
            ultimateMove = move[0]
            simpleMove = move[1]
            simpleGame = self.simpleGames[ultimateMove[0]][ultimateMove[1]]
            simpleGame.make_move(simpleMove, self.turn)
            self.rotate_turn()
        else:
            raise Exception("Invalid move.")
        
    def possible_moves(self) -> list[UltimateMove]:
        possibleMoves = []
        for row in range(3):
            for column in range(3):
                simpleGame = self.simpleGames[row][column]
                for move in simpleGame.possible_moves():
                    possibleMoves.append(((row, column), move))
        return possibleMoves
    
    def has_someone_won(self) -> bool:
        return self.winner() != None
    
    def is_game_over(self) -> bool:
        hasSomeoneWon = self.has_someone_won()
        boardFull = self.is_board_full()
        return hasSomeoneWon or boardFull
    
    def winner(self) -> PlayerType | None:
        xThreesInARow = 0
        oThreesInARow = 0
        threesInARow = self.get_threes_in_a_row()
        for games in threesInARow:
            if self.is_three_in_a_row(games):
                if games[0].winner() == 'X':
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
    
    def get_ultimate_board_row_copy(self, row: int) -> list[TicTacToe]:
        return [game.get_board_copy() for game in self.simpleGames[row]]
    
    def rotate_turn(self):
        self.turn = PlayerType.X if self.turn == PlayerType.O else PlayerType.O

    def is_board_full(self) -> bool:
        for row in self.simpleGames:
            for game in row:
                if not game.is_board_full():
                    return False
        return True
    
    def get_threes_in_a_row(self) -> list[list[TicTacToe]]:
        column1 = self.get_column(0)
        column2 = self.get_column(1)
        column3 = self.get_column(2)
        row1 = self.get_row(0)
        row2 = self.get_row(1)
        row3 = self.get_row(2)
        diagonal1 = self.get_diagonal(1)
        diagonal2 = self.get_diagonal(2)

        return [
            column1, column2, column3,
            row1, row2, row3,
            diagonal1, diagonal2
        ]
    
    def get_column(self, column: int) -> list[TicTacToe]:
        return [self.simpleGames[0][column], self.simpleGames[1][column], self.simpleGames[2][column]]
    
    def get_row(self, row: int) -> list[TicTacToe]:
        return self.simpleGames[row]
    
    def get_diagonal(self, diagonal: int) -> list[TicTacToe]:
        """Gets the diagonal simpleTicTacToe games of the ultimate board.

        Args:
            diagonal (int): The diagonal to get. 1 for the top-left to bottom-right diagonal, 2 for the top-right to bottom-left diagonal.

        Returns:
            list[TicTacToe]: The diagonal of simple games of the ultimate board.
        """
        if diagonal == 1:
            return [self.simpleGames[0][0], self.simpleGames[1][1], self.simpleGames[2][2]]
        else:
            return [self.simpleGames[0][2], self.simpleGames[1][1], self.simpleGames[2][0]]
    
    def is_three_in_a_row(self, games: list[TicTacToe]) -> bool:
        return games[0].winner() == games[1].winner() == games[2].winner() and games[0].winner() != None

    def toString(self) -> str:
        #initialize board string
        boardString = ""

        #for each row of tic tac toe boards
        for r in range(3):
            gameRow = self.simpleGames[r]       

            #get boards as lists of rows
            b1 = gameRow[0].toString().split("\n")
            b2 = gameRow[1].toString().split("\n")
            b3 = gameRow[2].toString().split("\n")

            #combine rows of each smaller board into full-width rows
            row = ['||'.join(item) for item in zip(b1, b2, b3)]
            for l in row:
                boardString += l + "\n"

            #if not the last row, add vertical divider
            if r != 2:
                boardString += "===========||===========||===========\n"
        return boardString

def ultimate_board_state_to_simple_games(board: UltimateBoardState) -> SimpleGames:
    simpleGames: SimpleGames = []
    for row in board:
        gamesRow: list[TicTacToe] = []
        for simpleBoard in row:
            gamesRow.append(TurnLessTicTacToe(simpleBoard, defaultSimpleRuleBook))
        simpleGames.append(gamesRow)
    return simpleGames

class UltimateTicTacToeFactory:
    @staticmethod
    def emptyTurnLessGame() -> UltimateTicTacToe:
        emptyBoard = [[[['' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        print("emptyBoard: ", emptyBoard)
        return StrictUltimateTicTacToe(emptyBoard, defaultUltimateRuleBook)
    
game = UltimateTicTacToeFactory.emptyTurnLessGame()