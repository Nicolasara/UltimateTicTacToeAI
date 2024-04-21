import numpy as np
from typing import Callable
from numpy.typing import NDArray
from numpy import int32

from ultimateTicTacToe.ultimateHeuristic import *
from unitTicTacToe.unitHeuristic import *
from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToe
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove
from unitTicTacToe.unitTicTacToeTypes import PlayerType

UltimateHeuristic = Callable[[UltimateTicTacToe], int]

class UltimateBoardEvaluator:
    def __init__(self, heuristics: list[UltimateHeuristic], weights: NDArray[np.float32], readableNames: list[str]):
        if len(heuristics) != len(weights) or len(weights) != len(readableNames):
            raise ValueError("The number of heuristics, weights, and readable names must be the same")
        
        self.heuristics = heuristics
        self.weights = weights
        self.readableNames = readableNames

    def get_weights(self):
        return self.weights
    
    def build_copy(self, weights: NDArray[np.float32]):
        return UltimateBoardEvaluator(self.heuristics, weights, self.readableNames)

    def evaluate(self, game: UltimateTicTacToe) -> int:
        heuristicCount = len(self.heuristics)
        scores = np.zeros(heuristicCount, dtype=int32)
        for i in range(heuristicCount):
            heuristic = self.heuristics[i]
            scores[i] = heuristic(game)
        return scores @ self.weights


class UltimateBoardEvaluatorBuilder:
    def __init__(self):
        self.heuristics = []
        self.weights = []
        self.readableNames = []
        
    def addHeuristic(self, heuristic: UltimateHeuristic, weight: np.float32, readableName: str):
        self.heuristics.append(heuristic)
        self.weights.append(weight)
        self.readableNames.append(readableName)

    def build(self) -> UltimateBoardEvaluator:
        return UltimateBoardEvaluator(self.heuristics, np.array(self.weights, dtype=np.float32), self.readableNames)

class UltimateBoardEvaluatorFactory:
    @staticmethod
    def firstEvaluator() -> UltimateBoardEvaluator:
        builder = UltimateBoardEvaluatorBuilder()
        builder.addHeuristic(XCanMoveOnAnyBoard, 0, "X can move on any ultimate board")
        builder.addHeuristic(OCanMoveOnAnyBoard, 0, "O can move on any ultimateboard")
        builder.addHeuristic(XUltimateTwoInARows, 0, "X ultimate two in a row")
        builder.addHeuristic(OUltimateTwoInARows, 0, "O ultimate two in a row")
        builder.addHeuristic(XUltimateOneInARows, 0, "X ultimate one in a row")
        builder.addHeuristic(OUltimateOneInARows, 0, "O ultimate one in a row")
        builder.addHeuristic(XBlockingOWins, 0, "X blocking O wins")
        builder.addHeuristic(OBlockingXWins, 0, "O blocking X wins")
        builder.addHeuristic(X_three_in_line, 0, "X three in line")
        builder.addHeuristic(O_three_in_line, 0, "O three in line")
        builder.addHeuristic(X_unblocked_two_in_line, 0, "X unblocked two in line in unit game")
        builder.addHeuristic(O_unblocked_two_in_line, 0, "O unblocked two in line in unit game")
        builder.addHeuristic(X_block_O_three_in_line, 0, "X block O three in line in unit game")
        builder.addHeuristic(O_block_X_three_in_line, 0, "O block X three in line in unit game")
        builder.addHeuristic(X_fork, 0, "X fork in unit game")
        builder.addHeuristic(O_fork, 0, "O fork in unit game")
        builder.addHeuristic(X_unblocked_one_in_line, 0, "X unblocked one in line in unit game")
        builder.addHeuristic(O_unblocked_one_in_line, 0, "O unblocked one in line in unit game")
        return builder.build()