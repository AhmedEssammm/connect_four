import time
import tkinter as tk
from board import COLUMNS, ROWS, create_board, EMPTY_SYMBOL, game_over, check_winner, check_draw, make_move
from ai_agent import AI_AGENT_SYMBOL, get_ai_agent_move
from computer import COMPUTER_SYMBOL, get_computer_move

# Create an empty game board
board = create_board(ROWS, COLUMNS)

# Create the GUI window
root = tk.Tk()
root.title("Connect Four")

# Function to update the GUI board
def update_board():
    for row in range(ROWS):
        for col in range(COLUMNS):
            symbol = board[row][col]
            button = buttons[row][col]
            if symbol == AI_AGENT_SYMBOL:
                button.config(text=symbol, bg='red')
            elif symbol == COMPUTER_SYMBOL:
                button.config(text=symbol, bg='blue')
            else:
                button.config(text=symbol, bg='white')

# Function to handle the game loop
def play_game():
    while not game_over(board):
        # AI agent's turn
        time.sleep(1)  # Delay for 1 second
        ai_agent_move = get_ai_agent_move(board)
        make_move(board, ai_agent_move, AI_AGENT_SYMBOL)
        update_board()
        root.update()  # Update the GUI

        if game_over(board):
            winner = check_winner(board)
            if winner == AI_AGENT_SYMBOL:
                winner_label.config(text="AI agent wins!")
            elif winner == COMPUTER_SYMBOL:
                winner_label.config(text="Computer wins!")
            else:
                winner_label.config(text="It's a draw!")
            restart_button.config(state=tk.NORMAL)
            break

        # Computer's turn
        time.sleep(1)  # Delay for 1 second
        computer_move = get_computer_move(board)
        make_move(board, computer_move, COMPUTER_SYMBOL)
        update_board()
        root.update()  # Update the GUI

        if game_over(board):
            winner = check_winner(board)
            if winner == AI_AGENT_SYMBOL:
                winner_label.config(text="AI agent wins!")
            elif winner == COMPUTER_SYMBOL:
                winner_label.config(text="Computer wins!")
            else:
                winner_label.config(text="It's a draw!")
            restart_button.config(state=tk.NORMAL)
            break

# Function to start the game
def start_game():
    start_button.config(state=tk.DISABLED)
    play_game()

# Function to restart the game
def restart_game():
    global board
    board = create_board(ROWS, COLUMNS)
    update_board()
    winner_label.config(text="")
    restart_button.config(state=tk.DISABLED)
    start_game()

# Create buttons for the game board
buttons = []
for row in range(ROWS):
    row_buttons = []
    for col in range(COLUMNS):
        button = tk.Button(root, text=EMPTY_SYMBOL, width=4, height=2, font=('Helvetica', 20, 'bold'), relief='groove', bg='white')
        button.grid(row=row, column=col, padx=2, pady=2)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Create the start button
start_button = tk.Button(root, text="Start", width=10, bg='green', command=start_game)
start_button.grid(row=ROWS, column=0, columnspan=COLUMNS, pady=10)

# Create the restart button
restart_button = tk.Button(root, text="Restart", width=10, bg='yellow', state=tk.DISABLED, command=restart_game)
restart_button.grid(row=ROWS + 1, column=0, columnspan=COLUMNS, pady=10)

# Create the winner label
winner_label = tk.Label(root, text="", font=('Helvetica', 16, 'bold'))
winner_label.grid(row=ROWS + 2, column=0, columnspan=COLUMNS, pady=10)

# Start the GUI event loop
root.mainloop()