import numpy as np
from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToeFactory, ultimate_board_state_to_unit_games
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove
from unitTicTacToe.unitTicTacToeTypes import BoardState, CellState, PlayerType


def _check_num_in_lines(board: BoardState, condition: str):
    sum_dict = {0:"empty", 1: "1X", 2: "2X", 3: "3X", 5:"1O", 6:"1X1O", 7:"2X1O", 10:"2O", 11:"1X2O", 15:"3O"}
    value_arr_func = np.vectorize(lambda e: e)
    value_arr = value_arr_func(board.get_board_copy())
    result = 0

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


#def three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
#    condition = "3" + player.value
#    simpleList = ultimate_board_state_to_unit_games(board)
#    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
#    total = np.matrix(total_func(simpleList))
#
#    return total.sum()

#def opp_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
#    condition = '3O' if player == PlayerType.X else '3X'
#    simpleList = ultimate_board_state_to_unit_games(board)
#    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
#    total = np.matrix(total_func(simpleList))

#    return total.sum()

def X_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '3X'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

def O_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '3O'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()
    
#def unblocked_two_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
#    condition = "2" + player.value
#    simpleList = ultimate_board_state_to_unit_games(board)
#    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
#    total = np.matrix(total_func(simpleList))
#
#    return total.sum()

def X_unblocked_two_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '2X'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

def O_unblocked_two_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '2O'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

#def block_opp_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    # fliping the player because our call to check_consecutive checks if the player passed in has 2 in a row
#    condition = '1X2O' if player == PlayerType.X else '2X1O'
#    simpleList = ultimate_board_state_to_unit_games(board)
#    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
#    total = np.matrix(total_func(simpleList))

#    return total.sum()

def X_block_O_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '1X2O'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

def O_block_X_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '2X1O'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

#def fork(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
#    condition = "2" + player.value
#    simpleList = ultimate_board_state_to_unit_games(board)
#    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
#    def check_fork(result):
#        return 1 if result >= 2 else 0
#    convert = np.vectorize(check_fork)
#    total = np.matrix(convert(total_func(simpleList)))
#
#    return total.sum()

def X_fork(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '2X'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    def check_fork(result):
        return 1 if result >= 2 else 0
    convert = np.vectorize(check_fork)
    total = np.matrix(convert(total_func(simpleList)))

    return total.sum()

def O_fork(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '2O'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    def check_fork(result):
        return 1 if result >= 2 else 0
    convert = np.vectorize(check_fork)
    total = np.matrix(convert(total_func(simpleList)))

    return total.sum()

#def unblocked_one_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
#    condition = "1" + player.value
#    simpleList = ultimate_board_state_to_unit_games(board)
#    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
#    total = np.matrix(total_func(simpleList))
#
#    return total.sum()

def X_unblocked_one_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '1X'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

def O_unblocked_one_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    condition = '1O'
    simpleList = ultimate_board_state_to_unit_games(board)
    total_func = np.vectorize(lambda e: _check_num_in_lines(e, condition))
    total = np.matrix(total_func(simpleList))

    return total.sum()

