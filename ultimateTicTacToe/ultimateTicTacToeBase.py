from abc import abstractmethod
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from unitTicTacToe.unitTicTacToeTypes import PlayerType, Result, CellState
from unitTicTacToe.unitTicTacToeBase import TicTacToe, TicTacToeFactory, TurnLessTicTacToe
from unitTicTacToe.ruleBook import defaultRuleBook as defaultUnitRuleBook
from ultimateTicTacToe.UnitGamesUtils import get_threes_in_a_row, is_wining_three_in_a_row
from ultimateTicTacToe.ultimateRuleBook import UltimateRuleBook, defaultUltimateRuleBook
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove, UnitGames

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
    def is_game_over(self) -> bool:
        pass

    @abstractmethod
    def get_last_move(self) -> UltimateMove:
        pass

    def toString() -> str:
        pass
    
    def winner(self) -> PlayerType:
        pass
  
    def result() -> Result:
        pass

class StrictUltimateTicTacToe(UltimateTicTacToe):
    """A UltimateTicTacToe game that enforces the rules of the game using a passed in RuleBook.
    """
    def __init__(self, board: UltimateBoardState, ruleBook: UltimateRuleBook = defaultUltimateRuleBook, turn: PlayerType = PlayerType.X):
        super().__init__()  
        self.unitGames = ultimate_board_state_to_unit_games(board)
        self.unit_games_list = sum(self.unitGames, [])
        self.ruleBook = ruleBook
        self.turn = turn
        self.pastMove = None
        self.board = self.generate_board()
        self.cached_winner = "Null"
        self.cached_is_board_full = None
        self.cached_possible_moves = None

    def get_turn(self) -> PlayerType:
        return self.turn
    
    def get_board_copy(self) -> UltimateBoardState:
        return np.copy(self.board)

    def generate_board(self) -> UltimateBoardState:
        row1Copy = self.generate_board_row(0)
        row2Copy = self.generate_board_row(1)
        row3Copy = self.generate_board_row(2)
        return np.array([row1Copy, row2Copy, row3Copy])
    
    def make_move(self, move: UltimateMove):
        if (self.ruleBook.is_valid(self.board, move, self.pastMove)):
            ultimateMove = move[0]
            unitMove = move[1]
            unitGame = self.unitGames[ultimateMove[0]][ultimateMove[1]]
            unitGame.make_move(unitMove, self.turn)
            self.pastMove = move
            self.board = self.generate_board()
            self.rotate_turn()
            self.cached_winner = "Null"
            self.cached_is_board_full = None
            self.cached_possible_moves = None
        else:
            raise Exception("Invalid move.")
        
    def move_follows_default_unit_rules(self, move: UltimateMove) -> bool:
            unitGame = self.unitGames[move[0][0]][move[0][1]]
            unitMove = move[1]
            return unitGame.move_valid(unitMove)

    def move_on_correct_unit_board(self, move: UltimateMove) -> bool:
        if self.pastMove == None:
            return True
        
        unitGame = self.unitGames[self.pastMove[1][0]][self.pastMove[1][1]]
        if unitGame.is_game_over():
            return True
        
        correctRow = self.pastMove[1][0] == move[0][0]
        correctColumn = self.pastMove[1][1] == move[0][1]
        return correctRow and correctColumn

    def move_valid(self, move: UltimateMove) -> bool:
        return self.move_follows_default_unit_rules(move) and self.move_on_correct_unit_board(move)

    def possible_moves(self) -> list[UltimateMove]:
        if self.cached_possible_moves != None:
            return self.cached_possible_moves
        
        possibleGames = []
        if self.pastMove == None or self.unitGames[self.pastMove[1][0]][self.pastMove[1][1]].is_game_over():
            for i in range(3):
                row = self.unitGames[i]
                for j in range(3):
                    game = row[j]
                    if not game.is_game_over():
                        possibleGames.append((game, (i, j)))
        else:
            unitGame = self.unitGames[self.pastMove[1][0]][self.pastMove[1][1]]
            firstDimension = self.pastMove[1]
            possibleGames = [(unitGame, firstDimension)]
        
        possibleMoves = []
        for game, firstDimension in possibleGames:
            for secondDimension in game.possible_moves():
                possibleMoves.append((firstDimension, secondDimension))
        self.cached_possible_moves = possibleMoves
        return possibleMoves
    
    def get_last_move(self) -> UltimateMove:
        return self.pastMove
    
    def has_someone_won(self) -> bool:
        return self.winner() != None
    
    def is_game_over(self) -> bool:
        return self.has_someone_won() or self.is_board_full()
    
    def winner(self) -> PlayerType:
        if self.cached_winner != "Null":
            return self.cached_winner
        threesInARow = get_threes_in_a_row(self.unitGames)
        for games in threesInARow:
            if is_wining_three_in_a_row(games):
                if games[0].winner() == PlayerType.X:
                    self.cached_winner = PlayerType.X
                    return PlayerType.X
                elif games[0].winner() == PlayerType.O:
                    self.cached_winner = PlayerType.O
                    return PlayerType.O
                else:
                    raise Exception("Invalid cell state.")

        self.cached_winner = None
        return None
        
    def result(self) -> Result:
        if not self.is_game_over():
            return None
        elif self.winner() == PlayerType.X:
            return Result.X
        elif self.winner() == PlayerType.O:
            return Result.O
        else:
            return Result.DRAW
    
    def generate_board_row(self, row: int) -> list[TicTacToe]:
        return np.array([game.board for game in self.unitGames[row]])
    
    def rotate_turn(self):
        self.turn = PlayerType.X if self.turn == PlayerType.O else PlayerType.O

    def is_board_full(self) -> bool:
        if self.cached_is_board_full != None:
            return self.cached_is_board_full
        boardFull = all(unit_game.is_game_over() for unit_game in self.unit_games_list)
        self.cached_is_board_full = boardFull
        return boardFull

    def toString(self) -> str:
        #initialize board string
        boardString = ""

        #for each row of tic tac toe boards
        for r in range(3):
            gameRow = self.unitGames[r]       

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

def ultimate_board_state_to_unit_games(board: UltimateBoardState) -> UnitGames:
    unitGames: UnitGames = []
    for row in board:
        gamesRow: list[TicTacToe] = []
        for unitBoard in row:
            gamesRow.append(TurnLessTicTacToe(unitBoard, defaultUnitRuleBook))
        unitGames.append(gamesRow)
    return unitGames

class UltimateTicTacToeFactory:
    @staticmethod
    def emptyStrictGame() -> UltimateTicTacToe:
        emptyBoard = np.full((3, 3, 3, 3), CellState.EMPTY.value)
        return StrictUltimateTicTacToe(emptyBoard, defaultUltimateRuleBook)
    
def format_board(board) -> UltimateBoardState:
    formatted_board = np.full((3,3,3,3), CellState.EMPTY.value)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if board[i][j][k][l] == CellState.X.value:
                        formatted_board[i][j][k][l] = CellState.X.value
                    elif board[i][j][k][l] == CellState.O.value:
                        formatted_board[i][j][k][l] = CellState.O.value
    return formatted_board

game = UltimateTicTacToeFactory.emptyStrictGame()