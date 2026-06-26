
ROWS = 6
COLS = 7

board = [["." for _ in range(COLS)] for _ in range(ROWS)]


def show_board():
    for row in board:
        print(" ".join(row))
    print("1 2 3 4 5 6 7\n")


def place_piece(col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ".":
            board[row][col] = piece
            return True
    return False


def check_winner(piece):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != piece:
                continue

            for dr, dc in directions:
                count = 0

                for i in range(4):
                    nr = r + dr * i
                    nc = c + dc * i

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and board[nr][nc] == piece
                    ):
                        count += 1

                if count == 4:
                    return True

    return False


player = "X"

while True:
    show_board()

    try:
        col = int(input(f"Player {player}, choose column (1-7): ")) - 1

        if not (0 <= col < COLS):
            print("Invalid column!\n")
            continue

        if not place_piece(col, player):
            print("Column is full!\n")
            continue

        if check_winner(player):
            show_board()
            print(f"🎉 Player {player} Wins!")
            break

        player = "O" if player == "X" else "X"

    except ValueError:
        print("Enter a valid number!")
      