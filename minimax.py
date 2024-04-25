from config import *
from board import Board

class Minimax:
    def __init__(self):
        self.weights = [[100, -30, 6, 2, 2, 6, -30, 100],
                        [-30, -50, 0, 0, 0, 0, -50, -30],
                        [  6,   0, 3, 3, 3, 3,   0,   6],
                        [  2,   0, 3, 2, 2, 3,   0,   2],
                        [  2,   0, 3, 2, 2, 3,   0,   2],
                        [  6,   0, 3, 4, 3, 3,   0,   6],
                        [-30, -50, 0, 0, 0, 0, -50, -30],
                        [100, -30, 6, 2, 2, 6, -30, 100]]
        self.valid_moves = {}
        self.pos = (3,3)
        self.new_board = Board()

    def minimax (self, board, position, maximizing_agent, depth, alpha, beta):
        self.valid_moves = board.get_valid_moves(WHITE)
        self.pos = position
        if depth == 0:
            print(position, ' Weight: ', self.weights[position[0]][position[1]])
            return self.pos
        if maximizing_agent:                               # Computer's turn
            max_eval = -INF                                # Arbitrarily small initial value
            for valid_move_list in self.valid_moves.values():
                for valid_move in valid_move_list:
                    self.new_board = board.evaluate_move(position, valid_move, WHITE)
                    cur_move = self.minimax(board, valid_move, False, depth-1, alpha, beta)
                    eval = self.weights[cur_move[0]][cur_move[1]]
                    max_eval = max(max_eval, eval)
                    if (eval > max_eval):
                        return cur_move
                    if (beta <= alpha):
                        break
            return self.pos
        else:                                              # Player's turn
            min_eval = INF                                 # Arbitrarily large initial value
            for valid_move_list in self.valid_moves.values():
                for valid_move in valid_move_list:
                    self.new_board = board.evaluate_move(position, valid_move, BLACK)
                    cur_move = self.minimax(board, valid_move, True, depth-1, alpha, beta)
                    eval = self.weights[cur_move[0]][cur_move[1]]
                    min_eval = min(min_eval, eval)
                    if (eval < min_eval):
                        return cur_move
                    if (beta <= alpha):
                        break
            return self.pos