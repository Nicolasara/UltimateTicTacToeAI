from ultimateTicTacToe.ultimateTicTacToe import UltimateTicTacToeFactory, ultimate_board_state_to_unit_games
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove
from unitTicTacToe.unitTicTacToeTypes import BoardState, CellState, PlayerType


def _check_num_in_lines(board: BoardState, player: PlayerType, num: int, blocked: bool):
    result = 0
    opp = PlayerType.O
    if player == PlayerType.O:
        opp = PlayerType.X
    # check for horizontal consecutive
    for i in range(3):
        total_in_row = 0
        other_in_row = 0
        for j in range(3):
            print(board[i][j] == CellState.EMPTY)
            if board[i][j].value == player.value:
                total_in_row += 1
            elif blocked and board[i][j].value == opp.value:
                other_in_row += 1
            elif (not blocked) and board[i][j] == CellState.EMPTY:
                other_in_row += 1
        if (total_in_row == num and other_in_row == 3 - num):
            result += 1

    # check for vertical consecutive
    for i in range(3):
        total_in_col = 0
        other_in_col = 0
        for j in range(3):
            if board[j][i].value == player.value:
                total_in_col += 1
            elif blocked and board[j][i].value == opp.value:
                other_in_col += 1
            elif not blocked and board[j][i] == CellState.EMPTY:
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
            if board[j][j].value == player.value:
                total_in_diag_left += 1
            elif blocked and board[j][j].value == opp.value:
                other_in_diag_left += 1
            elif not blocked and board[j][j] == CellState.EMPTY:
                other_in_diag_left += 1
            if board[2-j][j].value == player.value:
                total_in_diag_right += 1
            elif blocked and board[2-j][j].value == opp.value:
                other_in_diag_right += 1
            elif not blocked and board[2-j][j] == CellState.EMPTY:
                other_in_diag_right += 1
                
        if ((total_in_diag_left == num and other_in_diag_left == 3 - num) 
            or (total_in_diag_right == num and other_in_diag_right == 3 - num)):
            result += 1
    return result

def three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    simpleList = ultimate_board_state_to_unit_games(board)
    total = 0
    for simpleGame in simpleList:
        total += _check_num_in_lines(simpleGame, player, 3, False)
    return total

def not_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    simpleList = ultimate_board_state_to_unit_games(board)
    total = 0
    for simpleGame in simpleList:
        simple_total = 0
        if player == PlayerType.X:
            simple_total += _check_num_in_lines(simpleGame, PlayerType.O, 3, False)
        else:
            simple_total += _check_num_in_lines(simpleGame, PlayerType.X, 3, False)
        total += simple_total
    return total
    
def unblocked_two_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    simpleList = ultimate_board_state_to_unit_games(board)
    total = 0
    for simpleRow in simpleList:
        for simpleGame in simpleRow:
            total += _check_num_in_lines(simpleGame.get_board_copy(), player, 2, False)
    return total

def block_opp_three_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    # fliping the player because our call to check_consecutive checks if the player passed in has 2 in a row
    simpleList = ultimate_board_state_to_unit_games(board)
    total = 0
    for simpleGame in simpleList:
        simple_total = 0
        if player == PlayerType.X:
            simple_total += _check_num_in_lines(simpleGame, PlayerType.O, 2, True)
        else: 
            simple_total += _check_num_in_lines(simpleGame, PlayerType.X, 2, True) 
        total += simple_total

def fork(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    simpleList = ultimate_board_state_to_unit_games(board)
    total = 0
    for simpleGame in simpleList:
        if unblocked_two_in_line(simpleGame, player) >= 2:
            total += 1
    return total

def unblocked_one_in_line(board: UltimateBoardState, _: UltimateMove, player: PlayerType):
    simpleList = ultimate_board_state_to_unit_games(board)
    total = 0
    for simpleGame in simpleList:
        total += _check_num_in_lines(simpleGame, player, 1, False)
    return total

strictUltimateTicTacToe = UltimateTicTacToeFactory.emptyStrictGame()
strictUltimateTicTacToe.make_move(((0, 0), (0, 0)))
strictUltimateTicTacToe.make_move(((0, 0), (1,0)))
strictUltimateTicTacToe.make_move(((1, 0), (1,0)))
strictUltimateTicTacToe.make_move(((1, 0), (0,0)))
strictUltimateTicTacToe.make_move(((0, 0), (0,1)))
print(unblocked_two_in_line(strictUltimateTicTacToe.get_board_copy(), ((0, 0), (0, 1)), PlayerType.X))