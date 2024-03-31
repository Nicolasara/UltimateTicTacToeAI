from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToeFactory

strictUltimateTicTacToe = UltimateTicTacToeFactory.emptyStrictGame()

strictUltimateTicTacToe.make_move(((0, 0), (0, 0)))
assert len(strictUltimateTicTacToe.possible_moves()) == 8

