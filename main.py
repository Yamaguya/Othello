import pygame
from board import Board
from config import *

pygame.display.set_caption("Reversi")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board()
        board.get_valid_moves(BLACK)
        pygame.display.update()

    pygame.quit() # If loop breaks close game

main()