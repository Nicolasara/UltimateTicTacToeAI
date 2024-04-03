from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToeFactory
import time

print("Testing Ultimate Tic Tac Toe")

# test how long this function takes
currentTime = time.time()
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                strictUltimateTicTacToe = UltimateTicTacToeFactory.emptyStrictGame()
                firstMoveDimension = (i, j)
                secondMoveDimension = (k, l)
                move = (firstMoveDimension, secondMoveDimension)
                strictUltimateTicTacToe.make_move(move)

                if firstMoveDimension == secondMoveDimension:
                    possibleMoveCount = 8
                else:
                    possibleMoveCount = 9

                assert len(strictUltimateTicTacToe.possible_moves()) == possibleMoveCount

# print how long this function took
timeAfter = time.time()
print("Function took: " + str(timeAfter - currentTime) + " seconds")

print(" + make move method passes for first move")
print(" + possible moves returns correct number of moves after first move")




