# main_game.py

from game_board import create_board, show_board, make_move
from game_logic import check_winner, is_tie, random_ai_turn, medium_ai_turn, ai_turn

def choose_difficulty():
    """Let the user choose the difficulty level."""
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in {"1", "2", "3"}:
            return int(choice)
        print("Invalid choice. Try again.")

def choose_theme():
    """Let the user choose a theme."""
    print("Choose a theme:")
    print("1. Classic (X, O)")
    print("2. Emoji (😊, 🤖)")
    print("3. Custom symbols")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            return ("X", "O")
        elif choice == "2":
            return ("😊", "🤖")
        elif choice == "3":
            x = input("Enter symbol for Player 1: ")
            o = input("Enter symbol for AI: ")
            return (x, o)
        print("Invalid choice. Try again.")

def human_turn(board):
    """Let the human player make a move."""
    while True:
        try:
            move = input("Enter your move as row,col (e.g., 1,2): ")
            row, col = map(int, move.split(","))
            if make_move(board, row - 1, col - 1, "X"):
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input format. Use row,col (e.g., 1,2).")

def main_game():
    """Run the main game loop."""
    print("Welcome to Tic-Tac-Toe!")
    board_size = int(input("Enter board size (e.g., 3 for 3x3): "))
    board = create_board(board_size)
    difficulty = choose_difficulty()
    theme = choose_theme()
    show_board(board, theme)

    while True:
        # Human turn
        print("Your turn:")
        human_turn(board)
        show_board(board, theme)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_tie(board):
            print("It's a tie!")
            break

        # AI turn
        print("AI's turn:")
        if difficulty == 1:
            random_ai_turn(board)
        elif difficulty == 2:
            medium_ai_turn(board)
        else:
            ai_turn(board)
        show_board(board, theme)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        if is_tie(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main_game()
