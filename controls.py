
#  ОТРИСОВКА ВСЕХ СОБЫТИЙ

import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets): # обработка событий

    for event in pygame.event.get():  # перебираем все события
        if event.type == pygame.QUIT:  # событе завершения игры
            sys.exit()  # закрываем игру
        elif event.type == pygame.KEYDOWN: # нажата клавиша
            # кнопка вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # кнопка влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            # клавиша пробел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # кнопка вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # кнопка влево
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, inos, bullets):  # обновление экрана
    screen.fill(bg_color)  # заливка
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets): # обновлять позиции пуль, что бы они не засоряли память
    bullets.update()  # помещаем пули на экран
    for bulet in bullets.copy():
        if bulet.rect.bottom <= 0:
            bullets.remove(bulet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def gun_kill(stats, screen, sc,  gun, inos, bullets):
# столкновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):
    # обновляет позицию пришельцев
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc, gun, inos,bullets):
    # проверка, добралась ли армия до нижнего ркая экрана
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

def create_army(screen, inos): #создание армии пришельцев
    ino = Ino(screen)
    ino_wight = ino.rect.width
    number_inos_x = int((700 - 2 * ino_wight) / ino_wight)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 4):
        for ino_number in range(number_inos_x):
            ino = Ino(screen) # cоздаем 1 пришельца
            ino.x = ino_wight + (ino_wight * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)


def check_high_score(stats, sc):
    # проверка новых рекордов
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f: # буква w как запись, write
            f.write(str(stats.high_score))