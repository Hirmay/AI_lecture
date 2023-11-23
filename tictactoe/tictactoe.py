"""
Tic Tac Toe Player
"""
import copy
import math
import sys

X = "X"
O = "O"
EMPTY = None

# here pytest would be really helpful


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # If the number of (X - O) = 1 then O's turn and vice versa
    cnt_X, cnt_O = 0, 0
    # checking if it's the initial state
    if not board:
        return "X"
    for row in board:
        for entry in row:
            if entry == "X":
                cnt_X += 1
            elif entry == "O":
                cnt_O += 1
    if cnt_X - cnt_O == 1 and cnt_X < 5:
        return "O"
    elif cnt_X - cnt_O == 0:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Essentially if there is an empty entry that is a possible action
    actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    # will return None if board is terminal
    if actions:
        return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action[0], action[1]
    if board[i][j] == "X" or board[i][j] == "O":
        raise ValueError("Invalid Action")
    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking for the set cases, trying to make the algorithm
    # somewhat optimal
    # pos_x, pos_o = [], []
    # for i in range(3):
    #     for j in range(2*(i%2) + 1):
    #         if board[i][(j + 2)%3] == "X":
    #             pos_x.append((i, (j + 2)%3))
    #         elif board[i][(j + 2)%3] == "O":
    #             pos_o.append((i, (j + 2)%3))

    # checking for horizontal
    for i in range(3):
        if board[i][0] == None:
            continue
        if board[i] == [board[i][0], board[i][0], board[i][0]]:
            return board[i][0]

    # checking for vertical
    cnt = 0
    for j in range(3):
        for k in range(3):
            if board[0][j] == None:
                # if one entry is none, no point checking
                break
            if board[k][j] == board[0][j]:
                cnt += 1
        if cnt == 3:
            return board[0][j]
        cnt = 0

    # now have to check for diagonal case
    if board[1][1] == None:
        return None
    if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
        return board[1][1]

    elif board[2][0] == board[1][1] and board[0][2] == board[1][1]:
        return board[1][1]

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    turn = player(board)
    winner_game = winner(board)
    # the game has ended if there is no turn left or there exists a winner
    if not turn or winner_game:
        return True
    else:
        return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_game = winner(board)
    if winner_game == "X":
        return 1
    elif winner_game == "O":
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # now we'd have to implement the max-value and the min-value functions
    def MAX_VALUE(board, action):
        # here the terminal check would be necessary as it'd be recursive
        if terminal(board):
            return utility(board), action
        # we'll compare it with neg infinity
        v = float("-inf")
        track_dict = {}
        for action in actions(board):
            y, action_output = MIN_VALUE(result(board, action), action)
            # if the v is already one, then don't need to look at other actions
            if y == 1:
                return y, action
            if y > v:
                v = y
                list_returned = (y, action)
        return list_returned

    def MIN_VALUE(board, action):
        if terminal(board):
            return utility(board), action
        # we'll compare it with pos infinity, might not need it
        v = float("inf")
        # might need to introduce a dict
        track_dict = {}
        for action in actions(board):
            y, action_output = MAX_VALUE(result(board, action), action)
            if y == -1:
                return y, action
            if y < v:
                v = y
                list_returned = (y, action)
        return list_returned

    # first have to find the current player on the board and the set of available actions
    current_player = player(board)
    if current_player == "X":
        return MAX_VALUE(board, None)[1]
    elif current_player == "O":
        return MIN_VALUE(board, None)[1]
