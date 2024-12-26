# game_logic.py

import random
from game_board import is_valid_move, make_move

def check_winner(board, player):
    """Check if the given player has won."""
    size = len(board)
    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(size)) or all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False

def is_tie(board):
    """Check if the game is a tie."""
    return all(board[row][col] != " " for row in range(len(board)) for col in range(len(board)))

def evaluate_board(board):
    """Evaluate the board for the AI's Minimax algorithm."""
    if check_winner(board, "O"):
        return 10
    elif check_winner(board, "X"):
        return -10
    return 0

def minimax(board, is_ai_turn):
    """Implement the Minimax algorithm for the AI."""
    score = evaluate_board(board)
    if score != 0 or is_tie(board):
        return score

    if is_ai_turn:
        best_score = float("-inf")
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    best_score = max(best_score, minimax(board, False))
                    board[row][col] = " "
        return best_score
    else:
        best_score = float("inf")
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    best_score = min(best_score, minimax(board, True))
                    board[row][col] = " "
        return best_score

def random_ai_turn(board):
    """AI plays a random move."""
    available_moves = [(row, col) for row in range(len(board)) for col in range(len(board)) if board[row][col] == " "]
    if available_moves:
        move = random.choice(available_moves)
        board[move[0]][move[1]] = "O"

def medium_ai_turn(board):
    """AI plays a medium-difficulty move."""
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == " ":
                board[row][col] = "X"  # Simulate opponent's move
                if check_winner(board, "X"):
                    board[row][col] = "O"  # Block the win
                    return
                board[row][col] = " "  # Undo move
    # If no immediate threat, play randomly
    random_ai_turn(board)

def ai_turn(board):
    """AI plays the best move using Minimax."""
    best_move = None
    best_score = float("-inf")

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == " ":
                board[row][col] = "O"
                move_score = minimax(board, False)
                board[row][col] = " "
                if move_score > best_score:
                    best_score = move_score
                    best_move = (row, col)

    if best_move:
        board[best_move[0]][best_move[1]] = "O"
