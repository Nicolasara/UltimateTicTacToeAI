from abc import abstractmethod
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from unitTicTacToe.unitTicTacToeTypes import PlayerType, Result, CellState
from unitTicTacToe.unitTicTacToeBase import TicTacToe, TurnLessTicTacToe
from unitTicTacToe.ruleBook import defaultRuleBook as defaultUnitRuleBook
from ultimateTicTacToe.UnitGamesUtils import get_threes_in_a_row, is_wining_three_in_a_row
from ultimateTicTacToe.ultimateRuleBook import UltimateRuleBook, defaultUltimateRuleBook
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove, UnitGames
import numpy as np

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
        self.ruleBook = ruleBook
        self.turn = turn
        self.pastMove = None

    def get_turn(self) -> PlayerType:
        return self.turn
    
    def get_board_copy(self) -> UltimateBoardState:
        row1Copy = self.get_ultimate_board_row_copy(0)
        row2Copy = self.get_ultimate_board_row_copy(1)
        row3Copy = self.get_ultimate_board_row_copy(2)
        return np.array([row1Copy, row2Copy, row3Copy])
    
    def make_move(self, move: UltimateMove):
        if (self.ruleBook.is_valid(self.get_board_copy(), move, self.pastMove)):
            ultimateMove = move[0]
            unitMove = move[1]
            unitGame = self.unitGames[ultimateMove[0]][ultimateMove[1]]
            unitGame.make_move(unitMove, self.turn)
            self.pastMove = move
            self.rotate_turn()
        else:
            raise Exception("Invalid move.")
        
    def possible_moves(self) -> list[UltimateMove]:
        possibleMoves = []
        for ultimateRow in range(3):
            for ultimateColumn in range(3):
                ultimateMove = (ultimateRow, ultimateColumn)
                for unitRow in range(3):
                    for unitColumn in range(3):
                        unitMove = (unitRow, unitColumn)
                        move = (ultimateMove, unitMove)
                        if self.ruleBook.is_valid(self.get_board_copy(), move, self.pastMove):
                            possibleMoves.append(move)
        return possibleMoves
    
    def get_last_move(self) -> UltimateMove:
        return self.pastMove
    
    def has_someone_won(self) -> bool:
        return self.winner() != None
    
    def is_game_over(self) -> bool:
        hasSomeoneWon = self.has_someone_won()
        boardFull = self.is_board_full()
        return hasSomeoneWon or boardFull
    
    def winner(self) -> PlayerType:
        xThreesInARow = 0
        oThreesInARow = 0
        threesInARow = get_threes_in_a_row(self.unitGames)
        for games in threesInARow:
            if is_wining_three_in_a_row(games):
                if games[0].winner() == PlayerType.X:
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
        
    def result(self) -> Result:
        if not self.is_game_over():
            return None
        elif self.winner() == PlayerType.X:
            return Result.X
        elif self.winner() == PlayerType.O:
            return Result.O
        else:
            return Result.DRAW
    
    def get_ultimate_board_row_copy(self, row: int) -> list[TicTacToe]:
        return np.array([game.get_board_copy() for game in self.unitGames[row]])
    
    def rotate_turn(self):
        self.turn = PlayerType.X if self.turn == PlayerType.O else PlayerType.O

    def is_board_full(self) -> bool:
        flattenedGames = [game for row in self.unitGames for game in row]
        with ThreadPoolExecutor() as executor:
            isBoardFull = list(executor.map(lambda game: game.is_board_full(), flattenedGames))
            if not any(isBoardFull):
                return False
        return True

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
    
game = UltimateTicTacToeFactory.emptyStrictGame()