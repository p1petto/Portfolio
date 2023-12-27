from grid import *
from color import *
import time
import numpy

WIDTH = 900
HEIGHT = 750
pygame.init()
pygame.display.set_caption('Four in a row')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

turn = 1


def message(msg, color):
    font_style = pygame.font.SysFont(None, 90)
    msg = font_style.render(msg, True, color)
    textRect = msg.get_rect()
    textRect.center = (WIDTH / 2, HEIGHT / 2)
    pygame.draw.rect(screen, WHITE, textRect, 0)
    screen.blit(msg, textRect)


def next_turn(t):
    if t == 1:
        return 2
    else:
        return 1


if __name__ == '__main__':
    run = True
    game_over = False
    pygame.init()
    clock.tick(30)
    grid = Grid(WIDTH, HEIGHT, screen)
    while run:
        screen.fill(MOCCASIN)
        grid.draw_grid()

        if game_over:
            message(f"Игрок {turn} выиграл", (0, 0, 0))
        elif grid.is_draw_game():
            message(f"Ничья", (0, 0, 0))
        pygame.display.update()
        # EventHandle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if grid.is_map(x, y):
                        if grid.matrix[grid.row][grid.column] == 0:
                            row = grid.row
                            while row < BLOCKS - 1:
                                grid.matrix[row][grid.column] = turn
                                grid.draw_grid()
                                time.sleep(0.15)
                                pygame.display.update()
                                grid.matrix[row][grid.column] = 0
                                if grid.matrix[row+1][grid.column] == 0:
                                    row += 1
                                else:
                                    break
                            grid.matrix[row][grid.column] = turn
                            if grid.is_four_in_row(row, grid.column):
                                game_over = True
                                break
                            turn = next_turn(turn)

    pygame.display.update()

    pygame.quit()
