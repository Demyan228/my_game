import pygame as pg
import sys
from time import time

# pygame
pg.init()
pg.font.init()
pg.display.set_caption('Forgoten world')
FPS = 60
clock = pg.time.Clock()


def load_level(filename):
    filename = "Levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]


    return level_map


def draw_text(surf, x, y, text, font_size, font_color):
    font = pg.font.Font(None, font_size)
    text_coord = y
    for line in text:
        string_rendered = font.render(line, 1, font_color)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = x
        text_coord += intro_rect.height
        surf.blit(string_rendered, intro_rect)

def check_surf_collide(x1, y1, surf : pg.Surface, x2, y2):
    rect = pg.rect.Rect(x1, y1, *surf.get_size())
    return rect.collidepoint(x2, y2)

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
                  "Экипировать предмет можно нажав на кнопку equip",
                  f"Для прохождения игры тебе нужно достичь {end_lvl} уровня"]

    fon = pg.Surface((DW, DH))
    fon.fill(pg.Color("black"))
    screen.blit(fon, (0, 0))
    draw_text(screen, 10, 50, intro_text, 30, pg.Color("white"))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pg.display.flip()
        clock.tick(FPS)

def end_screen():
    intro_text = ["YOU WIN", "",
                  "Поздровляю с победой",
                  "Вы можете продолжить играть"]

    fon = pg.Surface((DW, DH))
    fon.fill(pg.Color("black"))
    screen.blit(fon, (0, 0))
    draw_text(screen, 10, 50, intro_text, 40, pg.Color("white"))
    t = time()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN and time() - t > 1:
                return  # начинаем игру
        pg.display.flip()
        clock.tick(FPS)


# map
map = load_level("location1.txt") + load_level("location2.txt")

map_cell_w, map_cell_h = len(map[0]), len(map)
c_size = 60
map_size = map_w, map_h = map_cell_w * c_size, map_cell_h * c_size



# camera
CW, CH = 10, 10
size = DW, DH = CW * c_size, CH * c_size
screen = pg.display.set_mode(size)



# hero
end_lvl = 1
game_over = False
spawn_x, spawn_y = 10, 10
hero_hp = 100
hero_hp_w = 100
hero_hp_h = 25
hero_hp_x = DW - hero_hp_w // 2 - 5
hero_hp_y = 20
hero_lvl_w = 100
hero_lvl_h = 25
hero_lvl_x = DW - hero_lvl_w // 2 - 5
hero_lvl_y = hero_hp_y + hero_hp_h + 10
hero_xp = 10
hero_xp_cof = 1.5
hero_power = 10
power_from_lvl = 2


# enemy
e_hp_w = 40
e_hp_h = 10

# inventory
view_area_x = 0
view_area_y = 0
view_area_w = DW // 3
view_area_h = DH * 1
view_area_img_scale = (100 , 100)
view_area_color = pg.Color("white")
view_area_text_color = pg.Color("black")
equip_void = DW // 10
equip_btn_w = DW // 7
equip_btn_h = DH // 20
equip_btn_x = view_area_x + view_area_w // 2 - equip_btn_w // 2
equip_btn_y = DH - DH // 5
unequip_btn_w = equip_btn_w * 1
unequip_btn_h = equip_btn_h * 1
unequip_btn_x = equip_btn_x * 1
unequip_btn_y = equip_btn_y + DH // 15

closed_inv_w = 50
closed_inv_h = 50
closed_inv_x = DW - closed_inv_w
closed_inv_y = 300
opened_inv_w = 5
opened_inv_h = 7
inv_item_w = DW // 12
inv_item_h = DH // 12
inv_equip_circle_r = inv_item_w // 7
inv_equip_circle_x = inv_item_w - inv_equip_circle_r
inv_equip_circle_y = inv_equip_circle_r * 1
inv_x = view_area_w + view_area_x + DW // 15
inv_y = DH // 10
inv_w = DW - inv_x
inv_h = DH - inv_y
inv_void_w = 20
inv_void_h = 20
inv_color = pg.Color("black")
inv_item_color = pg.Color("white")



# sprites
sprite_w, sprite_h = 30, 30
all_sprites = pg.sprite.Group()

#
close_w = DW // 20
close_h = close_w * 1
close_path = r'pictures_need\tile_0010.png'
close_img = pg.image.load(close_path)
close_img = pg.transform.scale(close_img, (close_w, close_h))
