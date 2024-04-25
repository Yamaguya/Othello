import pygame
from board import Board
from config import *

pygame.display.set_caption("Reversi")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.draw_board()
    turn = 0
    current_color = BLACK
    board.get_valid_moves(current_color)
    board.count_pieces()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                
                clicked_row = (mouse_x * BOARD_WIDTH) // WINDOW_WIDTH
                clicked_col = (mouse_y * BOARD_HEIGHT) // WINDOW_HEIGHT
                position = (clicked_row, clicked_col)
                
                if (board.is_valid(position, current_color)):
                    board.place_piece(position, current_color)  # Player places piece
                    # current_color = WHITE                     # Computer's turn
                    # minimax that returns position
                    # board.place_piece(position, current_color) # Computer places piece
                    current_color = BLACK                        # Player's turn, waiting for click
                    board.count_pieces()
                
        board.get_valid_moves(current_color)
        pygame.display.update()

    pygame.quit() # If loop breaks close game

main()