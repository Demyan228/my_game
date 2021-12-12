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
