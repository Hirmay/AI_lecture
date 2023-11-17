import random

import pygame

from utils import *
from pygame_utils import *


current_grid = grids[2]

# setting up pygame
screen = pygame.display.set_mode((505, 630))
# icon = pygame.image.load('icon.png')
# pygame.display.set_icon(icon)
pygame.display.set_caption("SUDOKU SOLVING AGENT")

pygame.font.init()
font1 = pygame.font.SysFont("arial", 35)
font2 = pygame.font.SysFont("arial", 13)

# starting point
x = 0
y = 0
unit = 500 / 9
val = 0


def update_pygame_coordinate(cell):
    """Update the pygame coordinate based on the cell"""
    global x, y

    x = cell[0] // unit
    y = cell[1] // unit

def solve_using_backtrack(grid):
    empty_squares = get_empty_squares(grid)

    if len(empty_squares) == 0:
        return True

    pygame.event.pump()
    d=[i for i in range(1,10)]
    square = random.choice(empty_squares)
    row = square[0]
    col = square[1]

    # possible_values = get_possible_values(grid)
    # possible_cell_values = possible_values[row][col]

    while len(d) > 0:
        value = random.choice(d)
        d.remove(value)

        if is_valid(grid,row,col,value):
            if solve_using_filtering(grid):
                return True
            else:
                grid[row][col] = 0
    return False
        

    
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

            add_cell_in_pygame(x, y, grid, unit, font1, screen)

            if solve_using_filtering(grid):
                return True

            grid[row][col] = 0

    return False

def solve_using_mrv(grid):
    empty_squares = get_empty_squares(grid)

    if len(empty_squares) == 0:
        return True

    pygame.event.pump()
    possible_values = get_possible_values(grid)
    list_containing_mrv = []
    for square in empty_squares:
        row = square[0]
        col = square[1]
        possible_cell_values = possible_values[row][col]
        list_containing_mrv.append(len(possible_cell_values))
    
    min_val = min(list_containing_mrv)
    squares_having_min_val = []
    for i in range(len(list_containing_mrv)):
        if list_containing_mrv[i] == min_val:
            squares_having_min_val.append(empty_squares[i])
    
    if(len(squares_having_min_val) == 1):
        square = squares_having_min_val[0]
    else:
        square = random.choice(squares_having_min_val)
    
    row = square[0]
    col = square[1]
    possible_cell_values = possible_values[row][col]
    while len(possible_cell_values) > 0:
        value = random.choice(possible_cell_values)
        possible_cell_values.remove(value)

        if is_forward_check_consistent(possible_values, value, row, col):
            grid[row][col] = value

            add_cell_in_pygame(x, y, grid, unit, font1, screen)

            if solve_using_mrv(grid):
                return True

            grid[row][col] = 0
    return False
    
# setting up flags
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0


while run:
    screen.fill((255, 255, 255))

    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            update_pygame_coordinate(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                current_grid = grids[0]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                current_grid = grids[2]

    if flag2 == 1:
        #if solve_using_backtrack(current_grid) == False:
        #if solve_using_filtering(current_grid) == False:
        if solve_using_mrv(current_grid) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0

    if val != 0:
        draw_value(x, y, font1, screen, unit, val)

        if is_valid(current_grid, int(x), int(y), val) == True:
            current_grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            current_grid[int(x)][int(y)] = 0
            raise_error2(font1, screen)

        val = 0

    if error == 1:
        raise_error1(font1, screen)

    if rs == 1:
        result(font1, screen)

    draw_grid(current_grid, unit, font1, screen)

    if flag1 == 1:
        draw_box(x, y, unit, screen)

    instruction(screen, font2)

    pygame.display.update()

pygame.quit()
