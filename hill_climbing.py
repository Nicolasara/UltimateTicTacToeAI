import random as rd
from player import Player
from matchRunner import playAllFirstMovesPool
import math
from ultimateTicTacToe.ultimateBoardEvaluator import UltimateBoardEvaluator, UltimateBoardEvaluatorFactory
from example_weights import EQUAL_BIAS, BLOCKING_BIAS, ROW_BIAS, BALANCED_BIAS
import numpy as np

BASE_EVALUATOR = UltimateBoardEvaluatorFactory.firstEvaluator()

def energy_function_adversarial(x_weights, o_weights, depth: int = 2, workers: int = 60):
    """
    Simulates 81 UltimateTicTacToe games between X and O and returns the total performance score for X
    """
    playerX = Player(BASE_EVALUATOR.build_copy(x_weights), maximizing=True)
    playerO = Player(BASE_EVALUATOR.build_copy(o_weights), maximizing=False)

    results = playAllFirstMovesPool(playerX, playerO, depth=depth, workers=workers)

    return results

def energy_function_archetypal(board_evaluator: UltimateBoardEvaluator, depth: int = 2, workers: int = 60):
    """
    Simulates 81 UltimateTicTacToe games per opponent and returns the total performance score for X
    """
    playerX = Player(board_evaluator, maximizing=True)

    player_O_baseline = Player(BASE_EVALUATOR, maximizing=False)
    player_O_equal_bias = Player(BASE_EVALUATOR.build_copy(EQUAL_BIAS), maximizing=False)
    player_O_block_bias = Player(BASE_EVALUATOR.build_copy(BLOCKING_BIAS), maximizing=False)
    player_O_row_bias = Player(BASE_EVALUATOR.build_copy(ROW_BIAS), maximizing=False)
    playerO_balanced = Player(BASE_EVALUATOR.build_copy(BALANCED_BIAS), maximizing=False)

    opponents = [player_O_baseline, player_O_equal_bias, player_O_block_bias, player_O_row_bias, playerO_balanced]
    total_results = [0, 0, 0]

    for i in range(len(opponents)):
        print("Opponent: " + str(i))
        results = playAllFirstMovesPool(playerX, opponents[i], depth=depth, workers=workers)
        total_results[0] += results[0]
        total_results[1] += results[1]
        total_results[2] += results[2]

    return total_results[0]


def hill_climbing_adversarial(initial_weights, num_iterations: int, depth: int = 2, workers: int = 60):
    """
    Adversarial hill climbing

    :param list initial_weights: an integer dictionary of weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int depth: minimax depth
    :param int workers: number of pool workers

    :return (list, list, int) The best weights for X, best for weights for O, and the best win rate
    """
    current_x_weights = initial_weights
    current_o_weights = initial_weights

    current_score = 34

    x_turn = True
    
    for i in range(num_iterations):
        print("Iteration: " + str(i))

        if x_turn:
            print("Adjusting Player X...")

            adjusted_weights = current_x_weights.copy()

            for i in range(len(adjusted_weights)):
                adjusted_weights[i] += rd.uniform(-10, 10)

            print("Adjusted Weights:")
            print(adjusted_weights)

            # get a win rate with all weights adjusted
            energy = energy_function_adversarial(adjusted_weights, current_o_weights, depth=depth, workers=workers)
            score = energy[0]

            if score > current_score:
                current_x_weights = adjusted_weights
                current_score = score
                x_turn = False
        else:
            print("Adjusting Player O...")

            adjusted_weights = current_o_weights.copy()

            for i in range(len(adjusted_weights)):
                adjusted_weights[i] += rd.uniform(-10, 10)

            print("Adjusted Weights:")
            print(adjusted_weights)

            # get a win rate with all weights adjusted
            energy = energy_function_adversarial(current_x_weights, adjusted_weights, depth=depth, workers=workers)
            score = energy[0]

            if score < current_score:
                current_o_weights = adjusted_weights
                current_score = score
                x_turn = True

        print("Current X Weights:")
        print(current_x_weights)
        print("Current O Weights:")
        print(current_o_weights)
        print("Current Score:")
        print(current_score)

    best_solution = (current_x_weights, current_o_weights, score)
        
    return best_solution

def hill_climbing_archetypal(initial_weights, initial_score: int, num_iterations: int, depth: int = 2, workers: int = 60):
    """
    Archetypal hill climbing

    :param list initial_weights: an integer dictionary of weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int depth: minimax depth
    :param int workers: number of pool workers

    :return (list, int) The best weights for X and the best win rate
    """
    
    current_weights = initial_weights
    current_score = initial_score
    
    for _ in range(num_iterations):
        print("Iteration: " + str(_))

        adjusted_weights = current_weights.copy()

        for i in range(len(adjusted_weights)):
            adjusted_weights[i] += rd.uniform(-10, 10)

        print("Adjusted Weights:")
        print(adjusted_weights)

        # get a win rate with all weights adjusted
        score = energy_function_archetypal(BASE_EVALUATOR.build_copy(adjusted_weights), depth=depth, workers=workers)

        if score > current_score:
            current_weights = adjusted_weights
            current_score = score

        print("Current Weights and Score:")
        print(current_weights)
        print(current_score)

    best_solution = (current_weights, current_score)
        
    return best_solution

'''

OLD UNUSED VERSIONS OF HILL_CLIMBING

def hill_climbing_per_weight(evaluator: UltimateBoardEvaluator, num_iterations: int, depth: int = 2, workers: int = 60):
    """
    Adjusts weights individually (while keeping all other weights constant) 
    """
    
    current_weights = evaluator.get_weights()
    current_win_rate = INITIAL_WINS[depth] / 81
    
    for _ in range(num_iterations):
        print("Iteration: " + str(_))

        d_weights = np.zeros(len(current_weights))
        directions = [-1, 1]

        # run 81 games for each weight in a random direction
        for i in range(len(current_weights)):
            print("Weight: " + str(i))

            direction = rd.choice(directions)
            weights_copy = current_weights.copy()
            weights_copy[i] += direction * rd.uniform(0, 10)

            d_win_rate = energy_function(evaluator.build_copy(weights_copy), depth=depth, workers=workers)

            if d_win_rate > current_win_rate:
                d_weights[i] = direction

        print("D_weights:")
        print(d_weights)

        adjusted_weights = current_weights.copy()

        # adjust all weights based on tests above
        for i in range(len(adjusted_weights)):
            adjusted_weights[i] += d_weights[i] * rd.uniform(0, 10)

        # get a win rate with all weights adjusted
        win_rate = energy_function(evaluator.build_copy(adjusted_weights), depth=depth, workers=workers)

        if win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate

        print("Current Weights and Win Rate:")
        print(current_weights)
        print(current_win_rate)

    best_solution = (current_weights, current_win_rate)
        
    return best_solution

def hill_climbing(evaluator: UltimateBoardEvaluator, num_iterations: int):
    """
    Our hill climbing algorithm to adjust the weights of game heuristics

    :param dict initial_weights: an integer dictionary of weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int num_games: number of UltimateTicTacToe games to run per hill climbing iteration

    :return (dict, int) The best found set of weights and its associated win rate
    """
    
    current_weights = evaluator.get_weights()
    current_win_rate = 0
    
    for _ in range(num_iterations):

        d_weights = np.zeros(len(current_weights))
        directions = [-1, 1]

        # run 81 games for each weight in each direction, recording best direction to move in
        for i in range(len(current_weights)):
            for direction in directions:
                weights_copy = current_weights.copy()
                weights_copy[i] += direction * rd.uniform(0, 1)
                # TODO - we're making a lot of evaluator copies here. Expensive?
                new_evaluator = evaluator.build_copy(weights_copy)

                d_win_rate = energy_function(new_evaluator)

                # if both negative and positive changes have a positive impact, we should check for better impact
                if d_win_rate > current_win_rate:
                    d_weights[i] = direction
                    break

        adjusted_weights = current_weights.copy()

        # adjust all weights based on tests above
        for i in range(len(adjusted_weights)):
            adjusted_weights[i] += d_weights[i] * rd.uniform(0, 1)

        # get a win rate with all weights adjusted
        win_rate = energy_function(evaluator.build_copy(adjusted_weights))

        # if 
        if win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate

    best_solution = (current_weights, current_win_rate)
        
    return best_solution

'''
