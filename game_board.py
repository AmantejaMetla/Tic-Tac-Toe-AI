# game_board.py

def create_board(size=3):
    """Create a Tic-Tac-Toe board with the given size."""
    return [[" " for _ in range(size)] for _ in range(size)]

def show_board(board, theme=("X", "O")):
    """Display the current state of the board using the specified theme."""
    size = len(board)
    print("\n")
    for row in board:
        print(" | ".join(cell if cell == " " else theme[0] if cell == "X" else theme[1] for cell in row))
        print("-" * (size * 2 - 1))
    print("\n")

def is_valid_move(board, row, col):
    """Check if a move is valid."""
    return 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == " "

def make_move(board, row, col, player):
    """Make a move for the given player if valid."""
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

