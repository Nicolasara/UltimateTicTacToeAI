from matchRunner import playAGame
from player import Player
from ultimateTicTacToe.ultimateBoardEvaluator import UltimateBoardEvaluatorFactory
from time import time

e = UltimateBoardEvaluatorFactory.firstEvaluator()

playerX = Player(e, True)
playerO = Player(e, False)

currentTime = time()
playAGame(playerX, playerO, None, False, 2)
print("Time: " + str(time() - currentTime))