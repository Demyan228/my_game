import pygame as pg
import confiq

class Map:
    def __init__(self):
        self.map = confiq.map

        self.MW, self.MH = confiq.MW, confiq.MH
        self.k_size = confiq.k_size
        self.size = self.DW, self.DH = self.MW * self.k_size, self.MH * self.k_size
        self.x, self.y = -confiq.spawn_x * self.k_size, -confiq.spawn_y * self.k_size
        grass = pg.transform.scale(pg.image.load(r'pictures_need\tile_0050.png'),
                                   (self.k_size, self.k_size))
        tree = pg.transform.scale(pg.image.load(r'pictures_need\tile_0048.png'),
                                  (self.k_size, self.k_size))
        bush = pg.transform.scale(pg.image.load(r'pictures_need\tile_0036.png'),
                                  (self.k_size, self.k_size))
        self.background = {"1": grass, "2": tree, "3": bush}

    def draw(self, screen):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                cords = (self.x + self.k_size * j, self.y + self.k_size * i)
                screen.blit(self.background[self.map[i][j]], cords)

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y