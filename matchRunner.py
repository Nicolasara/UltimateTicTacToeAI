from ultimateTicTacToe import UltimateTicTacToe
from player import TwoDimensionalMove

# play a game between two AI players and return the winner
def playAGame(playerX, playerO, print_game = False):
    # new board state 
    game = UltimateTicTacToe()
    while not game.is_gameOver():
        move = None
        match game.get_turn:
            # p1
            case 'X':
                move = playerX(game)
            # p2
            case 'O':
                move = playerO(game)
        game.make_move(move)
        if print_game:
            print(game.get_turn() + " moves: " + str(move) + "\n")
            print(game.toString())
    if print_game:
        print("Game over. Winner: " + game.winner + "\n")
    return game.winner

# play a game between an AI player and a manual player
def playAManualGame(AIplayerX):
    game = UltimateTicTacToe()
    while not game.is_gameOver():
        move = None
        match game.get_turn:
            # p1
            case 'X':
                move = AIplayerX(game)
            # p2
            case 'O':
                print("Enter your move: ")
                
                #expect entry to be: Y X y x
                input = input().split(" ")
                
                #convert move to TwoDimensionalMove
                move = TwoDimensionalMove(int(input[0]), int(input[1]), int(input[2]), int(input[3]))

                #check if move is valid
                while not game.is_valid_move(move):
                    print("Invalid move. Try again: ")
                    input = input().split(" ")
                    move = TwoDimensionalMove(int(input[0]), int(input[1]), int(input[2]), int(input[3]))

        game.make_move(move)
        print(game.get_turn() + " moves: " + str(move) + "\n")
        print(game.toString())
    print("Game over. Winner: " + game.winner + "\n")
    return game.winner

# play a set of games between two AI and return the number of wins for each player
def playManyGames(playerX, playerO, num_games):
    playerX_wins = 0
    playerO_wins = 0
    for i in range(num_games):
        winner = playAGame(playerX, playerO)
        if winner == 'X':
            playerX_wins += 1
        elif winner == 'O':
            playerO_wins += 1
    return (playerX_wins, playerO_wins)

#example of a player
player1 = lambda game: game.get_valid_moves()[0]

#play a game
playAManualGame(player1)

    