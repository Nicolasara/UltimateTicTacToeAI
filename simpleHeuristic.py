from typing import Callable
from ultimateTicTacToeTypes import BoardState

Simple_Heuristic_Rule = Callable[[BoardState], str]

class SimpleHeuristic():
    def __init__(self, heuristics: list[Simple_Heuristic_Rule]):
        self.heuristics = heuristics


class SimpleHeuristicBuilder():
    def __init__(self) -> None:
        self.heuristics = []

    def add_heuristic(self, heuristic: Simple_Heuristic_Rule) -> SimpleHeuristicBuilder:
        self.heuristics.append(heuristic)
        return self
    
    def build(self) -> SimpleHeuristic:
        return SimpleHeuristic(self.rules)

def _check_num_in_lines(board: BoardState, player: str, num: int, blocked: bool):
    result = 0
    opp = 'O'
    if player == 'O':
        opp = 'X'
        
    # check for horizontal consecutive
    for i in range(3):
        total_in_row = 0
        other_in_row = 0
        for j in range(3):
            if board[i][j] == player:
                total_in_row += 1
            elif blocked and board[i][j] == opp:
                other_in_row += 1
            elif not blocked and board[i][j] == '':
                other_in_row += 1
        if (total_in_row == num and other_in_row == 3 - num):
            result += 1

    # check for vertical consecutive
    for i in range(3):
        total_in_col = 0
        other_in_col = 0
        for j in range(3):
            if board[j][i] == player:
                total_in_col += 1
            elif blocked and board[j][i] == opp:
                other_in_col += 1
            elif not blocked and board[j][i] == '':
                other_in_col += 1
        if (total_in_col == num and other_in_col == 3 - num):
            result += 1
        
    # check for diagonal consecutive
    for i in range(2):
        total_in_diag_left = 0
        other_in_diag_left = 0
        total_in_diag_right = 0
        other_in_diag_right = 0
        for j in range(3):
            if board[j][j] == player:
                total_in_diag_left += 1
            elif blocked and board[j][j] == opp:
                other_in_diag_left += 1
            elif not blocked and board[j][j] == '':
                other_in_diag_left += 1
            if board[2-j][j] == player:
                total_in_diag_right += 1
            elif blocked and board[2-j][j] == opp:
                other_in_diag_right += 1
            elif not blocked and board[2-j][j] == '':
                other_in_diag_right += 1
                
        if ((total_in_diag_left == num and other_in_diag_left == 3 - num) 
            or (total_in_diag_right == num and other_in_diag_right == 3 - num)):
            result += 1
    return result

def three_in_line(board: BoardState, player: str):
    return _check_num_in_lines(board, player, 3, False)

def not_three_in_line(board: BoardState, player: str):
    if player == 'X':
        return _check_num_in_lines(board, 'O', 3, False)
    else:
        return _check_num_in_lines(board, 'X', 3, False)
    
def unblocked_two_in_line(board: BoardState, player: str):
    return _check_num_in_lines(board, player, 2, False)

def block_opp_three_in_line(board: BoardState, player: str):
    # fliping the player because our call to check_consecutive checks if the player passed in has 2 in a row
    if player == 'X':
        return _check_num_in_lines(board, 'O', 2, True)
    else: 
        return _check_num_in_lines(board, 'X', 2, True) 

def fork(board: BoardState, player: str):
    return unblocked_two_in_line(board, player) >= 2

def unblocked_one_in_line(board: BoardState, player):
    return _check_num_in_lines(board, player, 1, False)
