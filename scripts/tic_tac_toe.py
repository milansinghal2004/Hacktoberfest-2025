# --- Constants ---
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# --- Print the whole Ultimate Tic-Tac-Toe board ---
def print_board(boards):
    print("    0   1   2       0   1   2       0   1   2")
    print("  +---+---+---+   +---+---+---+   +---+---+---+")

    for big_row in range(3):
        for small_row in range(3):
            print(f"{big_row * 3 + small_row} |", end="")
            for big_col in range(3):
                for small_col in range(3):
                    print(f" {boards[big_row][big_col][small_row][small_col]} |", end="")
                print("   |", end="")
            print()
            print("  +---+---+---+   +---+---+---+   +---+---+---+")


# --- Check win on a single 3x3 board ---
def check_win(board, player):
    # Rows & cols
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    # Diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False


# --- Check if a 3x3 board is full ---
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def main():
    # A 4D list: [big_row][big_col][small_row][small_col]
    game_boards = [[[[EMPTY for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]

    # Big board state (who won each small board)
    big_board_state = [[EMPTY for _ in range(3)] for _ in range(3)]

    current_player = PLAYER_X
    big_row, big_col = -1, -1
    game_over = False
    winner = EMPTY

    print("Welcome to Ultimate Tic-Tac-Toe!")
    print("Player X goes first.")

    while not game_over:
        print_board(game_boards)
        print(f"Player {current_player}'s turn.")

        if big_row != -1 and big_board_state[big_row][big_col] == EMPTY:
            print(f"You must play on the board at ({big_row}, {big_col}).")
        else:
            print("You can play on any available board.")
            big_row, big_col = -1, -1

        valid_move = False
        while not valid_move:
            try:
                board_row, board_col, row, col = map(int, input(
                    "Enter your move (big_row big_col small_row small_col): "
                ).split())
            except ValueError:
                print("Invalid input. Enter 4 integers separated by space.")
                continue

            # Check boundaries
            if not (0 <= board_row <= 2 and 0 <= board_col <= 2 and 0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid coordinates. Please try again.")
                continue

            # Correct board check
            if big_row != -1 and (board_row != big_row or board_col != big_col):
                print("Invalid move. You must play on the designated board.")
                continue

            # Already won board
            if big_board_state[board_row][board_col] != EMPTY:
                print("This board is already won. Choose a different one.")
                if big_row != -1:
                    big_row, big_col = -1, -1
                continue

            # Spot taken
            if game_boards[board_row][board_col][row][col] != EMPTY:
                print("This spot is already taken. Try again.")
                continue

            # Valid move
            valid_move = True
            game_boards[board_row][board_col][row][col] = current_player
            big_row, big_col = row, col

        # Small board win/draw
        if check_win(game_boards[board_row][board_col], current_player):
            big_board_state[board_row][board_col] = current_player
        elif is_board_full(game_boards[board_row][board_col]):
            big_board_state[board_row][board_col] = 'D'

        # Big board win
        if check_win(big_board_state, current_player):
            winner = current_player
            game_over = True

        # Big board draw
        if is_board_full(big_board_state) and not game_over:
            game_over = True

        # Switch player
        if not game_over:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    print_board(game_boards)
    if winner != EMPTY:
        print(f"Congratulations, Player {winner} wins the game!")
    else:
        print("The game is a draw!")


if __name__ == "__main__":
    main()
