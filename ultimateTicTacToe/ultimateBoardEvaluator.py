from concurrent.futures import ThreadPoolExecutor
import numpy as np
from typing import Callable
from numpy.typing import NDArray
from numpy import int32

from ultimateTicTacToe.ultimateHeuristic import *
from unitTicTacToe.unitHeuristic import *
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove
from unitTicTacToe.unitTicTacToeTypes import PlayerType

UltimateHeuristic = Callable[[UltimateBoardState, UltimateMove, PlayerType], int]

class UltimateBoardEvaluator:
    def __init__(self, heuristics: list[UltimateHeuristic], weights: NDArray[np.float64], readableNames: list[str]):
        if len(heuristics) != len(weights) or len(weights) != len(readableNames):
            raise ValueError("The number of heuristics, weights, and readable names must be the same")
        
        self.heuristics = heuristics
        self.weights = weights
        self.readableNames = readableNames

    def evaluate(self, board: UltimateBoardState, move: UltimateMove, player: PlayerType) -> int:
        heuristicCount = len(self.heuristics)
        with ThreadPoolExecutor(max_workers=heuristicCount) as executor:
            scores = np.array(list(executor.map(lambda h: h(board, move, player), self.heuristics)))
            return scores @ self.weights
        

class UltimateBoardEvaluatorBuilder:
    def __init__(self):
        self.heuristics = []
        self.weights = []
        self.readableNames = []
        
    def addHeuristic(self, heuristic: UltimateHeuristic, weight: np.float64, readableName: str):
        self.heuristics.append(heuristic)
        self.weights.append(weight)
        self.readableNames.append(readableName)

    def get_weights(self):
        return self.weights
    
    def build_copy(self, weights: NDArray[np.float64]):
        return UltimateBoardEvaluator(self.heuristics, weights, self.readableNames)

    def build(self) -> UltimateBoardEvaluator:
        return UltimateBoardEvaluator(self.heuristics, np.array(self.weights, dtype=int32), self.readableNames)

class UltimateBoardEvaluatorFactory:
    @staticmethod
    ## TODO - add more heuristics from unitTicTacToe Heuristics
    def firstEvaluator() -> UltimateBoardEvaluator:
        builder = UltimateBoardEvaluatorBuilder()
        builder.addHeuristic(XWinsUltimateGame, 1, "X wins ultimate game")
        builder.addHeuristic(OWinsUltimateGame, 1, "O wins ultimate game")
        builder.addHeuristic(XCanMoveOnAnyBoard, 1, "X can move on any ultimate board")
        builder.addHeuristic(OCanMoveOnAnyBoard, 1, "O can move on any ultimateboard")
        builder.addHeuristic(XUltimateTwoInARows, 1, "X ultimate two in a row")
        builder.addHeuristic(OUltimateTwoInARows, 1, "O ultimate two in a row")
        builder.addHeuristic(XUltimateOneInARows, 1, "X ultimate one in a row")
        builder.addHeuristic(OUltimateOneInARows, 1, "O ultimate one in a row")
        builder.addHeuristic(XBlockingOWins, 1, "X blocking O wins")
        builder.addHeuristic(OBlockingXWins, 1, "O blocking X wins")
        builder.addHeuristic(X_three_in_line, 1, "X three in line")
        builder.addHeuristic(O_three_in_line, 1, "O three in line")
        builder.addHeuristic(X_unblocked_two_in_line, 1, "X unblocked two in line in unit game")
        builder.addHeuristic(O_unblocked_two_in_line, 1, "O unblocked two in line in unit game")
        builder.addHeuristic(X_block_O_three_in_line, 1, "X block O three in line in unit game")
        builder.addHeuristic(O_block_X_three_in_line, 1, "O block X three in line in unit game")
        builder.addHeuristic(X_fork, 1, "X fork in unit game")
        builder.addHeuristic(O_fork, 1, "O fork in unit game")
        builder.addHeuristic(X_unblocked_one_in_line, 1, "X unblocked one in line in unit game")
        builder.addHeuristic(O_unblocked_one_in_line, 1, "O unblocked one in line in unit game")
        return builder.build()