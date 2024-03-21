from ruleBook import defaultRuleBook, move_on_empty_cell, move_in_bounds, game_has_not_been_won
from simpleTicTacToe import TicTacToe, TurnLessTicTacToe, TicTacToeFactory
from examples import emptySimpleBoard, tiedSimpleBoard, wonSimpleBoard, ticTacToeBoard1

print("Testing Simple Tic Tac Toe")

## Factory Methods

turnLessGame = TicTacToeFactory.emptyTurnLessGame()
assert turnLessGame.get_board_copy() == emptySimpleBoard

print(" + Factory Methods passed") 

