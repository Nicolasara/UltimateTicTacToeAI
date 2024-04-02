import numpy as np
from unitTicTacToe.ruleBook import defaultRuleBook, move_on_empty_cell, move_in_bounds, game_has_not_been_won
from unitTicTacToe.unitTicTacToeBase import TicTacToe, TurnLessTicTacToe, TicTacToeFactory
from unitTicTacToe.unitTicTacToeTypes import BoardState, Move, CellState, PlayerType, Result
from examples import emptyUnitBoard, tiedUnitBoard, wonUnitBoard, ticTacToeBoard1

print("Testing Unit Tic Tac Toe Factory")

# Factory Methods

def unit_board_states_equal(board1: BoardState, board2: BoardState) -> bool:
    for r in range(3):
        for c in range(3):
            if board1[r][c] != board2[r][c]:
                return False
    return True

emptyTurnLessGame = TicTacToeFactory.empty_turn_less_game()
assert unit_board_states_equal(emptyTurnLessGame.get_board_copy(), emptyUnitBoard)

print(" + empty_turn_less_game() method passed") 


print("Testing Turn Less Tic Tac Toe")

# UnitTicTacToe

emptyTurnLessGame = TicTacToeFactory.empty_turn_less_game()

## show that get turn throws an exception
try:
    emptyTurnLessGame.get_turn()
    assert False
except Exception as e:
    assert str(e) == "This implementation does not have a turn."
print(" + get_turn() method passed")

## possible moves on empty game
def contains_subarray(arr_2d, specific_array):
    for sub_array in arr_2d:
        if np.array_equal(sub_array, specific_array):
            return True
    return False

possibleMoves = emptyTurnLessGame.possible_moves()
for i in range(3):
    for j in range(3):
        assert contains_subarray(possibleMoves, [i, j])
print(" + possible_moves() method passed on empty game")

## show that has_someone_won() method returns False on empty game
assert emptyTurnLessGame.has_someone_won() == False
print(" + has_someone_won() method passed on empty game")

## show that game is not over on empty game
assert emptyTurnLessGame.is_game_over() == False
print(" + is_game_over() method passed on empty game")

## show that winner is None on empty game
assert emptyTurnLessGame.winner() == None
print(" + winner() method passed on empty game")

## show that result is None on empty game
assert emptyTurnLessGame.result() == None
print(" + result() method passed on empty game")

## make move on empty game

emptyTurnLessGame.make_move((0, 0), PlayerType.X)
expectedBoardState = [
    [CellState.X.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value],
    [CellState.EMPTY.value, CellState.EMPTY.value, CellState.EMPTY.value]
]
assert unit_board_states_equal(emptyTurnLessGame.get_board_copy(), expectedBoardState)

print(" + make_move() method passed first initial move")

## possible moves updated after move
possibleMoves = emptyTurnLessGame.possible_moves()
expectedMoves = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
for expectedMove in expectedMoves:
    assert contains_subarray(possibleMoves, expectedMove)
print(" + possible_moves() method passed after first move")

## show that has_someone_won() method returns False after first move
assert emptyTurnLessGame.has_someone_won() == False
print(" + has_someone_won() method passed after first move")

## show that game is not over after first move
assert emptyTurnLessGame.is_game_over() == False
print(" + is_game_over() method passed after first move")

## show that winner is None after first move
assert emptyTurnLessGame.winner() == None
print(" + winner() method passed after first move")

## show that result is None after first move
assert emptyTurnLessGame.result() == None
print(" + result() method passed after first move")

## make moves until x wins
emptyTurnLessGame.make_move((0, 1), PlayerType.O)
emptyTurnLessGame.make_move((1, 0), PlayerType.X)
emptyTurnLessGame.make_move((1, 1), PlayerType.O)
emptyTurnLessGame.make_move((2, 0), PlayerType.X)
assert emptyTurnLessGame.has_someone_won() == True
assert emptyTurnLessGame.is_game_over() == True
assert emptyTurnLessGame.winner() == PlayerType.X
assert emptyTurnLessGame.result() == Result.X
assert len(emptyTurnLessGame.possible_moves()) == 0
print(" + make_move() method passed until x wins")
print(" + has_someone_won() method passed after x wins")
print(" + is_game_over() method passed after x wins")
print(" + winner() method passed after x wins")
print(" + result() method passed after x wins")
print(" + possible_moves() method passed after x wins")

## make moves until draw
emptyTurnLessGame = TicTacToeFactory.empty_turn_less_game()

emptyTurnLessGame.make_move((0, 0), PlayerType.X)
emptyTurnLessGame.make_move((0, 2), PlayerType.X)
emptyTurnLessGame.make_move((1, 1), PlayerType.X)
emptyTurnLessGame.make_move((2, 1), PlayerType.X)
emptyTurnLessGame.make_move((0, 1), PlayerType.O)
emptyTurnLessGame.make_move((1, 0), PlayerType.O)
emptyTurnLessGame.make_move((1, 2), PlayerType.O)
emptyTurnLessGame.make_move((2, 0), PlayerType.O)
emptyTurnLessGame.make_move((2, 2), PlayerType.O)
assert emptyTurnLessGame.has_someone_won() == False
assert emptyTurnLessGame.is_game_over() == True
assert emptyTurnLessGame.winner() == None
assert emptyTurnLessGame.result() == Result.DRAW
assert len(emptyTurnLessGame.possible_moves()) == 0
print(" + make_move() method passed until draw")
print(" + has_someone_won() method passed after draw")
print(" + is_game_over() method passed after draw")
print(" + winner() method passed after draw")
print(" + result() method passed after draw")
print(" + possible_moves() method passed after draw")

## make moves until o wins
emptyTurnLessGame = TicTacToeFactory.empty_turn_less_game()

emptyTurnLessGame.make_move((0, 0), CellState.O)
emptyTurnLessGame.make_move((1, 1), CellState.O)
emptyTurnLessGame.make_move((2, 1), CellState.O)
emptyTurnLessGame.make_move((0, 2), CellState.O)
emptyTurnLessGame.make_move((0, 1), CellState.O)
assert emptyTurnLessGame.has_someone_won() == True
assert emptyTurnLessGame.is_game_over() == True
assert emptyTurnLessGame.winner() == PlayerType.O
assert emptyTurnLessGame.result() == Result.O
assert len(emptyTurnLessGame.possible_moves()) == 0
print(" + make_move() method passed until o wins")
print(" + has_someone_won() method passed after o wins")
print(" + is_game_over() method passed after o wins")
print(" + winner() method passed after o wins")
print(" + result() method passed after o wins")
print(" + possible_moves() method passed after o wins")
