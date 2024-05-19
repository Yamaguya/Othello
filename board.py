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
        self.dict_of_valid_moves = {}
        self.white_pieces = 0
        self.black_pieces = 0
        self.game_status = False
        self.valid_moves_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.valid_moves_surface.fill((0, 0, 0, 0))  # Fill with fully transparent initially
        pygame.init()

    def draw_board(self):
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.surface.fill((12, 100, 12, 255))
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
                    pygame.draw.circle(WIN, self.board[i][j], ((i * SQUARE_SIZE) + SQUARE_SIZE//2, (j * SQUARE_SIZE) + SQUARE_SIZE // 2), SQUARE_SIZE // 2.5)

    def get_valid_moves(self, color):
        self.dict_of_valid_moves = {}
        number_of_moves = 0
        if color == BLACK:
            opp = WHITE
        else:
            opp = BLACK

        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                if self.board[i][j] == color:
                    piece_moves = self.get_piece_moves(i, j, opp)
                    piece_pos = (i, j)
                    self.dict_of_valid_moves[piece_pos] = piece_moves
                    if (piece_moves != []):
                        number_of_moves += 1
                    
        if (number_of_moves == 0):
            self.game_status = True
        return self.dict_of_valid_moves

    def place_piece(self, pos, color):
        if pos == None:
            return
        for lists in self.dict_of_valid_moves.values():
            if pos in lists:
                pygame.draw.circle(WIN, color, ((pos[0] * SQUARE_SIZE) + SQUARE_SIZE//2, (pos[1] * SQUARE_SIZE) + SQUARE_SIZE // 2), SQUARE_SIZE // 2.5)
                self.board[pos[0]][pos[1]] = color
                for key, value in self.dict_of_valid_moves.items():
                    for val in value:
                        if (val == pos): 
                            self.flip_pieces(key, pos, color)
                            self.count_pieces()

    def evaluate_move(self, start_pos, end_pos, color): # Possible computer move evaluation
        captured_pieces = []
        row_start = start_pos[1]
        row_end = end_pos[1]
        col_start = start_pos[0]
        col_end = end_pos[0]
        if (row_start < row_end):
            if (col_start < col_end):
                while (row_start < row_end and row_start < BOARD_HEIGHT-1 and col_start < BOARD_WIDTH-1): # Move diagonally down left
                    row_start += 1
                    col_start += 1
                    captured_pieces.append(self.board[col_start][row_start])
            elif (col_start > col_end):
                while (row_start < row_end and row_start < BOARD_HEIGHT-1): # Move diagonally down left
                    row_start += 1
                    col_start -= 1
                    captured_pieces.append(self.board[col_start][row_start])
            else:
                while (row_start < row_end and row_start < BOARD_HEIGHT-1): # Move down
                    row_start += 1
                    captured_pieces.append(self.board[col_start][row_start])
        elif (row_start > row_end):
            if (col_start < col_end):
                while (row_start > row_end and row_start > 0 and col_start < BOARD_WIDTH-1): # Move diagonally up right
                    row_start -= 1
                    col_start += 1
                    captured_pieces.append(self.board[col_start][row_start])
            elif (col_start > col_end):
                while (row_start > row_end and row_start > 0 and col_start > 0): # Move diagonally up left
                    row_start -= 1
                    col_start -= 1
                    captured_pieces.append(self.board[col_start][row_start])
            else:
                while (row_start > row_end and row_start > 0):                        # Move up
                    row_start -= 1
                    captured_pieces.append(self.board[col_start][row_start])
        else:
            if (col_start < col_end):
                while (col_start < col_end and col_start < BOARD_WIDTH):                        # Move right
                    col_start += 1
                    captured_pieces.append(self.board[col_start][row_start])
            elif (col_start > col_end):
                while (col_start > col_end and col_start > 0):                        # Move left
                    col_start -= 1
                    captured_pieces.append(self.board[col_start][row_start])
        return captured_pieces

    def flip_pieces(self, start_pos, end_pos, color):
        row_start = start_pos[1]
        row_end = end_pos[1]
        col_start = start_pos[0]
        col_end = end_pos[0]
        if (row_start < row_end):
            if (col_start < col_end):
                while (row_start < row_end):                        # Move diagonally down left
                    row_start += 1
                    col_start += 1
                    self.board[col_start][row_start] = color
            elif (col_start > col_end):
                while (row_start < row_end):                        # Move diagonally down left
                    row_start += 1
                    col_start -= 1
                    self.board[col_start][row_start] = color
            else:
                while (row_start < row_end):                        # Move down
                    row_start += 1
                    self.board[col_start][row_start] = color
        elif (row_start > row_end):
            if (col_start < col_end):
                while (row_start > row_end):                        # Move diagonally up right
                    row_start -= 1
                    col_start += 1
                    self.board[col_start][row_start] = color
            elif (col_start > col_end):
                while (row_start > row_end):                        # Move diagonally up left
                    row_start -= 1
                    col_start -= 1
                    self.board[col_start][row_start] = color
            else:
                while (row_start > row_end):                        # Move up
                    row_start -= 1
                    self.board[col_start][row_start] = color
        else:
            if (col_start < col_end):
                while (col_start < col_end):                        # Move right
                    col_start += 1
                    self.board[col_start][row_start] = color
            elif (col_start > col_end):
                while (col_start > col_end):                        # Move left
                    col_start -= 1
                    self.board[col_start][row_start] = color
        
    def get_piece_moves(self, row, col, opp):
        # Clear the valid moves surface
        self.valid_moves_surface.fill((0, 0, 0, 0))

        valid_squares = []
        for (dir_x, dir_y) in [
                (-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)
            ]:
                # print(row, col, dir_x, dir_y)
                pos = self.check_direction(row, col, dir_x, dir_y, opp)
                if pos:
                    valid_squares.append(pos) 
                    semi_transparent_blue = (0, 191, 255, 85)
                    pygame.draw.circle(self.valid_moves_surface, semi_transparent_blue, ((pos[0] * SQUARE_SIZE) + SQUARE_SIZE//2, (pos[1] * SQUARE_SIZE) + SQUARE_SIZE // 2), SQUARE_SIZE // 2.5)
        WIN.blit(self.valid_moves_surface, (0, 0))
        return valid_squares
    
    # Follow through direction checking for adjacent opponent's pieces to be flipped
    def check_direction(self, row, col, dir_x, dir_y, opp):
        target_row = row + dir_y
        target_col = col + dir_x
        if (target_row >= 0 and target_col >=0 and target_row < BOARD_HEIGHT and target_col < BOARD_WIDTH and self.board[target_row][target_col] == opp):
            target_row += dir_y
            target_col += dir_x
            while (target_row >= 0 and target_col >=0 and target_row < BOARD_HEIGHT and target_col < BOARD_WIDTH and self.board[target_row][target_col] == opp):
                target_row += dir_y
                target_col += dir_x
            if (target_row >= 0 and target_col >=0 and target_row < BOARD_HEIGHT and target_col < BOARD_WIDTH and self.board[target_row][target_col] == EMPTY):
                return (target_row, target_col)
        
    # Check if clicked move is valid
    def is_valid(self, pos, color):
        for lists in self.dict_of_valid_moves.values():
            if (pos in lists):
                return True
        return False
        
    def count_pieces(self):
        self.white_pieces = 0
        self.black_pieces = 0
        for i in range (BOARD_WIDTH):
            for j in range (BOARD_HEIGHT):
                if (self.board[i][j] == WHITE):
                    self.white_pieces += 1
                elif (self.board[i][j] == BLACK):
                    self.black_pieces += 1
        print("WHITE :", self.white_pieces, " - BLACK: ", self.black_pieces)
        if (self.white_pieces == 0): print("Black wins!")
        if (self.black_pieces == 0): print("White wins!")
        if (self.white_pieces + self.black_pieces == ROWS * COLS):
            if (self.white_pieces > self.black_pieces):
                print("White wins!")
            elif (self.white_pieces < self.black_pieces):
                print("Black wins!")
            else:
                print("Draw.")

    def game_over(self):
        if (self.game_status):
            self.white_pieces = 0
            self.black_pieces = 0
            for i in range (BOARD_WIDTH):
                for j in range (BOARD_HEIGHT):
                    if (self.board[i][j] == WHITE):
                        self.white_pieces += 1
                    elif (self.board[i][j] == BLACK):
                        self.black_pieces += 1

            if (self.white_pieces > self.black_pieces):
                print("White wins!")
            elif (self.white_pieces < self.black_pieces):
                print("Black wins!")
            else:
                print("Draw.")

            game_over_font = pygame.font.SysFont(None, 48)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            WIN.blit(game_over_text, game_over_rect)

            pygame.display.update()
            pygame.time.delay(2000)  # Wait for 2 seconds before quitting

            return self.game_status
        
        return self.game_status
        