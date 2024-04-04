from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToe, StrictUltimateTicTacToe
from ultimateTicTacToe.ultimateBoardEvaluator import UltimateBoardEvaluator
import math


def minimax(game: UltimateTicTacToe, board_evaluator: UltimateBoardEvaluator, depth: int, maximizing: bool, starting: bool = False, alpha=-math.inf, beta=math.inf):
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
        return board_evaluator.evaluate(game.get_board_copy(), game.get_last_move(), game.get_turn())
    
    # if we are the maximizing player
    if maximizing:
        possible_moves = game.possible_moves()
        best_value = -math.inf
        best_move = possible_moves[0]

        for move in possible_moves:
            game_copy = StrictUltimateTicTacToe(board = game.get_board_copy(), turn = game.get_turn())
            game_copy.make_move(move)

            move_value = minimax(game_copy, board_evaluator, depth - 1, False, False, alpha, beta)

            if move_value > best_value:
                best_value = move_value
                best_move = move

            if move_value > beta:
                break

            alpha = max(move_value, alpha)

        if starting:
            return best_value, best_move
        
        return best_value
    
    # if we are the minimizing player
    else:
        possible_moves = game.possible_moves()
        best_value = math.inf
        best_move = possible_moves[0]

        for move in possible_moves:
            game_copy = StrictUltimateTicTacToe(board = game.get_board_copy(), turn = game.get_turn())
            game_copy.make_move(move)

            move_value = minimax(game_copy, board_evaluator, depth - 1, True, False, alpha, beta)

            if move_value < best_value:
                best_value = move_value
                best_move = move

            if move_value < alpha:
                break

            beta = min(move_value, beta)
        
        if starting:
            return best_value, best_move
        
        return best_value