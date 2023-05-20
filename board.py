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
    # Check rows
    for row in board:
        for col in range(COLUMNS - 3):
            if row[col] != EMPTY_SYMBOL and row[col] == row[col + 1] == row[col + 2] == row[col + 3]:
                return row[col]

    # Check columns
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][col] != EMPTY_SYMBOL and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return board[row][col]

    # Check diagonals (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] != EMPTY_SYMBOL and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return board[row][col]

    # Check diagonals (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] != EMPTY_SYMBOL and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return board[row][col]

    return None

# Check if the game is a draw
def check_draw(board):
    for row in board:
        if EMPTY_SYMBOL in row:
            return False
    return True

# Generate all possible moves
def generate_moves(board):
    moves = []
    for col in range(COLUMNS):
        if board[0][col] == EMPTY_SYMBOL:
            moves.append(col)
    return moves

# Make a move on the game board
def make_move(board, column, symbol):
    for row in range(ROWS - 1, -1, -1):  # Start from the bottom row and move up
        if board[row][column] == EMPTY_SYMBOL:
            board[row][column] = symbol
            break

# Undo a move on the game board
def undo_move(board, column):
    for row in range(ROWS):
        if board[row][column] != EMPTY_SYMBOL:
            board[row][column] = EMPTY_SYMBOL
            break

# Evaluate the current game state and assign a score
def evaluate_state(board):
    if check_winner(board) == AI_AGENT_SYMBOL:
        return 1
    elif check_winner(board) == COMPUTER_SYMBOL:
        return -1
    else:
        return 0
