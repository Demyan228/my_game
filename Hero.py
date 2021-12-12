import pygame as pg
import confiq

class Hero(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))

    def update(self):
        pass


def create_hero(path):
    hi = pg.image.load(path)
    hi.set_colorkey(pg.Color("green"))
    hero_img = pg.transform.scale(hi, (confiq.sprite_w, confiq.sprite_h))
    hero = Hero(confiq.DW // 2, confiq.DH // 2, hero_img)
    return hero


hero_path = r'pictures_need\character0.png'
hero = create_hero(hero_path)

