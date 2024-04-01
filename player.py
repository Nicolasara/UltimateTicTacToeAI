from typing import NamedTuple
from ultimateTicTacToe.ultimateTicTacToe import UltimateTicTacToe
from minimax import minimax

class Move(NamedTuple):
    row: int
    col: int
    
class TwoDimensionalMove(NamedTuple):
    big_row: int
    big_col: int
    lil_row: int
    lil_col: int
    

class Player:
    def __init__(self, board_evaluator: BoardEvaluator, maximizing: bool) -> None:
        self.evaluator = board_evaluator
        self.maximizing = maximizing
    
    def best_move(self, game, depth=3) -> TwoDimensionalMove:
        _, move = minimax(game, self.evaluator, depth, self.maximizing, True)
        return move
    
    def get_evaluator(self):
        return self.evaluator
    
    def set_evaluator(self, evaluator):
        self.evaluator = evaluator