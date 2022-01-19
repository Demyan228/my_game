import pygame as pg
import confiq
from confiq import map, map_size, map_cell_w, map_cell_h, c_size

class Map(pg.sprite.Sprite):
    def __init__(self, x, y, img, group):
        super().__init__(confiq.all_sprites, group)
        self.image = img
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self):
        pass


def build_map():
    surf = pg.Surface(map_size)
    for i in range(map_cell_h):
        for j in range(map_cell_w):
            cords = c_size * j, c_size * i
            surf.blit(background[map[i][j]], cords)
    return surf

grass = pg.transform.scale(pg.image.load(r'pictures_need\tile_0050.png'),
                                   (c_size, c_size))
tree = pg.transform.scale(pg.image.load(r'pictures_need\tile_0048.png'),
                                  (c_size, c_size))
bush = pg.transform.scale(pg.image.load(r'pictures_need\tile_0036.png'),
                                  (c_size, c_size))
grass2 = pg.transform.scale(pg.image.load(r'pictures_need\tile_0019.png'),
                                   (c_size, c_size))
tree2 = pg.transform.scale(pg.image.load(r'pictures_need\tile_0016.png'),
                                  (c_size, c_size))
bush2 = pg.transform.scale(pg.image.load(r'pictures_need\tile_0013.png'),
                                  (c_size, c_size))
background = {"1": grass, "2": tree, "3": bush, "4": grass2, "5": tree2, "6": bush2}

map_img = build_map()
map_x, map_y = -confiq.spawn_x * c_size, -confiq.spawn_y * c_size
map_group = pg.sprite.Group()
map = Map(map_x, map_y, map_img, map_group)