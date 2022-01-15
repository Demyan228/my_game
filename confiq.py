import pygame as pg

# pygame
pg.init()
pg.font.init()
pg.display.set_caption('Forgoten world')


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


# map
map = """
        11111111111113111111
        11211131111131111211
        11111111311311211111
        11111112111311111111
        11131121111111131111
        11112111211121111311
        11121111311111121111
        11111111111211111131
        11131113111111122111
        13111311111121112111
        11111111111111211111
        11211131112111311111
        11111111311111211111
        11111112111211111111
        11131121121121112111
        11111111111131111111
        11121111311111311111
        11111111111112311111
        11131113111111111111
        13111311111121131111
        """

map = map.split()
map_cell_w, map_cell_h = len(map), len(map[0])
c_size = 60
map_size = map_w, map_h = map_cell_w * c_size, map_cell_h * c_size



# camera
CW, CH = 10, 10
size = DW, DH = CW * c_size, CH * c_size
screen = pg.display.set_mode(size)



# hero
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
