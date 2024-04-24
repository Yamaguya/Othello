import pygame
from board import Board
from config import *

pygame.display.set_caption("Reversi")

def valid_moves(board):
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            pass
            

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        valid_moves(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board()
        pygame.display.update()

    pygame.quit() # If loop breaks close game

main()