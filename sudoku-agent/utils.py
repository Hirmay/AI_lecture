import random

import pygame


grids = [
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ],
    [
        [0, 3, 0, 0, 8, 0, 0, 0, 6],
        [5, 0, 0, 2, 9, 4, 7, 1, 0],
        [0, 0, 0, 3, 0, 0, 5, 0, 0],
        [0, 0, 5, 0, 1, 0, 8, 0, 4],
        [4, 2, 0, 8, 0, 5, 0, 3, 9],
        [1, 0, 8, 0, 3, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 7, 0, 0, 0],
        [0, 4, 1, 6, 5, 3, 0, 0, 2],
        [2, 0, 0, 0, 4, 0, 0, 6, 0]
    ],
    [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 4, 1, 0, 2, 5, 0],
        [0, 1, 3, 0, 9, 5, 0, 0, 0],
        [8, 6, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 1, 0, 0, 0, 4, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 8, 6],
        [0, 0, 0, 8, 4, 0, 5, 3, 0],
        [0, 4, 2, 0, 3, 6, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
]


def is_valid(grid, row, col, value):
    """"Checks if any cell from the same row, col or square has same value"""
    for itr in range(9):
        if grid[row][itr] == value:
            return False
        if grid[itr][col] == value:
            return False

    square_row = row//3
    square_col = col//3

    for row in range(square_row * 3, square_row * 3 + 3):
        for col in range(square_col * 3, square_col * 3 + 3):
            if grid[row][col] == value:
                return False

    return True


def get_empty_squares(grid):
    """Returns a list of empty squares in the grid"""
    empty_squares = []

    for row in range(len(grid)):
        for col in range(len(grid[1])):
            if grid[row][col] == 0:
                empty_squares.append([row, col])

    return empty_squares


def update_possible_values(row, col, value, possible_values):
    """Update possible values when `value` is assigned to cell(grid[row][col])"""

    possible_values[row][col] = [0]

    for itr in range(9):
        if value in possible_values[row][itr]:
            possible_values[row][itr].remove(value)
        if value in possible_values[itr][col]:
            possible_values[itr][col].remove(value)

    square_row = row//3
    square_col = col//3

    for row in range(square_row * 3, square_row * 3 + 3):
        for col in range(square_col * 3, square_col * 3 + 3):
            if value in possible_values[row][col]:
                possible_values[row][col].remove(value)

    return possible_values


def get_possible_values(grid):
    possible_values = [[list(range(1, 10)) for _ in range(9)]
                       for _ in range(9)]

    for row in range(len(grid)):
        for col in range(len(grid[1])):
            if grid[row][col] != 0:
                value = grid[row][col]
                possible_values = update_possible_values(
                    row, col, value, possible_values)

    return possible_values


def is_forward_check_consistent(possible_values, value, row, col):
    """* Change Checks if the value is consistent with the possible values"""
    for col_itr in range(9):
        if col_itr != col:
            possible_cell_values = possible_values[row][col_itr]
            if len(possible_cell_values) == 1 and possible_cell_values[0] == value:
                print("returning from col", row, col_itr)
                return False

    for row_itr in range(9):
        if row_itr != row:
            possible_cell_values = possible_values[row_itr][col]

            if len(possible_cell_values) == 1 and possible_cell_values[0] == value:
                print("returning from row", row_itr, col)
                return False

    square_row = row//3
    square_col = col//3

    for square_row_itr in range(square_row * 3, square_row * 3 + 3):
        for square_col_itr in range(square_col * 3, square_col * 3 + 3):
            if square_row_itr != row and square_col_itr != col:
                possible_cell_values = possible_values[square_row_itr][square_col_itr]

                if len(possible_cell_values) == 1 and possible_cell_values[0] == value:
                    print("returning from square",
                          square_row_itr, square_col_itr)
                    return False

    return True


def solve_using_filtering(grid):
    empty_squares = get_empty_squares(grid)

    if len(empty_squares) == 0:
        return True

    pygame.event.pump()

    square = random.choice(empty_squares)
    row = square[0]
    col = square[1]

    possible_values = get_possible_values(grid)
    possible_cell_values = possible_values[row][col]

    while len(possible_cell_values) > 0:
        value = random.choice(possible_cell_values)
        possible_cell_values.remove(value)

        if is_forward_check_consistent(possible_values, value, row, col):
            grid[row][col] = value

            add_cell_in_pygame()

            if solve_using_filtering(grid):
                return True

            grid[row][col] = 0

    return False
