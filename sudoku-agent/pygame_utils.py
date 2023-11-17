import pygame


def draw_box(x, y, unit, screen):
    """Draw a box around the current pygame coordinate"""
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * unit-3, (y + i)
                         * unit), (x * unit + unit + 3, (y + i)*unit), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * unit,
                         y * unit), ((x + i) * unit, y * unit + unit), 7)


def draw_grid(current_grid, unit, font1, screen):
    """Draw the initial gill and fill the numbered cells"""
    for row in range(9):
        for col in range(9):
            if current_grid[row][col] != 0:  # blue color for numbered cells
                pygame.draw.rect(screen, (0, 153, 153),
                                 (row * unit, col * unit, unit + 1, unit + 1))

                text1 = font1.render(str(current_grid[row][col]), 1, (0, 0, 0))
                screen.blit(text1, (row * unit + 15, col * unit + 15))

    for row in range(10):
        if row % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, row * unit),
                         (500, row * unit), thick)
        pygame.draw.line(screen, (0, 0, 0), (row * unit, 0),
                         (row * unit, 500), thick)


def draw_value(x, y, font1, screen, unit, value):
    """Draw the value on the current pygame coordinate"""
    text1 = font1.render(str(value), 1, (0, 0, 0))
    screen.blit(text1, (x * unit + 15, y * unit + 15))


def raise_error1(font1, screen):
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2(font1, screen):
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def add_cell_in_pygame(x, y, current_grid, unit, font1, screen):
    screen.fill((255, 255, 255))
    draw_grid(current_grid, unit, font1, screen)
    draw_box(x, y, unit, screen)
    pygame.display.update()
    pygame.time.delay(20)


def instruction(screen, font2):
    text1 = font2.render(
        "PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render(
        "ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


def result(font1, screen):
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
