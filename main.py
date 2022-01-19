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




def terminate():
    pg.quit()
    sys.exit()

def start_screen():
    intro_text = ["FORGOTTEN WORLD", "",
                  "Тебе нужно исследовать карту и убивать монстров",
                  "Бить монстров можно на левую кнопку мыши",
                  "Есть определенный шанс выпадения предмета с монстра",
                  "Предметы улучшают твои статы",
                  "Если тебе выпал предмет, он перемещается в инвентарь",
                  "Ты можешь открыть инвентарь нажав на рюкзак",
                  "Нажми на предмет и справа покажется инфа о нем",
                  "Экипировать предмет можно нажав на кнопку equip"]

    fon = pg.Surface((confiq.DW, confiq.DH))
    fon.fill(pg.Color("black"))
    screen.blit(fon, (0, 0))
    confiq.draw_text(screen, 10, 50, intro_text, 30, pg.Color("white"))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pg.display.flip()
        clock.tick(FPS)



if __name__ == '__main__':


    FPS = 60
    clock = pg.time.Clock()
    camera = Camera()
    screen = confiq.screen

    start_screen()


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
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
        clock.tick(FPS)

        for sprite in all_sprites:
            sprite.update()
