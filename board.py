import random

# Constants
AI_AGENT_SYMBOL = 'AI'
COMPUTER_SYMBOL = 'C'
EMPTY_SYMBOL = ' '
ROWS = 6
COLUMNS = 7

# Create an empty game board
def create_board(rows, columns):
    return [[EMPTY_SYMBOL for _ in range(columns)] for _ in range(rows)]

# Check if the game is over
def game_over(board):
    return check_winner(board) or check_draw(board)

# Check if there is a winner
def check_winner(board):
    # ... Implementation ...

# Check if the game is a draw
def check_draw(board):
    # ... Implementation ...

# Generate all possible moves
def generate_moves(board):
    # ... Implementation ...

# Make a move on the game board
def make_move(board, column, symbol):
    # ... Implementation ...

# Undo a move on the game board
def undo_move(board, column):
    # ... Implementation ...

# Evaluate the current game state and assign a score
def evaluate_state(board):
    # ... Implementation ...