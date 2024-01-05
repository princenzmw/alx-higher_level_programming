#!/usr/bin/python3
import sys

"""_summary_ """


def is_safe(board, row, col, N):
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board, N):
    """_summary_

    Args:
        board (_type_): _description_
        N (_type_): _description_
    """
    for i in range(N):
        row_str = ""
        for j in range(N):
            if j == board[i]:
                row_str += "Q"
            else:
                row_str += "."
        print(row_str)
    print()


def solve_nqueens(board, row, N):
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        N (_type_): _description_
    """
    if row == N:
        print_solution(board, N)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def nqueens(N):
    """_summary_

    Args:
        N (_type_): _description_
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    """_summary_
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
