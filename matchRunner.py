from ultimateTicTacToe.ultimateTicTacToe import UltimateTicTacToe, UltimateTicTacToeFactory
from unitTicTacToe.unitTicTacToeTypes import PlayerType
from player import Player

# play a game between two AI players and return the winner
def playAGame(playerX: Player, playerO: Player, print_game = False):
    # new board state 
    game = UltimateTicTacToeFactory.emptyStrictGame()
    while not game.is_game_over():
        move = None
        turn = game.get_turn()
        match turn:
            # p1
            case PlayerType.X:
                move = playerX.best_move(game)
            # p2
            case PlayerType.O:
                move = playerO.best_move(game)
        #assumes that the move is valid!
        game.make_move(move)
        if print_game:
            print(turn.value + " moves: " + str(move) + "\n")
            print(game.toString())
    winner = game.winner() if game.winner() != None else "Tie"
    if print_game:
        print("Game over. Winner: " + winner.value + "\n")
    return winner

# play a game between an AI player and a manual player
def playAManualGame(AIplayerX: Player):
    game = UltimateTicTacToeFactory.emptyStrictGame()
    while not game.is_game_over():
        move = None
        turn = game.get_turn()
        match turn:
            # p1
            case PlayerType.X:
                move = AIplayerX.best_move(game)
            # p2
            case PlayerType.O:
                print("Enter your move: ")
                
                #expect entry to be: Y X y x
                move_input = input().split(" ")
                
                #convert move to two tuples
                move = ((int(move_input[0]), int(move_input[1])), (int(move_input[2]), int(move_input[3])))

                #check if move is valid
                while move not in game.possible_moves():
                    print("Invalid move. Try again: ")
                    move_input = input().split(" ")
                    move = ((int(move_input[0]), int(move_input[1])), (int(move_input[2]), int(move_input[3])))

        game.make_move(move)
        print(turn.value + " moves: " + str(move) + "\n")    
        print(game.toString())
    winner = game.winner() if game.winner() != None else "Tie"
    print("Game over. Winner: " + winner.value + "\n")
    return winner

# play a set of games between two AI and return the number of wins for each player
def playManyGames(playerX: Player, playerO: Player, num_games):
    playerX_wins = 0
    playerO_wins = 0
    for i in range(num_games):
        winner = playAGame(playerX, playerO)
        if winner == PlayerType.X:
            playerX_wins += 1
        elif winner == PlayerType.O:
            playerO_wins += 1
    return (playerX_wins, playerO_wins)

#example of a player // DEPRECATED
player1 = lambda game: game.possible_moves()[0]

#play a game
playAManualGame(player1)

    