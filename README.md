# Othello Game with Pygame

This is an implementation of the classic Othello (Reversi) game using Python and Pygame. The game features a computer opponent that uses the Minimax algorithm with alpha-beta pruning for making moves.

## Installation

1. **Clone the repository**:
```
git clone https://github.com/yourusername/othello-game.git
cd othello-game
```
2. **Install the required packages**:

   
Make sure you have Python and Pygame installed. You can install Pygame using pip:

```bash
pip install pygame
```
## Usage

To start the game, simply run the main.py script:

```bash
python main.py
```
## Game Rules

Othello is a strategy board game for two players. The game is played on an 8x8 board and involves pieces that are black on one side and white on the other. The objective is to have the majority of your color pieces on the board at the end of the game.

#### Basic Rules:

- Players take turns placing pieces on the board.
- A move is valid if it outflanks one or more of the opponent's pieces.
- Outflanked pieces are flipped to the player's color.
- The game ends when neither player can make a valid move.
- The player with the most pieces of their color on the board wins.

## Files

- board.py: Contains the Board class, which manages the game board, valid moves, and game state.
- config.py: Stores game configuration constants such as window dimensions, colors, and piece sizes.
- main.py: The main script that runs the game loop, handles user input, updates the game state, and renders the game using Pygame.
- minimax.py: Implements the Minimax class with the minimax algorithm and alpha-beta pruning for the computer's moves.

## Credits

This game was developed using Python and Pygame. The Minimax algorithm with alpha-beta pruning is used for the computer opponent.
