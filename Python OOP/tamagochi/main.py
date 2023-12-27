import pygame
from color import *
from ui import *

WIDTH = 800
HEIGHT = 400
CHANGE_RATE = 5
INCREASE_VALUE = 30

pygame.init()
pygame.display.set_caption('Tamagochi')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
clock = pygame.time.Clock()

class Pets():
    def __init__(self, width, height):
        self._W = width
        self._H = height
        self.__hp = WIDTH / 100 * 50
        self.__happiness = WIDTH / 100 * 50
        self.__is_alive = True

    def _draw_pet(self, path_img):
        self.__sprite_surf = pygame.image.load(path_img)
        self.__pet_rect = self.__sprite_surf.get_rect()
        self.__pet_rect.x = WIDTH / 2 - self._W / 2
        self.__pet_rect.y = HEIGHT / 2 - self._H
        screen.blit(self.__sprite_surf, self.__pet_rect)

    def check_hp(self):
        if (self.__hp > hp.max_val):
            self.__hp = hp.max_val
        if (self.__hp == 0):
            self.__is_alive = False

    def check_happiniess(self):
        if (self.__happiness > happy.max_val):
            self.__happiness = happy.max_val
        if (self.__happiness == 0):
            self.__is_alive = False

    def change_hp(self):
        self.__hp -= CHANGE_RATE

    def change_happiness(self):
        self.__happiness -= CHANGE_RATE

    def increase_hp(self):
        self.__hp += INCREASE_VALUE

    def increase_happiness(self):
        self.__happiness += INCREASE_VALUE

    @property
    def get_hp(self):
        return self.__hp

    @property
    def get_happiness(self):
        return self.__happiness

    @property
    def get_status(self):
        return self.__is_alive

    
class Frog(Pets):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw_pet(self, path_img):
        super()._draw_pet(path_img)
        
f = Frog(100, 100)
hp = Progress_bar(WIDTH  / 5, HEIGHT - HEIGHT / 2.1, GREEN, f.get_hp, 50, screen)
happy = Progress_bar(WIDTH  / 5, HEIGHT - HEIGHT / 5, GREEN, f.get_happiness, 50, screen)
feed = Button(WIDTH  / 14, HEIGHT - HEIGHT / 2, screen)
play = Button(WIDTH  / 14, HEIGHT - HEIGHT / 4, screen)
# MainLoop
def main():
    run = True
    while run:
        
        clock.tick(30)
        screen.fill(WHITE)
         
        feed._draw_button('img/food.png')
        play._draw_button('img/play.png')
        f.check_hp()
        f.check_happiniess()
        happy.draw_bar(f.get_happiness)
        hp.draw_bar(f.get_hp)
        if (f.get_status):
            f.draw_pet('img/frog.png')
            f.change_hp()
            f.change_happiness()
        else:
            f.draw_pet('img/die_frog.png')

        pygame.display.update()
        
        # EventHandle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if (f.get_status):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (feed.get_collider.collidepoint(pygame.mouse.get_pos())):
                        f.increase_hp()
                    
                    if (play.get_collider.collidepoint(pygame.mouse.get_pos())):
                        f.increase_happiness()

        pygame.display.update()
 
    pygame.quit()
 
 
main()