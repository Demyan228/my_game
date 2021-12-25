import pygame as pg
import confiq

class Hero(pg.sprite.Sprite):
    def __init__(self, x, y, img, group):
        super().__init__(confiq.all_sprites, group)
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))
        self.power = 10
        self.speed = 2

    def update(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.rect.y -= self.speed
        if key[pg.K_s]:
            self.rect.y += self.speed
        if key[pg.K_a]:
            self.rect.x -= self.speed
        if key[pg.K_d]:
            self.rect.x += self.speed

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def punch(self, enemy):
        enemy.punch(self.power)

def create_hero(path, group):
    hi = pg.image.load(path)
    hi.set_colorkey(pg.Color("green"))
    hero_img = pg.transform.scale(hi, (confiq.sprite_w, confiq.sprite_h))
    hero = Hero(confiq.DW // 2, confiq.DH // 2, hero_img, group)
    return hero


hero_path = r'pictures_need\character0.png'
hero_group = pg.sprite.Group()
hero = create_hero(hero_path, hero_group)

