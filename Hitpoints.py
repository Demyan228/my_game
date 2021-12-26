import pygame as pg
from time import time
import confiq

class Hitpoints(pg.sprite.Sprite):
    def __init__(self, x, y, max_hp):
        super().__init__(confiq.all_sprites, hp_group)
        self.max_hp = max_hp
        self.hp = max_hp * 1
        self.image = self.create_img()
        self.rect = self.image.get_rect(
            center=(x, y))

    def create_hp_img(self):
        hp_w = int((confiq.hp_w - 4) * (self.hp / self.max_hp))
        hp_h = int(confiq.hp_h - 4)
        hp_img = pg.Surface((hp_w, hp_h))
        hp_img.fill(pg.Color("green"))
        return hp_img


    def create_img(self):
        image = pg.Surface((confiq.hp_w, confiq.hp_h))
        image.fill((255, 255, 255))
        image.blit(self.create_hp_img(), (2, 2))
        return image


    def update(self):
        pass

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def punch(self, power):
        self.hp = max(0, self.hp - power)
        self.image = self.create_img()


hp_group = pg.sprite.Group()