from unitTicTacToe.ruleBook import defaultRuleBook, move_on_empty_cell, move_in_bounds, game_has_not_been_won
from examples import emptyUnitBoard, tiedUnitBoard, wonUnitBoard, ticTacToeBoard1

### Rule Tests
print("Testing Rules")

## Move on Empty Cell

for i in range(3):
    for j in range(3):
        assert move_on_empty_cell(emptyUnitBoard, (i, j)) == True
        assert move_on_empty_cell(tiedUnitBoard, (i, j)) == False

print(" + move_on_empty_cell passed") 

## Move in Bounds

for i in range(3):
    for j in range(3):
        assert move_in_bounds(emptyUnitBoard, (i, j)) == True
        assert move_in_bounds(tiedUnitBoard, (i, j)) == True

for i in range(3, 6):
    for j in range(3):
        assert move_in_bounds(emptyUnitBoard, (i, j)) == False
        assert move_in_bounds(tiedUnitBoard, (i, j)) == False
        assert move_in_bounds(emptyUnitBoard, (j, i)) == False
        assert move_in_bounds(tiedUnitBoard, (j, i)) == False

for i in range(-3, 0):
    for j in range(3):
        assert move_in_bounds(emptyUnitBoard, (i, j)) == False
        assert move_in_bounds(tiedUnitBoard, (i, j)) == False
        assert move_in_bounds(emptyUnitBoard, (j, i)) == False
        assert move_in_bounds(tiedUnitBoard, (j, i)) == False

print(" + move_in_bounds passed")

## Game Has Not Been Won

for i in range(3):
    for j in range(3):
        assert game_has_not_been_won(emptyUnitBoard, (i, j)) == True
        assert game_has_not_been_won(tiedUnitBoard, (i, j)) == True
        assert game_has_not_been_won(wonUnitBoard, (i, j)) == False

print(" + game_has_not_been_won passed")

### RuleBook tests
print("Testing RuleBook")

## Default RuleBook

for i in range(3):
    for j in range(3):
        assert defaultRuleBook.is_valid(emptyUnitBoard, (i, j)) == True
        assert defaultRuleBook.is_valid(tiedUnitBoard, (i, j)) == False
        assert defaultRuleBook.is_valid(wonUnitBoard, (i, j)) == False

assert defaultRuleBook.is_valid(ticTacToeBoard1, (0, 0)) == False
assert defaultRuleBook.is_valid(ticTacToeBoard1, (0, 1)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (0, 2)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (1, 0)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (1, 1)) == False
assert defaultRuleBook.is_valid(ticTacToeBoard1, (1, 2)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (2, 0)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (2, 1)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (2, 2)) == True
assert defaultRuleBook.is_valid(ticTacToeBoard1, (2, 3)) == False

print(" + defaultRuleBook passed")

