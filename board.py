import pygame
from config import WHITE, BLACK, GREEN, ROWS, COLS, SQUARE_SIZE, WIN, WINDOW_WIDTH, WINDOW_HEIGHT


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
        WIN.fill(GREEN)
        for row in range (1, ROWS):
            pygame.draw.line(WIN, BLACK, (0, row * SQUARE_SIZE), (WINDOW_WIDTH, row * SQUARE_SIZE), 2)
        
        for col in range (1, COLS):
            pygame.draw.line(WIN, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, WINDOW_HEIGHT), 2)
            
        self.place_piece((3,3), WHITE)
        self.place_piece((4,4), WHITE)
        self.place_piece((3,4), BLACK)
        self.place_piece((4,3), BLACK)

    def place_piece(self, pos, color):
        if pos == None:
            return
        pygame.draw.circle(WIN, color, ((pos[0] * SQUARE_SIZE) + SQUARE_SIZE//2, (pos[1] * SQUARE_SIZE) + SQUARE_SIZE // 2), SQUARE_SIZE // 2.5)