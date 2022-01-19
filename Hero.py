import pygame as pg
import confiq
from confiq import hero_hp, hero_hp_x, hero_hp_y, hero_hp_w,\
    hero_hp_h, hero_power, power_from_lvl
from confiq import hero_lvl_h, hero_lvl_w, hero_lvl_x,\
    hero_lvl_y, hero_xp, hero_xp_cof
from Stats import Hitpoints, Level
from Inventory import inventory

class Hero(pg.sprite.Sprite):
    def __init__(self, x, y, img, group, max_hp, power, inv):
        super().__init__(confiq.all_sprites, group)
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))
        self.power = power * 1
        self.speed = 2
        self.max_hp = max_hp
        self.inv = inv
        self.hp = Hitpoints(hero_hp_x, hero_hp_y, hero_hp_w,
                            hero_hp_h, max_hp, hero=True)
        self.lvl = Level(hero_lvl_x, hero_lvl_y, hero_lvl_w,
                         hero_lvl_h, hero_xp, hero_xp_cof)

    def update(self):
        key = pg.key.get_pressed()
        speed = self.speed + self.inv.get_equip_characteristics().get("speed", 0)

        if key[pg.K_w]:
            self.rect.y = max(0, self.rect.y - speed)
        if key[pg.K_s]:
            self.rect.y = min(confiq.DH - confiq.sprite_h, self.rect.y + speed)
        if key[pg.K_a]:
            self.rect.x = max(0, self.rect.x - speed)
        if key[pg.K_d]:
            self.rect.x = min(confiq.DW - confiq.sprite_w, self.rect.x + speed)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def punch(self, enemy):
        all_power = self.power + power_from_lvl * self.lvl.lvl + self.inv.get_equip_characteristics().get("power", 0)
        enemy.punch(self, all_power)

    def get_xp(self, xp):
        self.lvl.get_xp(xp)
        if not confiq.game_over and self.lvl.lvl >= confiq.end_lvl:
            confiq.end_screen()
            confiq.game_over = True

    def get_item(self, item):
        self.inv.add_item(item)

def create_hero(path, group, hero_hp, power, inv):
    hi = pg.image.load(path)
    hi.set_colorkey(pg.Color("green"))
    hero_img = pg.transform.scale(hi, (confiq.sprite_w, confiq.sprite_h))
    hero = Hero(confiq.DW // 2, confiq.DH // 2, hero_img, group, hero_hp, power, inv)
    return hero


hero_path = r'pictures_need\character0.png'
hero_group = pg.sprite.Group()
hero = create_hero(hero_path, hero_group, hero_hp, hero_power, inventory)

