import pygame
from board import Board
from config import *
from minimax import Minimax

pygame.init()

pygame.display.set_caption("Reversi")

# Create a font object for displaying text
score_font = pygame.font.SysFont(None, 36)

def render_score_text(board):
    # Render text surfaces for white and black pieces count
    white_score_text = score_font.render(f"White: {board.white_pieces}", True, WHITE)
    black_score_text = score_font.render(f"Black: {board.black_pieces}", True, BLACK)
    
    return white_score_text, black_score_text

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    evaluator = Minimax()
    board.draw_board()
    current_color = BLACK
    board.get_valid_moves(current_color)
    board.count_pieces()
    # Render score text surfaces
    white_score_text, black_score_text = render_score_text(board)
    
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

                if board.is_valid(position, current_color):

                    board.place_piece(position, current_color)      # Player places piece
                    board.draw_board()

                    pygame.display.update()                         # Update the display to show player's move
                    
                    pygame.time.delay(1000)                         # Delay to simulate the move animation

                    current_color = WHITE                           # Computer's turn
                    
                    computer_move = evaluator.minimax(board, DEPTH, -INF, INF, True)

                    board.place_piece(computer_move, current_color) # Computer places piece
                    board.draw_board()

                    current_color = BLACK                           # Player's turn, waiting for click
                    board.count_pieces()
        
                    if board.game_over():                           # Check if game is over
                        break
                    
                    board.get_valid_moves(current_color)            # Get valid moves for the player
            white_score_text, black_score_text = render_score_text(board)
            
            WIN.blit(white_score_text, (20, 20))                    # Blit score text onto the main surface
            WIN.blit(black_score_text, (WINDOW_WIDTH - 120, 20))
            
        pygame.display.update() 

    pygame.quit()                                                   # If loop breaks close game

main()