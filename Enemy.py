import pygame as pg
import confiq
import Effect
from Stats import Hitpoints
from random import randint
from Skills import create_random_skill, Fireball, Wave
import Items
from copy import copy

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, img, xp, hp, group, chances_list, skills):
        super().__init__(confiq.all_sprites, group)
        self.xp = xp
        self.skills = skills
        self.skill_timer = 0
        self.spawn_img = img
        self.image = img
        self.chances_list = chances_list
        self.rect = self.image.get_rect(
            center=(x, y))
        self.spawn_hp = hp * 1
        self.rect.x = x
        self.rect.y = y
        self.init()

    def init(self):
        self.dead = False
        self.timer = 0
        self.skill_timer = 0
        self.target = None
        self.image = self.spawn_img
        self.hp = Hitpoints(self.rect.centerx, self.rect.centery - 15,
                            confiq.e_hp_w, confiq.e_hp_h, self.spawn_hp)

    def choose_random_item(self):
        r = randint(0, len(self.chances_list) - 1)
        return copy(self.chances_list[r])

    def update(self):
        if self.dead:
            self.timer += 1
            if self.timer >= 100:
                self.init()
            return
        if self.target:
            self.skill_timer += 1
            if self.skill_timer >= 200:
                self.skill_timer = 0
                create_random_skill(self.skills, *self.rect.center,
                                    self.target.get_pos())
            #dx = self.rect.centerx - self.target.get_pos()[0]
            #dy = self.rect.centery - self.target.get_pos()[1]
            #self.move(*confiq.move_to(dx, dy, confiq.e_speed))

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_punch(self, hero, power):
        if self.dead:
            return
        self.target = hero
        Effect.Effect(self.rect.centerx, self.rect.centery, Effect.punch_effect, Effect.effect_group)
        self.hp.punch(power)
        if self.hp.hp <= 0:
            hero.get_xp(self.xp)
            item = self.choose_random_item()
            if item:
                hero.get_item(item)
            self.dead = True
            self.hp.kill()
            self.image = pg.Surface((0, 0))


def create_chances_list(chances: dict):
    res = []
    s = sum(chances.values())
    for i in chances:
        res += [i] * int(1000 / s * chances[i])
    return res

def create_group_enemyes(path, cords, group, hp, xp, chances_list, skills=[]):
    ei = pg.image.load(path)
    ei.set_colorkey(pg.Color("green"))
    enemy_img = pg.transform.scale(ei, (confiq.sprite_w, confiq.sprite_h))
    for c in cords:
        x, y = c
        x = x - confiq.spawn_x * confiq.c_size
        y = y - confiq.spawn_y * confiq.c_size
        Enemy(x, y, enemy_img, group, hp, xp, chances_list, skills)


enemy_group = pg.sprite.Group()

enemyes1_path = r'pictures_need\enemy1.png'
e1_skills = [Fireball]
cords_for_e1 = [(280, 280), (240, 240), (280, 200)]
e1_chance_list = create_chances_list({None:70, Items.sword1:20, Items.sword2:10})
create_group_enemyes(enemyes1_path, cords_for_e1, 2,
                     500, enemy_group, e1_chance_list, e1_skills)

enemyes2_path = r'pictures_need\enemy2.png'
e2_skills = [Wave]
cords_for_e2 = [(300, 40), (280, 80)]
e2_chance_list = create_chances_list({None:80, Items.sword3:20})
create_group_enemyes(enemyes2_path, cords_for_e2, 4,
                     1000, enemy_group, e2_chance_list, e2_skills)