import pygame as pg
from time import time
import confiq

class Hitpoints(pg.sprite.Sprite):
    def __init__(self, x, y, hp_w, hp_h, max_hp, hero=False):
        groups = [hp_group]
        if not hero:
            groups.append(confiq.all_sprites)
        super().__init__(*groups)
        self.max_hp = max_hp
        self.hp = max_hp * 1
        self.hp_w = hp_w
        self.hp_h = hp_h
        self.image = self.create_img()
        self.rect = self.image.get_rect(
            center=(x, y))

    def create_hp_img(self):
        hp_w = int((self.hp_w - 4) * (self.hp / self.max_hp))
        hp_h = int(self.hp_h - 4)
        hp_img = pg.Surface((hp_w, hp_h))
        hp_img.fill(pg.Color("green"))
        return hp_img


    def create_img(self):
        image = pg.Surface((self.hp_w, self.hp_h))
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


class Level(pg.sprite.Sprite):
    def __init__(self, x, y, lvl_w, lvl_h, first_max_xp, max_xp_cof):
        super().__init__(lvl_group)
        self.max_xp = first_max_xp
        self.lvl = 0
        self.xp = 0
        self.lvl_w = lvl_w
        self.lvl_h = lvl_h
        self.max_xp_cof = max_xp_cof
        self.image = self.create_img()
        self.rect = self.image.get_rect(
            center=(x, y))

    def create_lvl_img(self):
        lvl_w = int((self.lvl_w - 4) * (self.xp / self.max_xp))
        lvl_h = int(self.lvl_h - 4)
        lvl_img = pg.Surface((lvl_w, lvl_h))
        lvl_img.fill(pg.Color("blue"))
        return lvl_img


    def create_img(self):
        image = pg.Surface((self.lvl_w, self.lvl_h))
        image.fill((255, 255, 255))
        image.blit(self.create_lvl_img(), (2, 2))
        font = pg.font.Font(None, 30)
        string_rendered = font.render(str(self.lvl), 1, pg.Color('grey'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 2
        intro_rect.x = 4
        image.blit(string_rendered, intro_rect)
        return image


    def update(self):
        pass

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_xp(self, xp):
        if self.xp + xp >= self.max_xp:
            self.xp = (self.xp + xp) % self.max_xp
            self.max_xp *= self.max_xp_cof
            self.lvl += 1
        else:
            self.xp += xp
        self.image = self.create_img()


hp_group = pg.sprite.Group()
lvl_group = pg.sprite.Group()
