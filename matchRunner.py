def playAGame(player1, player2):
    # new board state 
    game = UltimateTicTacToe()
    while not game.is_gameOver():
        move = None
        match game.get_turn:
            # p1
            case 'X':
                move = player1(game)
            # p2
            case 'O':
                move = player2(game)
        game.make_move(move)
    return game.winner
