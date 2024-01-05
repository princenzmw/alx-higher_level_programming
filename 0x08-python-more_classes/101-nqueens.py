#!/usr/bin/python3
import sys

""" Queen of N chess """


def is_safe(board, row, col, N):
    """
    Check if placing a queen in the given row and column is safe.

    Args:
        board (list): Current state of the chessboard.
        row (int): Row index.
        col (int): Column index.
        N (int): Size of the chessboard.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board, N):
    """
    Print the current solution of the N Queens problem.

    Args:
        board (list): Current state of the chessboard.
        N (int): Size of the chessboard.
    """
    solution = []
    for i in range(N):
        solution.append([i, board[i]])
    print(solution)


def solve_nqueens(board, row, N):
    """
    Recursively solve the N Queens problem.

    Args:
        board (list): Current state of the chessboard.
        row (int): Current row being considered.
        N (int): Size of the chessboard.
    """
    if row == N:
        print_solution(board, N)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def nqueens(N):
    """
    Main function to solve the N Queens problem.

    Args:
        N (str): Size of the chessboard.

    Raises:
        ValueError: If N is not a valid integer.
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
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
