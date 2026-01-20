# tic_tac_toe.py

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = input(f"Player {current_player}, enter your move (row and column: 1 2): ").split()
            if len(move) != 2:
                print("Please enter two numbers separated by a space.")
                continue

            row, col = int(move[0]) - 1, int(move[1]) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("Cell already taken! Choose another one.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()

