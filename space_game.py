# ГЛАВНЫЙ ЦИКЛ

import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800)) # создаем окошко
    pygame.display.set_caption("Космодисант") # присваиваем название
    bg_color = (0, 0, 0) # цвет окошка
    gun = Gun(screen) # создаем наш объект пушки
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)



    while True:
        # обработка всех событий
        controls.events(screen, gun, bullets) # передвежение пушечки
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos,bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)


run()