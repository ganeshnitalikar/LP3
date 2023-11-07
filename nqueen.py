def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at board[row][col]
    # Checking columns
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Checking upper-left diagonals
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checking upper-right diagonals
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    # Base case: if all queens are placed, return True
    if col >= n:
        return True

    # Placing the first queen in the specified column
    if col == 0:
        first_queen_col = int(input("Enter the column index (0-indexed) of the first queen: "))
        if first_queen_col < 0 or first_queen_col >= n:
            print("Invalid column index. Please enter a valid index.")
            return False

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                if solve_n_queens(board, col + 1, n):
                    return True
                board[row][col] = 0
        return False

    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

def main():
    n = int(input("Enter the value of N: "))

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print("N-Queens matrix:")
        print_board(board)
    else:
        print("No solution exists for the given configuration.")

if __name__ == "__main__":
    main()
