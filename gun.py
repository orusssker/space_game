# МЕХАННИКА ПУШКИ

import pygame
from  pygame.sprite import Sprite

class Gun(Sprite):
    # инициализация пушки
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self): # рисование пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self): # обновление позиции пушки в окошке
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 3.5
        if self.mleft and self.rect.left > 0:
            self.center -= 3.5

        self.rect.centerx = self.center

    def create_gun(self):
        # размещает пушку по центру внизу
        self.center = self.screen_rect.centerx
