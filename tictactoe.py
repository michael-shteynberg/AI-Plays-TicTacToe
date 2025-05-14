"""
Tic Tac Toe Player
"""

import math
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    i, j = action
    if action not in actions(board):
        raise Exception("Invalid action")
    
    new_board = copy.deepcopy(board)

    current_player = player(board)

    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not EMPTY:
        return board[2][0]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    
    current_player = player(board)

    possible_actions = actions(board)

    if current_player == X:
        best_value = float('-inf')
        best_action = None

        for action in possible_actions:
            value = min_value(result(board, action))

            if value > best_value:
                best_value = value
                best_action = action

    else:
        best_value = float('inf')
        best_action = None

        for action in possible_actions:
            value = max_value(result(board, action))

            if value < best_value:
                best_value = value
                best_action = action
    
    return best_action


def max_value(board):
    """
    Returns the maximum utility value possible for a board.
    """

    if terminal(board):
        return utility(board)

    value = float('-inf')

    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    
    return value

def min_value(board):
    """
    Returns the minimum utility value possible for a board.
    """

    if terminal(board):
        return utility(board)

    value = float('inf')
 
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    
    return value
