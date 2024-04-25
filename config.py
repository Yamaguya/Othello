import pygame

# CONSTANTS
WINDOW_WIDTH  = 640
WINDOW_HEIGHT = 640
FPS           = 30
BOARD_WIDTH   = 8
BOARD_HEIGHT  = 8
ROWS, COLS    = 8, 8
EMPTY         = 0
DEPTH         = 3
INF           = 10000
SQUARE_SIZE   = WINDOW_WIDTH // COLS

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# RGB
WHITE         = (255, 255, 255)
BLACK         = (0, 0, 0)
GREEN         = (0, 100, 0)
BLUE          = (0,191,255)