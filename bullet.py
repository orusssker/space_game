# МЕХАННИКА ПУЛЬ

import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun): # создаем пулю в позиции пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12) # (0, 0) это координаты, (2 ширина 12 высота)
        self.color = 166, 230, 29
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    # перемещение вверх
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    # отрисовка пули на экране
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


