import random as rd
from player import Player
from matchRunner import playAllFirstMovesPool
import math
from ultimateTicTacToe.ultimateBoardEvaluator import UltimateBoardEvaluator
import numpy as np

# Pre-calculated number of wins for X, given depth
INITIAL_WINS = {1: 9, 2: 29}

def energy_function(board_evaluator: UltimateBoardEvaluator, depth: int = 2, workers: int = 60):
    """
    Simulates 81 UltimateTicTacToe games and returns the win rate for X
    """

    playerX = Player(board_evaluator, maximizing=True)
    playerO = Player(board_evaluator, maximizing=False)

    results = playAllFirstMovesPool(playerX, playerO, depth=depth, workers=workers)

    return results[0] / 81

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

def hill_climbing_all_weights(evaluator: UltimateBoardEvaluator, num_iterations: int, depth: int = 2, workers: int = 60):
    """
    Adjusts all weights randomly at once
    """
    
    current_weights = evaluator.get_weights()
    current_win_rate = INITIAL_WINS[depth] / 81
    
    for _ in range(num_iterations):
        print("Iteration: " + str(_))

        adjusted_weights = current_weights.copy()

        # adjust all weights based on tests above
        for i in range(len(adjusted_weights)):
            adjusted_weights[i] += rd.uniform(-10, 10)

        # get a win rate with all weights adjusted
        win_rate = energy_function(evaluator.build_copy(adjusted_weights), depth=depth, workers=workers)

        if win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate

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








"""

OLD IMPLEMENTATIONS, IGNORE FOR NOW

"""

def hill_climbing_adaptive(initial_weights, num_iterations: int, num_games: int):
    """
    The same as the hill climbing function above, but now we dynamically adjust
    how significantly the weights change per iteration

    :param int[] initial_weights: an array of integer weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int num_games: number of UltimateTicTacToe games to run per hill climbing iteration

    :return (int[], int) The best found set of weights and its associated win rate
    """
    
    current_weights = initial_weights
    current_win_rate = 0
    learning_rate = 1
    
    for _ in range(num_iterations):
        adjusted_weights = [weight + learning_rate * rd.uniform(-1, 1) for weight in current_weights]
        win_rate = energy_function(adjusted_weights, num_games)

        if win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate
            learning_rate *= 1.1
        else:
            learning_rate *= 0.9

    best_solution = (current_weights, current_win_rate)
        
    return best_solution


def hill_climbing_random_uphill(initial_weights, num_iterations: int, num_games: int, probability: float):
    """
    Hill climbing with a random probability of keeping a worse weight change

    :param int[] initial_weights: an array of integer weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int num_games: number of UltimateTicTacToe games to run per hill climbing iteration
    :param float probability: probability of keeping worse weight change

    :return (int[], int) The best found set of weights and its associated win rate
    """

    current_weights = initial_weights
    current_win_rate = 0
    best_weights = current_weights
    best_win_rate = current_win_rate

    for _ in range(num_iterations):
        adjusted_weights = [weight + rd.uniform(-1, 1) for weight in current_weights]
        win_rate = energy_function(adjusted_weights, num_games)

        if win_rate > best_win_rate:
            best_weights = adjusted_weights
            best_win_rate = win_rate
            current_weights = adjusted_weights
            current_win_rate = win_rate
        elif win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate
        elif rd.random() < probability:
            current_weights = adjusted_weights
            current_win_rate = win_rate

    best_solution = (best_weights, best_win_rate)

    return best_solution


def hill_climbing_annealing(initial_weights, num_iterations: int, num_games: int, T: float, decay: float):
    """
    Hill climbing utilizing simulated annealing

    :param int[] initial_weights: an array of integer weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int num_games: number of UltimateTicTacToe games to run per hill climbing iteration
    :param float T: initial temperature
    :param float decay: decay rate to decrease temperature per iteration

    :return (int[], int) The best found set of weights and its associated win rate
    """

    current_weights = initial_weights
    current_win_rate = 0
    best_weights = current_weights
    best_win_rate = current_win_rate
    curr_T = T

    for _ in range(num_iterations):
        adjusted_weights = [weight + rd.uniform(-1, 1) for weight in current_weights]
        win_rate = energy_function(adjusted_weights, num_games)

        if win_rate > best_win_rate:
            best_weights = adjusted_weights
            best_win_rate = win_rate
            current_weights = adjusted_weights
            current_win_rate = win_rate
        elif win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate
        elif rd.random() < (math.e)**((win_rate - current_win_rate)/curr_T):
            current_weights = adjusted_weights
            current_win_rate = win_rate

        curr_T *= decay

    best_solution = (best_weights, best_win_rate)

    return best_solution
