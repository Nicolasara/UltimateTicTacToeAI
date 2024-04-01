from ultimateTicTacToe.ultimateTicTacToe import UltimateTicTacToe
import math


def minimax(game: UltimateTicTacToe, board_evaluator, depth: int, maximizing: bool, starting: bool):
    """
    :param UltimateTicTacToe game: the UltimateTicTacToe game instance
    :param int depth: how many moves ahead we want to calculate the heuristic for
    :param bool maximizing: whether or not it is the maximizing player's turn
    :param bool starting: whether or not this is the starting function call (i.e. not a recursive call), and if so,
                          we want to return the best move as well as the best heuristic value
    
    :return int The best heuristic value
    :return (int, TwoDimensionalMove) The best heuristic value and its associated move
    """
    
    if game.is_game_over() or depth == 0:
        return board_evaluator.evaluate(game.get_board_copy())
    
    # if we are the maximizing player
    if maximizing:
        best_value = -math.inf
        best_move = None

        for move in game.possible_moves():
            game_copy = UltimateTicTacToe(game.get_board_copy())
            game_copy.make_move(move)

            heuristic = max(minimax(game_copy, depth - 1, False, False))

            if heuristic > best_value:
                best_value = heuristic
                best_move = move
        
        if starting:
            return best_value, best_move
        
        return best_value
    
    # if we are the minimizing player
    else:
        best_value = math.inf
        best_move = None

        for move in game.possible_moves():
            game_copy = UltimateTicTacToe(game.get_board_copy())
            game_copy.make_move(move)

            heuristic = min(minimax(game_copy, depth - 1, True, False))

            if heuristic < best_value:
                best_value = heuristic
                best_move = move
        
        if starting:
            return best_value, best_move
        
        return best_value