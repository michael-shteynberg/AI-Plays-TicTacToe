# tictactoe

Description
This project implements an AI for playing Tic Tac Toe using the minimax algorithm, which guarantees optimal play. The AI explores all possible game states to choose the best move, ensuring it never loses - at best, you can only achieve a tie against it.


Files:

- tictactoe.py: Contains the game logic and AI implementation with the minimax algorithm
- runner.py: Provides the graphical interface using Pygame

Core Game Functions:

- initial_state(): Returns the starting empty 3x3 board
- player(board): Determines which player's turn it is (X or O)
- actions(board): Returns all valid moves as (row, column) coordinates
- result(board, action): Returns a new board state after applying a move
- winner(board): Checks if there's a winner (X, O, or None)
- terminal(board): Determines if the game is over (win or tie)
- utility(board): Evaluates terminal states (1 for X win, -1 for O win, 0 for tie)

AI Algorithm:

- minimax(board): Determines the optimal move using the minimax algorithm
- max_value(board): Helper function for X's optimal strategy (maximizing player)
- min_value(board): Helper function for O's optimal strategy (minimizing player)


The minimax algorithm recursively explores all possible game states to the end, assuming both players make optimal moves. It constructs a complete game tree where:

- X tries to maximize the final score (wants utility = 1)
- O tries to minimize the final score (wants utility = -1)
