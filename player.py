from typing import NamedTuple

    # playAGame takes in two players
# each player is type (UltimateTicTacToe) -> Move
# map of heuristic to weight
def player(game_board, heuristics):
    # pick move based on heuristic
    # check valid move 
    chosen_move = nil
    while chosen_move not in possibleMoves:
        pass
pass

class Move(NamedTuple):
    row: int
    col: int
    
class TwoDimensionalMove(NamedTuple):
    big_row: int
    big_col: int
    lil_row: int
    lil_col: int
    

class Player:
    # heuristic_map is a dictionary of heuristic functions and weights
    # heuristic functions return a number
    def __init__(self, heuristic_map) -> None:
        self.heuristic_map = heuristic_map
    
    # minimax
    @abstractmethod
    def get_move(self) -> TwoDimensionalMove:
        pass