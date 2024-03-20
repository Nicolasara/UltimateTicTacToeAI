from __future__ import annotations
from typing import Callable
from ultimateTicTacToe import UltimateBoardState, UltimateMove

Rule = Callable[[UltimateBoardState, UltimateMove, UltimateMove], bool]

class UltimateRuleBook():
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def is_valid(self, board: UltimateBoardState, move: UltimateMove, pastMove: UltimateMove | None) -> bool:
        for rule in self.rules:
            if not rule(board, move, pastMove):
                return False
        return True

class UltimateRuleBookBuilder():
    def __init__(self) -> None:
        self.rules = []

    def add_rule(self, rule: Rule) -> UltimateRuleBookBuilder:
        self.rules.append(rule)
        return self
    
    def build(self) -> UltimateRuleBook:
        return UltimateRuleBook(self.rules)
    
def move_on_correct_simple_board(board: UltimateBoardState, move: UltimateMove, pastMove: UltimateMove) -> bool:
    if pastMove == None:
        return True
    correctRow = pastMove[1][0] == move[0][0]
    correctColumn = pastMove[1][1] == move[0][1]
    return correctRow and correctColumn

defaultUltimateRuleBook = UltimateRuleBookBuilder() \
                    .add_rule(move_on_correct_simple_board).build()

