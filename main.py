import pygame as pg
import sys
import confiq
from confiq import all_sprites
from Inventory import inventory
from Map import map, map_group
from Hero import hero, hero_group
from Enemy import enemy_group
from Effect import effect_group
from Camera import Camera
from Stats import hp_group, lvl_group
from Skills import skills_group




if __name__ == '__main__':

    camera = Camera()
    screen = confiq.screen

    confiq.start_screen()


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                confiq.terminate()
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
        hero_group.draw(screen)
        skills_group.draw(screen)
        hp_group.draw(screen)
        lvl_group.draw(screen)
        inventory.draw(screen)


        pg.display.flip()
        confiq.clock.tick(confiq.FPS)

        for sprite in all_sprites:
            sprite.update()

