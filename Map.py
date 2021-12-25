import pygame as pg
import confiq
from confiq import map, map_size, map_cell_w, map_cell_h, c_size, background

class Map(pg.sprite.Sprite):
    def __init__(self, x, y, img, group):
        super().__init__(confiq.all_sprites, group)
        self.image = img
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self):
        pass


def build_map():
    surf = pg.Surface(map_size)
    for i in range(map_cell_w):
        for j in range(map_cell_h):
            cords = c_size * j, c_size * i
            surf.blit(background[map[i][j]], cords)
    return surf


map_img = build_map()
map_x, map_y = -confiq.spawn_x * c_size, -confiq.spawn_y * c_size
map_group = pg.sprite.Group()
map = Map(map_x, map_y, map_img, map_group)