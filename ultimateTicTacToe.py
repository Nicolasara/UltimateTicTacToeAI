from abc import abstractmethod
from player import Move, TwoDimensionalMove
from typing import List
from enum import Enum

PlayerType = 'X' | 'O'

BoardState = PlayerType

# TicTacToe interface
class TicTacToe:
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    @abstractmethod
    def get_turn(self) -> PlayerType:
        pass

    @abstractmethod
    def get_board_copy(self) -> BoardState:
        pass

    @abstractmethod
    def make_move(self, move: Move):
        pass

    def toString(self) -> str:
        boardString = ""

        #if there is winner, print it surrounded by spaces
        if self.winner() != None:
            for t in range(5):
                if t == 2:
                    boardString += " " * 5 + self.winner() + " " * 5 + "\n"
                else:
                    boardString += " " * 11 + "\n"
            return boardString
        
        #else, print each row
        for r in range(3):
            row = self.board[r]
            #print each column in the row
            for c in range(3):
                col = row[c]
                boardString += " " + col + " "
                #divider
                if c != 2:
                    boardString += "|"
            #horizontal divider
            if r != 2:
                boardString += "\n---|---|---\n"
        return boardString 

# UltimateTicTacToe interface
class UltimateTicTacToe:
    board = [[TicTacToe(), TicTacToe(), TicTacToe()], [TicTacToe(), TicTacToe(), TicTacToe()], [TicTacToe(), TicTacToe(), TicTacToe()]]

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

    def toString(self) -> str:
        #initialize board string
        boardString = ""

        #for each row of tic tac toe boards
        for r in range(3):
            gameRow = self.board[r]       

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