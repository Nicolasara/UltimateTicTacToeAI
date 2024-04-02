from ultimateTicTacToe.ultimateBoardEvaluator import UltimateBoardEvaluatorFactory
from examples import emptyUltimateTicTacToeBoard, ultimateTicTacToeBoard
from unitTicTacToe.unitTicTacToeTypes import PlayerType

# Test the UltimateBoardEvaluatorFactory

evaluator = UltimateBoardEvaluatorFactory.firstEvaluator()
# evaluation = evaluator.evaluate(emptyUltimateTicTacToeBoard, None, PlayerType.X)
evaluation = evaluator.evaluate(ultimateTicTacToeBoard, ((0, 0), (0, 0)), PlayerType.O)
print(evaluation)