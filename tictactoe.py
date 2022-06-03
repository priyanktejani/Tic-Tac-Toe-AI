"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    if x_count > o_count:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                possible_actions.add((i, j)) 
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # If action is not a valid, rise exception
    if board[i][j] is not EMPTY:
        raise Exception

    board_copy = deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_positions = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], 
                         [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
                         [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                         [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    for position in winning_positions:
        for winner in (X, O):
            if all(board[row][cell] == winner for row, cell in position):
                return winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None and actions(board):
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)

    if win_player is X:
        return 1
    elif win_player is O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # Alpha-beta pruning source:
    # geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning
    alpha = - math.inf
    beta = math.inf

    if player(board) == X:
        if board == initial_state():
            return (0, 0)
        move = max_value(board, alpha, beta)[1]
        return move
    else:
        move = min_value(board, alpha, beta)[1]
        return move


def max_value(board, alpha, beta):
    """
    Returns the maximum utility and optimal move
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    move = None
    for action in actions(board):
        v = max(v, min_value((result(board, action)),  alpha,beta)[0])
        if v > alpha:
            alpha = v
            move = action
        if beta <= alpha:
            break
    return v, move


def min_value(board, alpha, beta):
    """
    Returns the minimum utility and optimal move
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    move = None
    for action in actions(board):
        v = min(v, max_value((result(board, action)), alpha, beta)[0])
        if v < beta:
            beta = v
            move = action
        if beta <= alpha:
            break
    return v, move
