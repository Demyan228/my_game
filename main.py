import pygame as pg
import confiq
from Map import Map
from Hero import hero
from Enemy import enemyes


def move():
    keys = pg.key.get_pressed()
    speed_x = 0
    speed_y = 0
    if keys[pg.K_w]:
        speed_y = 2
    if keys[pg.K_s]:
        speed_y = -2
    if keys[pg.K_a]:
        speed_x = 2
    if keys[pg.K_d]:
        speed_x = -2

    h_x = hero.rect.x - speed_x
    h_y = hero.rect.y - speed_y


    speed_x_hero = 0
    speed_y_hero = 0

    print(h_x, map.x + map.DW)


    if h_x <= map.x or h_x + confiq.sprite_w >= map.x + map.DW:
        speed_x = 0
    elif h_x - map.x <= confiq.DW // 2 - confiq.sprite_w // 2 or map.x + map.DW - h_x <= confiq.DW // 2 + confiq.sprite_w // 2:
        speed_x_hero = -speed_x
        speed_x = 0
    if h_y <= map.y or h_y + confiq.sprite_h >= map.y + map.DH:
        speed_y = 0
    elif h_y - map.y <= confiq.DH // 2 - confiq.sprite_h // 2 or map.y + map.DH - h_y <= confiq.DH // 2 + confiq.sprite_h // 2:
        speed_y_hero = -speed_y
        speed_y = 0

    hero.move(speed_x_hero, speed_y_hero)

    for i in enemyes.sprites():
        i.move(speed_x, speed_y)
    map.move(speed_x, speed_y)

if __name__ == '__main__':

    running = True

    clock = pg.time.Clock()
    map = Map()
    screen = confiq.screen


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        move()

        screen.fill(pg.Color("white"))

        map.draw(screen)
        enemyes.draw(screen)
        screen.blit(hero.image, hero.rect)

        pg.display.flip()
        clock.tick(60)

        hero.update()
        enemyes.update()
    pg.quit()
