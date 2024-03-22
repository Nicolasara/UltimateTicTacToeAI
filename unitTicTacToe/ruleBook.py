from __future__ import annotations
from typing import Callable
from unitTicTacToe.boardStateUtils import has_board_been_won
from unitTicTacToe.unitTicTacToeTypes import BoardState, Move, CellState

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
    try:
        return board[move[0]][move[1]] == CellState.EMPTY
    except IndexError:
        return False

def move_in_bounds(_: BoardState, move: Move) -> bool:
    return 0 <= move[0] < 3 and 0 <= move[1] < 3

def game_has_not_been_won(board: BoardState, _: Move) -> bool:
    gameWon = has_board_been_won(board)
    return not gameWon

defaultRuleBook = RuleBookBuilder() \
                    .add_rule(move_on_empty_cell) \
                    .add_rule(move_in_bounds) \
                    .add_rule(game_has_not_been_won).build()
