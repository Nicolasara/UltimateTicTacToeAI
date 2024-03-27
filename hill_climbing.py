import random as rd
import math


def energy_function(weights, num_games: int):
    """
    Simulates a number of UltimateTicTacToe games and returns the win rate

    :param int[] weights: an array of integer weights to run the game with
    :param int num_games: number of UltimateTicTacToe games to run

    :return int The win rate
    """

    wins = 0

    for _ in range(num_games):
        # run games here using minimax algorithm
        pass

    return wins / num_games


def hill_climbing(initial_weights, num_iterations: int, num_games: int):
    """
    Our hill climbing algorithm to adjust the weights of game heuristics

    :param int[] initial_weights: an array of integer weights to start with
    :param int num_iterations: number of hill climbing iterations
    :param int num_games: number of UltimateTicTacToe games to run per hill climbing iteration

    :return (int[], int) The best found set of weights and its associated win rate
    """
    
    current_weights = initial_weights
    current_win_rate = 0
    
    for _ in range(num_iterations):
        adjusted_weights = [weight + rd.uniform(-1, 1) for weight in current_weights]
        win_rate = energy_function(adjusted_weights, num_games)

        if win_rate > current_win_rate:
            current_weights = adjusted_weights
            current_win_rate = win_rate

    best_solution = (current_weights, current_win_rate)
        
    return best_solution


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
