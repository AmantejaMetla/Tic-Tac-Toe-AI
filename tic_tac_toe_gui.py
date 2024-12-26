import tkinter as tk
from tkinter import messagebox
from game_logic import check_winner, random_ai_turn, medium_ai_turn, ai_turn, is_tie

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board_size = 3
        self.board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.difficulty = 3  # Default to hard
        self.theme = ("X", "O")
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        self.create_menu()
        self.create_board()

    def create_menu(self):
        """Create the menu bar for difficulty and theme settings."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Set Difficulty", command=self.set_difficulty)
        settings_menu.add_command(label="Set Theme", command=self.set_theme)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)

    def create_board(self):
        """Create the game board as a grid of buttons."""
        for row in range(self.board_size):
            for col in range(self.board_size):
                btn = tk.Button(self.root, text="", font=("Arial", 24), height=2, width=5,
                                command=lambda r=row, c=col: self.player_move(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

    def set_difficulty(self):
        """Allow the player to choose a difficulty level."""
        def apply_difficulty():
            level = difficulty_var.get()
            if level:
                self.difficulty = int(level)
                messagebox.showinfo("Difficulty Set", f"Difficulty set to {'Easy' if level == '1' else 'Medium' if level == '2' else 'Hard'}")
                difficulty_window.destroy()

        difficulty_window = tk.Toplevel(self.root)
        difficulty_window.title("Set Difficulty")
        difficulty_var = tk.StringVar(value=str(self.difficulty))
        tk.Radiobutton(difficulty_window, text="Easy", variable=difficulty_var, value="1").pack(anchor="w")
        tk.Radiobutton(difficulty_window, text="Medium", variable=difficulty_var, value="2").pack(anchor="w")
        tk.Radiobutton(difficulty_window, text="Hard", variable=difficulty_var, value="3").pack(anchor="w")
        tk.Button(difficulty_window, text="Apply", command=apply_difficulty).pack()

    def set_theme(self):
        """Allow the player to choose a theme."""
        def apply_theme():
            x_symbol = x_var.get()
            o_symbol = o_var.get()
            if x_symbol and o_symbol:
                self.theme = (x_symbol, o_symbol)
                messagebox.showinfo("Theme Set", f"Theme set to Player: {x_symbol}, AI: {o_symbol}")
                theme_window.destroy()

        theme_window = tk.Toplevel(self.root)
        theme_window.title("Set Theme")
        x_var = tk.StringVar(value=self.theme[0])
        o_var = tk.StringVar(value=self.theme[1])
        tk.Label(theme_window, text="Player Symbol (X):").pack(anchor="w")
        tk.Entry(theme_window, textvariable=x_var).pack()
        tk.Label(theme_window, text="AI Symbol (O):").pack(anchor="w")
        tk.Entry(theme_window, textvariable=o_var).pack()
        tk.Button(theme_window, text="Apply", command=apply_theme).pack()

    def player_move(self, row, col):
        """Handle the player's move."""
        if self.board[row][col] == " ":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text=self.theme[0], state="disabled")
            if self.check_game_over("X"):
                return
            self.ai_move()

    def ai_move(self):
        """Handle the AI's move."""
        if self.difficulty == 1:
            random_ai_turn(self.board)
        elif self.difficulty == 2:
            medium_ai_turn(self.board)
        else:
            ai_turn(self.board)

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == "O":
                    self.buttons[row][col].config(text=self.theme[1], state="disabled")
        self.check_game_over("O")

    def check_game_over(self, player):
        """Check if the game is over."""
        if check_winner(self.board, player):
            winner = "You" if player == "X" else "AI"
            messagebox.showinfo("Game Over", f"{winner} win!")
            self.reset_game()
            return True
        if is_tie(self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        """Reset the game board."""
        self.board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
