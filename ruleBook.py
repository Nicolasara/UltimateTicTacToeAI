from __future__ import annotations
from typing import Callable
from simpleTicTacToeTypes import BoardState, Move, CellState

# A Rule is a function that takes a BoardState and a Move and returns a boolean, where True means the move is valid and False means the move is invalid.
Rule = Callable[[BoardState, Move], bool]

class RuleBook():
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def is_valid(self, board: BoardState, move: Move) -> bool:
        for rule in self.rules:
            if not rule(board, move):
                return False
        return True

class RuleBookBuilder():
    def __init__(self) -> None:
        self.rules = []

    def add_rule(self, rule: Rule) -> RuleBookBuilder:
        self.rules.append(rule)
        return self
    
    def build(self) -> RuleBook:
        return RuleBook(self.rules)
    
def move_on_empty_cell(board: BoardState, move: Move) -> bool:
    return board[move[0]][move[1]] == CellState.EMPTY

def move_in_bounds(_: BoardState, move: Move) -> bool:
    return 0 <= move[0] < 3 and 0 <= move[1] < 3

def game_has_not_been_won(board: BoardState, _: Move) -> bool:
    column1 = [board[0][0], board[1][0], board[2][0]]
    column2 = [board[0][1], board[1][1], board[2][1]]
    column3 = [board[0][2], board[1][2], board[2][2]]
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    threesInARow = [
        column1, column2, column3,
        row1, row2, row3,
        diagonal1, diagonal2
    ]
    gameWon = any([cells[0] == cells[1] == cells[2] and cells[0] != CellState.EMPTY for cells in threesInARow])
    return not gameWon

defaultRuleBook = RuleBookBuilder() \
                    .add_rule(move_on_empty_cell) \
                    .add_rule(move_in_bounds) \
                    .add_rule(game_has_not_been_won).build()
