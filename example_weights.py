'''

This file consists of example weights that are to be used for X's opponents during hill climbing.

Each set of weights defines a different "type" of player, as they are biased to make the player
want to make a certain type of move (e.g. always block X, always complete 3-in-a-rows, etc.)


INDEX TO HEURISTIC MAPPINGS:

0 = X can move on any ultimate board
1 = O can move on any ultimate board
2 = X has ultimate two in a row
3 = O has ultimate two in a row
4 = X has ultimate one in a row
5 = O has ultimate one in a row
6 = X blocks O's ultimate two in a row
7 = O blocks X's ultimate two in a row
8 = X has unit 3 in a row
9 = O has unit 3 in a row
10 = X has unblocked unit two in a row
11 = O has unblocked unit two in a row
12 = X blocks O's unit two in a row
13 = O blocks X's unit two in a row
14 = X has unit fork
15 = O has unit fork
16 = X has unblocked unit one in a row
17 = O has unblocked unit one in a row

'''

# all actions are equally biased
EQUAL_BIAS = [1 for _ in range(18)]

# player who biases blocking X
BLOCKING_BIAS = [0, 0, 20, 0, 10, 0, 0, -30, 10, 0, 5, 0, 0, -10, 0, 0, 2, 0]

# player who biases getting as many of their pieces in a row
ROW_BIAS = [0, -1, 0, -30, 0, -10, 0, 0, 0, -10, 0, -5, 0, 0, 0, 0, 0, -2]

# balanced player who will perform both blocking and row building when appropriate
BALANCED_BIAS = [5, -5, 30, -30, 10, -10, 10, -10, 10, -10, 5, -5, 5, -5, 2, -2, 1, -1]