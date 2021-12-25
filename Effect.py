import pygame as pg
from time import time
import confiq

class Effect(pg.sprite.Sprite):
    def __init__(self, x, y, img, group):
        super().__init__(confiq.all_sprites, group)
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))
        self.add(group)
        self.punch_time = time()

    def update(self):
        if time() - self.punch_time > 0.1:
            self.kill()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y




effect_group = pg.sprite.Group()
punch_effect_path = r'pictures_need\tile_0005.png'
punch_effect = pg.image.load(punch_effect_path)
punch_effect.set_colorkey(pg.Color("black"))
punch_effect = pg.transform.scale(punch_effect, (confiq.sprite_w, confiq.sprite_h))