import pygame as pg

pg.init()
pg.display.set_caption('Forgoten world')

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
c_size = 40
map_size = map_w, map_h = map_cell_w * c_size, map_cell_h * c_size

spawn_x, spawn_y = 10, 10
CW, CH = 10, 10
size = DW, DH = CW * c_size, CH * c_size
sprite_w, sprite_h = 30, 30
screen = pg.display.set_mode(size)
all_sprites = pg.sprite.Group()

grass = pg.transform.scale(pg.image.load(r'pictures_need\tile_0050.png'),
                                   (c_size, c_size))
tree = pg.transform.scale(pg.image.load(r'pictures_need\tile_0048.png'),
                                  (c_size, c_size))
bush = pg.transform.scale(pg.image.load(r'pictures_need\tile_0036.png'),
                                  (c_size, c_size))
background = {"1": grass, "2": tree, "3": bush}