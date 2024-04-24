import pygame
from config import *

class Board:
    
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.valid_moves = []

    def draw_board(self):
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.surface.fill((0, 100, 0, 128))
        WIN.blit(self.surface, (0,0))
        for row in range (1, ROWS):
            pygame.draw.line(WIN, BLACK, (0, row * SQUARE_SIZE), 
                             (WINDOW_WIDTH, row * SQUARE_SIZE), 2)
        
        for col in range (1, COLS):
            pygame.draw.line(WIN, BLACK, (col * SQUARE_SIZE, 0), 
                             (col * SQUARE_SIZE, WINDOW_HEIGHT), 2)
            
        for i in range (BOARD_WIDTH):
            for j in range (BOARD_HEIGHT):
                if self.board[i][j] != EMPTY:
                    pygame.draw.circle(WIN, self.board[i][j], 
                                       ((i * SQUARE_SIZE) + SQUARE_SIZE//2, 
                                        (j * SQUARE_SIZE) + SQUARE_SIZE // 2), 
                                        SQUARE_SIZE // 2.5)

    def get_valid_moves(self, color):
        if color == BLACK:
            opp = WHITE
        else:
            opp = BLACK
        self.valid_moves = []
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                if self.board[i][j] == color:
                    self.valid_moves.append(self.get_piece_moves(i, j, opp))
        return self.valid_moves

    def place_piece(self, pos, color):
        if pos == None:
            return
        print(pos)
        if pos in self.valid_moves:
            pygame.draw.circle(WIN, color, 
                               ((pos[0] * SQUARE_SIZE) + SQUARE_SIZE//2, 
                                (pos[1] * SQUARE_SIZE) + SQUARE_SIZE // 2), 
                                SQUARE_SIZE // 2.5)

    def get_piece_moves(self, row, col, opp):
        valid_squares = []

        # For each direction of the piece in this (row,col) check for possible moves
        for (dir_x, dir_y) in [
                (-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)
            ]:
                #print(row, col, dir_x, dir_y)
                pos = self.check_direction(row, col, dir_x, dir_y, opp)
                if pos:
                    valid_squares.append(pos) 
                    pygame.draw.circle(WIN, BLUE, 
                                       ((pos[0] * SQUARE_SIZE) + SQUARE_SIZE//2, 
                                        (pos[1] * SQUARE_SIZE) + SQUARE_SIZE // 2), 
                                        SQUARE_SIZE // 2.5)
                    #WIN.blit(self.surface, (pos[0]-SQUARE_SIZE, pos[1]-SQUARE_SIZE))
        return valid_squares
    
    def check_direction(self, row, col, dir_x, dir_y, opp):
        target_row = row + dir_y
        target_col = col + dir_x
        if (target_row >= 0 and target_col >=0 and target_row < BOARD_HEIGHT and 
            target_col < BOARD_WIDTH and self.board[target_row][target_col] == opp):
            target_row += dir_y
            target_col += dir_x
            while (target_row >= 0 and target_col >=0 and target_row < BOARD_HEIGHT and 
                   target_col < BOARD_WIDTH and self.board[target_row][target_col] == opp):
                target_row += dir_y
                target_col += dir_x
            if (target_row >= 0 and target_col >=0 and target_row < BOARD_HEIGHT and 
                target_col < BOARD_WIDTH and self.board[target_row][target_col] == EMPTY):
                return (target_row, target_col)
        
    def is_valid(self, pos, color):
        for lists in self.get_valid_moves(color):
            if (pos in lists):
                return True
        else:
            return False