import pygame as pg
import confiq
from confiq import all_sprites
from Inventory import inventory
from Map import map, map_group
from Hero import hero, hero_group
from Enemy import enemy_group
from Effect import effect_group
from Camera import Camera
from Stats import hp_group, lvl_group



if __name__ == '__main__':

    running = True

    clock = pg.time.Clock()
    camera = Camera()
    screen = confiq.screen


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                inventory.click()
                for e in enemy_group:
                    if pg.sprite.collide_rect(hero, e):
                        hero.punch(e)

        # изменяем ракурс камеры
        camera.update(hero)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)

        screen.fill(pg.Color("white"))

        map_group.draw(screen)
        enemy_group.draw(screen)
        effect_group.draw(screen)
        hp_group.draw(screen)
        lvl_group.draw(screen)
        hero_group.draw(screen)
        inventory.draw(screen)

        pg.display.flip()
        clock.tick(60)

        for sprite in all_sprites:
            sprite.update()
    pg.quit()
