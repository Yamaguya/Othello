from config import *
from board import Board

class Minimax:
    def __init__(self):
        # Predifined weights for the board positions, used for the heuristic evaluation
        self.weights = [[100, -30, 6, 2, 2, 6, -30, 100],
                        [-30, -50, 0, 0, 0, 0, -50, -30],
                        [  6,   0, 3, 3, 3, 3,   0,   6],
                        [  2,   0, 3, 2, 2, 3,   0,   2],
                        [  2,   0, 3, 2, 2, 3,   0,   2],
                        [  6,   0, 3, 4, 3, 3,   0,   6],
                        [-30, -50, 0, 0, 0, 0, -50, -30],
                        [100, -30, 6, 2, 2, 6, -30, 100]]
        
    # Minimax algorithm with alpha-beta pruning
    def minimax (self, board, depth, alpha, beta, maximizing_agent):
        # If the depth is 0 or the game is over, evaluate the board
        if depth == 0 or board.game_status:
            return self.evaluate_board(board)
        
        # Get the valid moves for the current color
        valid_moves = board.get_valid_moves(WHITE if maximizing_agent else BLACK)
        best_move = None

        if maximizing_agent:                                    # Computer's turn (maximizing agent)
            # Arbitrarily small initial value
            max_eval = -INF
            for moves in valid_moves.values():
                for move in moves:
                    # Simulate the move
                    new_board = self.simulate_move(board, move, WHITE)
                    # Recursively call minimax
                    eval = self.minimax(new_board, depth - 1, alpha, beta, False)
                    # Update the best evaluation score
                    if eval > max_eval:
                        max_eval = eval
                        best_move = move
                    # Alpha-beta pruning
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return best_move if depth == DEPTH else max_eval
        else:                                                   # Player's turn (minimizing agent)
            # Arbitrarily large initial value
            min_eval = INF
            best_move = None
            for moves in valid_moves.values():
                for move in moves:
                    # Simulate the move
                    new_board = self.simulate_move(board, move, BLACK)
                    # Recursively call minimax
                    eval = self.minimax(new_board, depth - 1, alpha, beta, True)
                    # Update the best evaluation score
                    if eval < min_eval:
                        min_eval = eval
                        best_move = move
                    # Alpha-beta pruning
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return best_move if depth == DEPTH else min_eval
        
    # Simulate a move by creating a new board and placing the piece
    def simulate_move(self, board, move, color):
        new_board = Board()
        new_board.board = [row[:] for row in board.board]
        new_board.place_piece(move, color)
        return new_board
    
    # Evaluate the board by calculating the score based on the predefined weights
    def evaluate_board(self, board):
        score = 0
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                if board.board[i][j] == WHITE:
                    score += self.weights[i][j]
                elif board.board[i][j] == BLACK:
                    score -= self.weights[i][j]
        return score