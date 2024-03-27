from ultimateTicTacToe.ultimateTicTacToe import StrictUltimateTicTacToe, ultimate_board_state_to_unit_games
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateMove, UltimateBoardState
from unitTicTacToe.unitTicTacToe import PlayerType
from ultimateTicTacToe.ultimateRuleBook import defaultUltimateRuleBook

def _check_num_in_ultimate_lines(board: UltimateBoardState, player: PlayerType, num: int, blocked: bool):
    result = 0
    opp = PlayerType.O
    if player == PlayerType.O:
        opp = PlayerType.X
    unit_games = ultimate_board_state_to_unit_games(board)

    # check for horizontal consecutive
    for i in range(3):
        total_in_row = 0
        other_in_row = 0
        for j in range(3):
            if unit_games[i][j].winner() == player:
                total_in_row += 1
            elif blocked and unit_games[i][j].winner() == opp:
                other_in_row += 1
            elif not blocked and unit_games[i][j].winner() == None:
                other_in_row += 1
        if (total_in_row == num and other_in_row == 3 - num):
            result += 1

    # check for vertical consecutive
    for i in range(3):
        total_in_col = 0
        other_in_col = 0
        for j in range(3):
            if unit_games[j][i].winner() == player:
                total_in_col += 1
            elif blocked and unit_games[j][i].winner() == opp:
                other_in_col += 1
            elif not blocked and unit_games[j][i].winner() == None:
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
            if unit_games[j][j].winner() == player:
                total_in_diag_left += 1
            elif blocked and unit_games[j][j].winner() == opp:
                other_in_diag_left += 1
            elif not blocked and unit_games[j][j].winner() == None:
                other_in_diag_left += 1
            if unit_games[2-j][j].winner() == player:
                total_in_diag_right += 1
            elif blocked and unit_games[2-j][j].winner() == opp:
                other_in_diag_right += 1
            elif not blocked and unit_games[2-j][j].winner() == None:
                other_in_diag_right += 1

        if ((total_in_diag_left == num and other_in_diag_left == 3 - num) 
            or (total_in_diag_right == num and other_in_diag_right == 3 - num)):
            result += 1
    return result

### 1 if the player has won the board, 0 otherwise
def playerHasWonUltimateBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    game = StrictUltimateTicTacToe(board, defaultUltimateRuleBook)
    print("winner: ", game.winner())
    if game.winner() == player:
        return 1
    return 0

### 1 if the opponent has won the board, 0 otherwise
def opponentHasWonUltimateBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    opponent = PlayerType.X if player == PlayerType.O else PlayerType.O
    game = StrictUltimateTicTacToe(board, defaultUltimateRuleBook)
    if game.winner() == opponent:
        return 1
    return 0

### 1 if the move sends the opponent to a board that is over, 0 otherwise
def moveSendsOpponentToAnyBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    #get the unit board that the previous move sent the opponent to
    unitBoard = ultimate_board_state_to_unit_games(board)[previousMove[1][0]][previousMove[1][1]]

    #if that board is over, then this rule evaluates true.
    if unitBoard.is_game_over():
        return 1
    return 0

### 0 if the move sends the opponent to a board that is over, 1 otherwise
def moveDoesNotSendOpponentToAnyBoard(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    if moveSendsOpponentToAnyBoard(board, previousMove, player):
        return 0
    return 1

#counts unblocked ultimate two-in-a-rows for player
def playerUltimateTwoInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, player, 2, False)

#counts unblocked ultimate two-in-a-rows for opponent
def opponentUltimateTwoInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    opp = PlayerType.O if player == PlayerType.X else PlayerType.X
    return _check_num_in_ultimate_lines(board, opp, 2, False)

#counts unblocked ultimate one-in-a-rows for player
def playerUltimateOneInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    return _check_num_in_ultimate_lines(board, player, 1, False)

#counts unblocked ultimate one-in-a-rows for opponent
def opponentUltimateOneInARows(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    opp = PlayerType.O if player == PlayerType.X else PlayerType.X
    return _check_num_in_ultimate_lines(board, opp, 1, False)

#counts how many times the player is blocking a 2-in-a-row for the opponent
def blockedOpponentWins(board: UltimateBoardState, previousMove: UltimateMove, player: PlayerType) -> int:
    opp = PlayerType.O if player == PlayerType.X else PlayerType.X
    return _check_num_in_ultimate_lines(board, opp, 2, True)
