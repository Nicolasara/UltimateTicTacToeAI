import numpy as np
from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToe
from unitTicTacToe.unitTicTacToeBase import PlayerType

INFINITY = 1073741824

def _check_num_in_ultimate_lines(game: UltimateTicTacToe, condition: str):
    result = 0
    unit_games = game.unitGames
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

# ### 1 if the player has won the board, 0 otherwise
# def playerHasWonUltimateBoard(game: UltimateTicTacToe) -> int:
#     print("winner: ", game.winner())
#     if game.winner() == player:
#         return 1
#     return 0

# ### 1 if the opponent has won the board, 0 otherwise
# def opponentHasWonUltimateBoard(game: UltimateTicTacToe) -> int:
#     opponent = PlayerType.X if player == PlayerType.O else PlayerType.O
#     if game.winner() == opponent:
#         return 1
#     return 0


def XCanMoveOnAnyBoard(game: UltimateTicTacToe) -> int:
    previousMove = game.pastMove
    player = game.get_turn()
    unitBoard = game.unitGames[previousMove[1][0]][previousMove[1][1]]
    if unitBoard.is_game_over():
        return 1 if player == PlayerType.X else 0
    return 0
    
def OCanMoveOnAnyBoard(game: UltimateTicTacToe) -> int:
    previousMove = game.pastMove
    player = game.get_turn()
    unitBoard = game.unitGames[previousMove[1][0]][previousMove[1][1]]
    if unitBoard.is_game_over():
        return 1 if player == PlayerType.O else 0
    return 0


# ### 1 if the move sends the opponent to a board that is over, 0 otherwise
# def moveSendsOpponentToAnyBoard(game: UltimateTicTacToe) -> int:
#     #get the unit board that the previous move sent the opponent to
#     unitBoard = game.unitGames[previousMove[1][0]][previousMove[1][1]]

#     #if that board is over, then this rule evaluates true.
#     if unitBoard.is_game_over():
#         return 1
#     return 0

# ### 0 if the move sends the opponent to a board that is over, 1 otherwise
# def moveDoesNotSendOpponentToAnyBoard(game: UltimateTicTacToe) -> int:
#     if moveSendsOpponentToAnyBoard(board, previousMove, player):
#         return 0
#     return 1

def XUltimateTwoInARows(game: UltimateTicTacToe) -> int:
    return _check_num_in_ultimate_lines(game, '2X')

def OUltimateTwoInARows(game: UltimateTicTacToe) -> int:
    return _check_num_in_ultimate_lines(game, '2O')

# #counts unblocked ultimate two-in-a-rows for player
# def playerUltimateTwoInARows(game: UltimateTicTacToe) -> int:
#     condition = '2X' if player == PlayerType.X else '2O'
#     return _check_num_in_ultimate_lines(game, condition)

# #counts unblocked ultimate two-in-a-rows for opponent
# def opponentUltimateTwoInARows(game: UltimateTicTacToe) -> int:
#     condition = '2O' if player == PlayerType.X else '2X'
#     return _check_num_in_ultimate_lines(game, condition)

def XUltimateOneInARows(game: UltimateTicTacToe) -> int:
    return _check_num_in_ultimate_lines(game, '1X')

def OUltimateOneInARows(game: UltimateTicTacToe) -> int:
    return _check_num_in_ultimate_lines(game, '1O')

def XBlockingOWins(game: UltimateTicTacToe) -> int:
    return _check_num_in_ultimate_lines(game, '1X2O')

def OBlockingXWins(game: UltimateTicTacToe) -> int:
    return _check_num_in_ultimate_lines(game, '2X1O')

# #counts unblocked ultimate one-in-a-rows for player
# def playerUltimateOneInARows(game: UltimateTicTacToe) -> int:
#     condition = '1X' if player == PlayerType.X else '1O'
#     return _check_num_in_ultimate_lines(game, condition)

# #counts unblocked ultimate one-in-a-rows for opponent
# def opponentUltimateOneInARows(game: UltimateTicTacToe) -> int:
#     condition = '1O' if player == PlayerType.X else '1X'
#     return _check_num_in_ultimate_lines(game, condition)

# #counts how many times the player is blocking a 2-in-a-row for the opponent
# def blockedOpponentWins(game: UltimateTicTacToe) -> int:
#     condition = '1X2O' if player == PlayerType.X else '2X1O'
#     return _check_num_in_ultimate_lines(game, condition)
