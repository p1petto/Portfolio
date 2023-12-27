from turtle import Screen
from color import *
import pygame

class Progress_bar():
    def __init__(self, x, y, color, w, h, screen):
        self._x = x
        self._y = y
        self._h = h
        self._w = w
        self._color = color
        self.sc = screen
        self.max_val = self._w
        self.min_val = 0

    def draw_bar(self, w):
        pygame.draw.rect(self.sc, self._color, (self._x, self._y, w, self._h))

class Button():
    def __init__(self, x, y, screen):
        self._x = x
        self._y = y
        self.sc = screen

    def _draw_button(self, path_img):
        self.__sprite_surf = pygame.image.load(path_img)
        self.__bt_rect = self.__sprite_surf.get_rect()
        self.__bt_rect.x = self._x
        self.__bt_rect.y = self._y
        self.sc.blit(self.__sprite_surf, self.__bt_rect)

    @property
    def get_collider(self):
        return self.__bt_rect