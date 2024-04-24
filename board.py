import pygame
from config import WHITE, BLACK, ROWS, COLS, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
    
    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range (COLS):
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    #def board_state()