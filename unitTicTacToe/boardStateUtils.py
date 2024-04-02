from unitTicTacToe.unitTicTacToeTypes import CellState, BoardState

def get_column(board: BoardState, column: int) -> list[CellState]:
    return [board[0][column], board[1][column], board[2][column]]

def get_row(board: BoardState, row: int) -> list[CellState]:
    return board[row]

def get_diagonal(board: BoardState, diagonal: int) -> list[CellState]:
    """Gets the diagonal of the board.

    Args:
        diagonal (int): The diagonal to get. 1 for the top-left to bottom-right diagonal, 2 for the top-right to bottom-left diagonal.

    Returns:
        list[CellState]: The diagonal of the board.
    """
    if diagonal == 1:
        return [board[0][0], board[1][1], board[2][2]]
    else:
        return [board[0][2], board[1][1], board[2][0]]

def get_threes_in_a_row(board) -> list[list[CellState]]:
    column1 = get_column(board, 0)
    column2 = get_column(board, 1)
    column3 = get_column(board, 2)
    row1 = get_row(board, 0)
    row2 = get_row(board, 1)
    row3 = get_row(board, 2)
    diagonal1 = get_diagonal(board, 1)
    diagonal2 = get_diagonal(board, 2)

    return [
        column1, column2, column3,
        row1, row2, row3,
        diagonal1, diagonal2
    ]

def is_wining_three_in_a_row(cells: list[CellState]) -> bool:
    return cells[0] == cells[1] == cells[2] and cells[0] != CellState.EMPTY.value

def has_board_been_won(board: BoardState) -> bool:
    threesInARow = get_threes_in_a_row(board)
    for threeInARow in threesInARow:
        if is_wining_three_in_a_row(threeInARow):
            return True
    return False
