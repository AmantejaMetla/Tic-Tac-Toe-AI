# Tic-Tac-Toe with AI and GUI

## Introduction
This project is a Python-based Tic-Tac-Toe game that includes:
- A Graphical User Interface (GUI) built with **Tkinter**.
- An AI opponent that uses varying difficulty levels (Easy, Medium, Hard).
- A modular structure with distinct files for board management, game logic, and GUI, making it extensible and easy to maintain.

## Project Structure
The project is organized into three main files:

### 1. `game_board.py`
Handles board creation, display, and move validation.
- **Purpose**: To keep all board-related functionalities in one place, ensuring reusability and separation of concerns.
- **Key Functions**:
  - `create_board(size=3)`: Creates an empty board.
  - `show_board(board, theme)`: Displays the current state of the board.
  - `is_valid_move(board, row, col)`: Validates whether a move is possible.
  - `make_move(board, row, col, player)`: Executes a move if valid.

### 2. `game_logic.py`
Implements the game's core logic, including AI decision-making and win/tie checks.
- **Purpose**: To encapsulate game rules and AI strategies, making it adaptable for different interfaces.
- **Key Functions**:
  - `check_winner(board, player)`: Checks if a player has won.
  - `is_tie(board)`: Determines if the game is a tie.
  - `evaluate_board(board)`: Evaluates the board for the Minimax algorithm.
  - AI Functions:
    - `random_ai_turn(board)`: Makes a random move (Easy difficulty).
    - `medium_ai_turn(board)`: Blocks winning moves or plays randomly (Medium difficulty).
    - `ai_turn(board)`: Uses the Minimax algorithm to choose the best move (Hard difficulty).

### 3. `tic_tac_toe_gui.py`
Provides a graphical interface for the game, integrating player interaction and AI functionality.
- **Purpose**: To offer an intuitive and engaging user experience.
- **Key Features**:
  - A grid-based layout for the board using buttons.
  - Menu options for selecting difficulty and customizing themes.
  - Interactive game flow that alternates between the player and AI.
  - Automatic resetting after a game ends.

## How the Files Work Together
1. **Game Initialization**:
   - The GUI (`tic_tac_toe_gui.py`) initializes the board using `create_board` from `game_board.py`.
2. **Player Interaction**:
   - The player clicks a button on the GUI to make a move.
   - The move is validated using `is_valid_move` and executed via `make_move` from `game_board.py`.
3. **AI Interaction**:
   - After the player’s move, the AI logic from `game_logic.py` is invoked based on the selected difficulty.
   - AI updates the board directly, and the GUI reflects the changes.
4. **Game Status**:
   - `check_winner` and `is_tie` from `game_logic.py` determine if the game ends in a win, loss, or tie.
   - Results are displayed in a popup, and the game resets automatically.

## Why This Structure Was Chosen
### Modularity
- Each file focuses on a specific aspect of the game, ensuring clarity and ease of maintenance.
- This separation allows independent updates to AI logic, board functions, or the GUI without affecting the other components.

### Scalability
- The modular approach makes it easy to add features like:
  - Dynamic board sizes.
  - Advanced AI strategies.
  - Additional themes or visual effects.

### User Experience
- The GUI provides an interactive and visually appealing interface.
- Features like difficulty settings and themes enhance engagement.

### Code Reusability
- Core logic in `game_logic.py` can be reused for other interfaces, such as a command-line or web-based version.

## How to Run the Project
1. Ensure you have Python installed (3.6 or higher recommended).
2. Save the following files in the same directory:
   - `game_board.py`
   - `game_logic.py`
   - `tic_tac_toe_gui.py`
3. Run the GUI file:
   ```bash
   python tic_tac_toe_gui.py
   ```
4. Use the menu options to select difficulty and customize themes.
5. Play against the AI by clicking on the grid.

## Future Improvements
1. **Dynamic Board Sizes**:
   - Allow users to choose different board sizes (e.g., 4x4 or 5x5).
   - Update AI logic to handle larger boards.

2. **Multiplayer Mode**:
   - Enable two-player local or online gameplay.

3. **Enhanced Visuals**:
   - Add animations for moves and results.
   - Improve themes with custom icons or images.

4. **AI Enhancements**:
   - Implement advanced algorithms like Monte Carlo Tree Search (MCTS).

5. **Mobile Compatibility**:
   - Use libraries like Kivy to make the game mobile-friendly.

---

Thank you for exploring this Tic-Tac-Toe project and Thank you CodSoft for giving me the oporturnity and motivation to achieve this!!

