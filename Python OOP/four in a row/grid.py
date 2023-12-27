import pygame
from color import *

BLOCKS = 6


class Grid:
    def __init__(self, width, height, screen):
        self.__y_surf = None
        self.__x_surf = None
        self.__height = 600
        self.__width = 600
        self.__height_screen = height
        self.__width_screen = width
        self.__screen = screen
        self.matrix = [[0 for i in range(0, BLOCKS)] for j in range(0, BLOCKS)]
        self.__margin_x = (self.size_screen[0] - self.width) / 2
        self.__margin_y = (self.size_screen[1] - self.height) / 2

    def __get_coordinates(self, x, y):
        self.__x_surf = x - self.__margin_x
        self.__y_surf = y - self.__margin_y
        return self.__x_surf, self.__y_surf

    def is_map(self, x, y):
        return (BLOCKS * 100 >= self.__get_coordinates(x, y)[0] >= 0
                and BLOCKS * 100 >= self.__get_coordinates(x, y)[1] >= 0)

    def __get_idx_block(self):
        return (int(self.__y_surf / (self.__height / BLOCKS)),
                int(self.__x_surf / (self.__width / BLOCKS)))

    @property
    def row(self):
        return self.__get_idx_block()[0]

    @property
    def column(self):
        return self.__get_idx_block()[1]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def size_screen(self):
        return self.__width_screen, self.__height_screen

    def __draw_block(self, x, y, color):
        rect = pygame.Rect(x + self.__margin_x, y + self.__margin_y, int(self.width / BLOCKS),
                           int(self.height / BLOCKS))
        inner_rect = rect.inflate(-5, -5)
        pygame.draw.rect(self.__screen, (0, 0, 0), rect, 0)
        pygame.draw.rect(self.__screen, color, inner_rect, 0)

    def draw_grid(self):
        i = 0
        for x in range(0, self.width, int(self.width / BLOCKS)):
            j = 0
            for y in range(0, self.height, int(self.height / BLOCKS)):
                if self.matrix[j][i] == 0:
                    self.__draw_block(x, y, WHITE)
                elif self.matrix[j][i] == 1:
                    self.__draw_block(x, y, LIGHT_SALMON)
                else:
                    self.__draw_block(x, y, PALE_TURQUOISE)
                j += 1
            i += 1

    def __check_column(self, row, col):
        num_same = 1
        for i in range(row, BLOCKS - 1):
            if self.matrix[row][col] == self.matrix[i + 1][col]:
                num_same += 1
            else:
                break
        return num_same

    def __check_row(self, row, col):
        num_same = 1
        for i in range(col, BLOCKS - 1):
            if self.matrix[row][col] == self.matrix[row][i + 1]:
                num_same += 1
            else:
                break
        for i in range(col, 1, -1):
            if self.matrix[row][col] == self.matrix[row][i - 1]:
                num_same += 1
            else:
                break
        return num_same

    def __check_diagonal_descending(self, row, col):
        num_same = 1
        for i in range(1, BLOCKS - 1):
            if self.matrix[row][col] == self.matrix[row - i][col - i]:
                num_same += 1
            elif row + i < BLOCKS and col + i < BLOCKS and self.matrix[row][col] == self.matrix[row + i][col + i]:
                num_same += 1
            else:
                break
        return num_same

    def __check_diagonal_ascending(self, row, col):
        num_same = 1
        for i in range(1, BLOCKS - 1):
            if (row - i >= 0 and col + i < BLOCKS and
                    self.matrix[row][col] == self.matrix[row - i][col + i]):
                num_same += 1
            elif row + i < BLOCKS and col - i >= 0 and self.matrix[row][col] == self.matrix[row + i][col - i]:
                num_same += 1
            else:
                break
        return num_same

    def is_four_in_row(self, row, col):
        if (self.__check_column(row, col) >= 4 or self.__check_row(row, col) >= 4
                or self.__check_diagonal_descending(row, col) >= 4 or self.__check_diagonal_ascending(row, col) >= 4):
            return True
        return False

    def is_draw_game(self):
        for row in self.matrix:
            if 0 in row:
                return False
        return True
