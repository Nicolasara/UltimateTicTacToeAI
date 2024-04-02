import numpy as np
from ultimateTicTacToe.ultimateTicTacToeBase import StrictUltimateTicTacToe, ultimate_board_state_to_unit_games
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateMove, UltimateBoardState
from unitTicTacToe.unitTicTacToeBase import PlayerType
from ultimateTicTacToe.ultimateRuleBook import defaultUltimateRuleBook
import math

def _check_num_in_ultimate_lines(board: UltimateBoardState, condition: str):
    result = 0
    unit_games = ultimate_board_state_to_unit_games(board)
    def convert_winner_to_num(game):
        if (game.winner() == PlayerType.X):
            return 1
        elif (game.winner() == PlayerType.O):
            return 5
        else:
            return 0
        
    sum_dict = {0:"empty", 1: "1X", 2: "2X", 3: "3X", 5:"1O", 6:"1X1O", 7:"2X1O", 10:"2O", 11:"1X2O", 15:"3O"}
    value_arr_func = np.vectorize(convert_winner_to_num)
    value_arr = value_arr_func(unit_games)

    # check for horizontal consecutive
    horizontal_sum = value_arr.sum(axis=1)
    if sum_dict[horizontal_sum[0]] == condition:
        result += 1
    if sum_dict[horizontal_sum[1]] == condition:
        result += 1
    if sum_dict[horizontal_sum[2]] == condition:
        result += 1    

    # check for vertical consecutive
    vertical_sum = value_arr.sum(axis=0)
    if sum_dict[vertical_sum[0]] == condition:
        result += 1
    if sum_dict[vertical_sum[1]] == condition:
        result += 1
    if sum_dict[vertical_sum[2]] == condition:
        result += 1  

    # check for diagonal consecutive
    diag1 = np.trace(value_arr)
    diag2 = np.trace(value_arr[::-1])
    if sum_dict[diag1] == condition:
        result += 1
    if sum_dict[diag2] == condition:
        result += 1
    return result


def XWinsUltimateGame(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    game = StrictUltimateTicTacToe(board, defaultUltimateRuleBook)
    if game.winner() == PlayerType.X:
        return math.inf
    return 0

def OWinsUltimateGame(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    game = StrictUltimateTicTacToe(board, defaultUltimateRuleBook)
    if game.winner() == PlayerType.O:
        return -math.inf
    return 0

# ### 1 if the player has won the board, 0 otherwise
# def playerHasWonUltimateBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     game = StrictUltimateTicTacToe(board, defaultUltimateRuleBook)
#     print("winner: ", game.winner())
#     if game.winner() == player:
#         return 1
#     return 0

# ### 1 if the opponent has won the board, 0 otherwise
# def opponentHasWonUltimateBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     opponent = PlayerType.X if player == PlayerType.O else PlayerType.O
#     game = StrictUltimateTicTacToe(board, defaultUltimateRuleBook)
#     if game.winner() == opponent:
#         return 1
#     return 0


def XCanMoveOnAnyBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    unitBoard = ultimate_board_state_to_unit_games(board)[previousMove[1][0]][previousMove[1][1]]
    if unitBoard.is_game_over():
        return 1 if player == PlayerType.X else 0
    
def OCanMoveOnAnyBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    unitBoard = ultimate_board_state_to_unit_games(board)[previousMove[1][0]][previousMove[1][1]]
    if unitBoard.is_game_over():
        return 1 if player == PlayerType.O else 0


# ### 1 if the move sends the opponent to a board that is over, 0 otherwise
# def moveSendsOpponentToAnyBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     #get the unit board that the previous move sent the opponent to
#     unitBoard = ultimate_board_state_to_unit_games(board)[previousMove[1][0]][previousMove[1][1]]

#     #if that board is over, then this rule evaluates true.
#     if unitBoard.is_game_over():
#         return 1
#     return 0

# ### 0 if the move sends the opponent to a board that is over, 1 otherwise
# def moveDoesNotSendOpponentToAnyBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     if moveSendsOpponentToAnyBoard(board, previousMove, player):
#         return 0
#     return 1

def XUltimateTwoInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, '2X')

def OUltimateTwoInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, '2O')

# #counts unblocked ultimate two-in-a-rows for player
# def playerUltimateTwoInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     condition = '2X' if player == PlayerType.X else '2O'
#     return _check_num_in_ultimate_lines(board, condition)

# #counts unblocked ultimate two-in-a-rows for opponent
# def opponentUltimateTwoInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     condition = '2O' if player == PlayerType.X else '2X'
#     return _check_num_in_ultimate_lines(board, condition)

def XUltimateOneInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, '1X')

def OUltimateOneInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, '1O')

def XBlockingOWins(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, '1X2O')

def OBlockingXWins(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, '2X1O')

# #counts unblocked ultimate one-in-a-rows for player
# def playerUltimateOneInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     condition = '1X' if player == PlayerType.X else '1O'
#     return _check_num_in_ultimate_lines(board, condition)

# #counts unblocked ultimate one-in-a-rows for opponent
# def opponentUltimateOneInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     condition = '1O' if player == PlayerType.X else '1X'
#     return _check_num_in_ultimate_lines(board, condition)

# #counts how many times the player is blocking a 2-in-a-row for the opponent
# def blockedOpponentWins(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
#     condition = '1X2O' if player == PlayerType.X else '2X1O'
#     return _check_num_in_ultimate_lines(board, condition)
