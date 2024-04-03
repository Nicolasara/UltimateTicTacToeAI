from ultimateTicTacToe.ultimateTicTacToeBase import UltimateTicTacToe, UltimateTicTacToeFactory
from unitTicTacToe.unitTicTacToeTypes import PlayerType
from ultimateTicTacToe.ultimateTicTacToeTypes import UltimateMove
from player import Player
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# play a game between two AI players and return the winner
def playAGame(playerX: Player, playerO: Player, firstMove: UltimateMove = None, print_game = False, depth: int = 2):
    # new board state 
    game = UltimateTicTacToeFactory.emptyStrictGame()

    #make the first move if it is not None
    if firstMove != None:
        game.make_move(firstMove)
        if print_game:
            print("X moves: " + str(firstMove) + "\n")
            print(game.toString())

    while not game.is_game_over():
        move = None
        turn = game.get_turn()
        if turn == PlayerType.X:
            move = playerX.best_move(game, depth)
        else:
            move = playerO.best_move(game, depth)
        #assumes that the move is valid!
        #print('test')
        #print(game.possible_moves())
        #print(move)
        game.make_move(move)
        if print_game:
            print(turn.value + " moves: " + str(move) + "\n")
            print(game.toString())
    winner = game.winner().value if game.winner() != None else "Tie"
    if print_game:
        print("Game over. Winner: " + winner + "\n")
    print("First move: " + str(firstMove) + " Winner: " + winner)
    return winner

# play a game between an AI player and a manual player
def playAManualGame(AIplayerX: Player, depth: int):
    game = UltimateTicTacToeFactory.emptyStrictGame()
    while not game.is_game_over():
        move = None
        turn = game.get_turn()
        if turn == PlayerType.X:
            move = AIplayerX.best_move(game, depth)
        else:
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
    winner = game.winner().value if game.winner() != None else "Tie"
    print("Game over. Winner: " + winner + "\n")
    return winner

# play a set of games between two AI and return the number of wins for each player
def playManyGames(playerX: Player, playerO: Player, num_games, depth: int):
    playerX_wins = 0
    playerO_wins = 0
    for i in range(num_games):
        winner = playAGame(playerX, playerO)
        if winner == PlayerType.X:
            playerX_wins += 1
        elif winner == PlayerType.O:
            playerO_wins += 1
    return (playerX_wins, playerO_wins)

# play a set of 81 games starting with the 81 unique first moves possible.
def playAllFirstMoves(playerX: Player, playerO: Player, depth: int):
    playerX_wins = 0
    playerO_wins = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    firstMove = ((i, j), (k, l))
                    winner = playAGame(playerX, playerO, firstMove)
                    if winner == PlayerType.X:
                        playerX_wins += 1
                    elif winner == PlayerType.O:
                        playerO_wins += 1
    return (playerX_wins, playerO_wins)

def playAllFirstMovesAsync(playerX: Player, playerO: Player, depth: int):
    result_counts = {'X': 0, 'O': 0, "Tie": 0}

    # create a list of all possible first moves
    first_moves = [((a,b),(c,d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3)]

    # play all games asynchronously
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(lambda move: playAGame(playerX, playerO, move), first_moves)
    
    # count the results
    for result in results:
        result_counts[result] += 1
    
    return (result_counts['X'], result_counts['O'])
