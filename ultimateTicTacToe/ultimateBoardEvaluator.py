from concurrent.futures import ThreadPoolExecutor
import numpy as np
from typing import Callable
from numpy.typing import NDArray
from numpy import int32

from ultimateTicTacToe.ultimateHeuristic import blockedOpponentWins, moveDoesNotSendOpponentToAnyBoard, moveSendsOpponentToAnyBoard, opponentHasWonUltimateBoard, opponentUltimateOneInARows, opponentUltimateTwoInARows, playerHasWonUltimateBoard, playerUltimateOneInARows, playerUltimateTwoInARows
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateBoardState, UltimateMove
from unitTicTacToe.unitTicTacToeTypes import PlayerType

UltimateHeuristic = Callable[[UltimateBoardState, UltimateMove, PlayerType], int]

class UltimateBoardEvaluator:
    def __init__(self, heuristics: list[UltimateHeuristic], weights: NDArray[int32], readableNames: list[str]):
        if len(heuristics) != len(weights) or len(weights) != len(readableNames):
            raise ValueError("The number of heuristics, weights, and readable names must be the same")
        
        self.heuristics = heuristics
        self.weights = weights
        print(weights)
        self.readableNames = readableNames

    def evaluate(self, board: UltimateBoardState, move: UltimateMove, player: PlayerType) -> int:
        # heuristicCount = len(self.heuristics)
        # with ThreadPoolExecutor(max_workers=heuristicCount) as executor:
        #     scores = np.array(executor.map(lambda h: h(board, move, player), self.heuristics))
        scores = np.array([h(board, move, player) for h in self.heuristics])
        print("Scores: ", scores)
        return scores @ self.weights
        

class UltimateBoardEvaluatorBuilder:
    def __init__(self):
        self.heuristics = []
        self.weights = []
        self.readableNames = []
        
    def addHeuristic(self, heuristic: UltimateHeuristic, weight: int, readableName: str):
        self.heuristics.append(heuristic)
        self.weights.append(weight)
        self.readableNames.append(readableName)
        
    def build(self) -> UltimateBoardEvaluator:
        return UltimateBoardEvaluator(self.heuristics, np.array(self.weights, dtype=int32), self.readableNames)

class UltimateBoardEvaluatorFactory:
    @staticmethod
    def firstEvaluator() -> UltimateBoardEvaluator:
        builder = UltimateBoardEvaluatorBuilder()
        builder.addHeuristic(playerHasWonUltimateBoard, 1, "player has won ultimate board")
        builder.addHeuristic(opponentHasWonUltimateBoard, 1, "opponentHasWon ultimate board")
        builder.addHeuristic(moveSendsOpponentToAnyBoard, 1, "move sends opponent to any board")
        builder.addHeuristic(moveDoesNotSendOpponentToAnyBoard, 1, "move does not send opponent to any board")
        builder.addHeuristic(playerUltimateTwoInARows, 1, "player ultimate two in a rows")
        builder.addHeuristic(opponentUltimateTwoInARows, 1, "opponent ultimate two in a rows")
        builder.addHeuristic(playerUltimateOneInARows, 1, "player ultimate one in a rows")
        builder.addHeuristic(opponentUltimateOneInARows, 1, "opponent ultimate one in a rows")
        builder.addHeuristic(blockedOpponentWins, 1, "blocked opponent wins")
        return builder.build()