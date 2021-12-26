import pygame as pg
import confiq
import Effect
from Hitpoints import Hitpoints
from random import randint

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, img, group, hp):
        super().__init__(confiq.all_sprites, group)
        self.spawn_img = img
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))
        self.spawn_hp = hp * 1
        self.rect.x = x
        self.rect.y = y
        self.init()

    def init(self):
        self.dead = False
        self.timer = 0
        self.image = self.spawn_img
        self.hp = Hitpoints(self.rect.centerx, self.rect.centery - 15, self.spawn_hp)


    def update(self):
        if self.dead:
            self.timer += 1
            if self.timer >= 100:
                self.init()
            return

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def punch(self, power):
        Effect.Effect(self.rect.centerx, self.rect.centery, Effect.punch_effect, Effect.effect_group)
        self.hp.punch(power)
        if self.hp.hp <= 0:
            self.dead = True
            self.hp.kill()
            self.image = pg.Surface((0, 0))




def create_group_enemyes(path, cords, group, hp):
    ei = pg.image.load(path)
    ei.set_colorkey(pg.Color("green"))
    enemy_img = pg.transform.scale(ei, (confiq.sprite_w, confiq.sprite_h))
    for c in cords:
        x, y = c
        x = x - confiq.spawn_x * confiq.c_size
        y = y - confiq.spawn_y * confiq.c_size
        Enemy(x, y, enemy_img, group, hp)


enemy_group = pg.sprite.Group()

enemyes1_path = r'pictures_need\enemy1.png'
cords_for_e1 = [(280, 280), (240, 240), (280, 200)]
create_group_enemyes(enemyes1_path, cords_for_e1, enemy_group, 100)

enemyes2_path = r'pictures_need\enemy2.png'
cords_for_e2 = [(300, 40), (280, 80)]
create_group_enemyes(enemyes2_path, cords_for_e2, enemy_group, 200)