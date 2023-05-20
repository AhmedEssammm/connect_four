from board import game_over, make_move, undo_move, generate_moves, check_winner, check_draw
from computer import COMPUTER_SYMBOL

MAX_DEPTH = 6
AI_AGENT_SYMBOL = 'AI'

# Function to get the AI agent's move using the Minimax algorithm with Alpha-Beta Pruning


def get_ai_agent_move(board):
    best_score = float('-inf')
    best_move = None

    for move in generate_moves(board):
        make_move(board, move, AI_AGENT_SYMBOL)
        score = minimax(board, 0, False, float('-inf'), float('inf'))
        undo_move(board, move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

# Minimax algorithm with Alpha-Beta Pruning


def minimax(board, depth, is_maximizing_player, alpha, beta):
    if depth == MAX_DEPTH or game_over(board):
        return evaluate_state(board)

    if is_maximizing_player:
        max_score = float('-inf')

        for move in generate_moves(board):
            make_move(board, move, AI_AGENT_SYMBOL)
            score = minimax(board, depth + 1, False, alpha, beta)
            undo_move(board, move)

            max_score = max(max_score, score)
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break

        return max_score
    else:
        min_score = float('inf')

        for move in generate_moves(board):
            make_move(board, move, COMPUTER_SYMBOL)
            score = minimax(board, depth + 1, True, alpha, beta)
            undo_move(board, move)

            min_score = min(min_score, score)
            beta = min(beta, min_score)
            if beta <= alpha:
                break

        return min_score

# Function to evaluate the current state of the board and assign a score


def evaluate_state(board):
    if check_winner(board) == AI_AGENT_SYMBOL:
        return 1
    elif check_winner(board) == COMPUTER_SYMBOL:
        return -1
    else:
        return 0
