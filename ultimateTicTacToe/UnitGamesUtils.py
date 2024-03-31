from unitTicTacToe.unitTicTacToeBase import TicTacToe
from ultimateTicTacToe.ultimateTicTacToeTypes import UnitGames

def get_column(unitGames: UnitGames, column: int) -> list[TicTacToe]:
    return [unitGames[0][column], unitGames[1][column], unitGames[2][column]]

def get_row(unitGames: UnitGames, row: int) -> list[TicTacToe]:
    return unitGames[row]

def get_diagonal(unitGames: UnitGames, diagonal: int) -> list[TicTacToe]:
    """Gets the diagonal unitTicTacToe games of the ultimate board.

    Args:
        diagonal (int): The diagonal to get. 1 for the top-left to bottom-right diagonal, 2 for the top-right to bottom-left diagonal.

    Returns:
        list[TicTacToe]: The diagonal of unit games of the ultimate board.
    """
    if diagonal == 1:
        return [unitGames[0][0], unitGames[1][1], unitGames[2][2]]
    else:
        return [unitGames[0][2], unitGames[1][1], unitGames[2][0]]

def get_threes_in_a_row(unitGames: UnitGames) -> list[list[TicTacToe]]:
    column1 = get_column(unitGames, 0)
    column2 = get_column(unitGames, 1)
    column3 = get_column(unitGames, 2)
    row1 = get_row(unitGames, 0)
    row2 = get_row(unitGames, 1)
    row3 = get_row(unitGames, 2)
    diagonal1 = get_diagonal(unitGames, 1)
    diagonal2 = get_diagonal(unitGames, 2)

    return [
        column1, column2, column3,
        row1, row2, row3,
        diagonal1, diagonal2
    ]

def is_wining_three_in_a_row(games: list[TicTacToe]) -> bool:
    return games[0].winner() == games[1].winner() == games[2].winner() and games[0].winner() != None
