import pygame as pg
from time import time
from random import randint
from Hero import hero
import confiq


class Skill(pg.sprite.Sprite):
    def __init__(self, x, y, img, group):
        super().__init__(confiq.all_sprites, group)
        self.image = img
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)

    def check_view(self):
        if not (0 <= self.rect.centerx <= confiq.DW and 0 <= self.rect.centery <= confiq.DH):
            self.kill()

    def update(self):
        pass


class Fireball(Skill):
    def __init__(self, x, y, img, group, speed, player_pos, dmg):
        super().__init__(x, y, img, group)
        dx, dy = x - player_pos[0], y - player_pos[1]
        self.m_x, self.m_y = confiq.move_to(dx, dy, speed)
        self.dmg = dmg

    def update(self):
        if pg.sprite.collide_mask(self, hero):
            hero.get_punch(self.dmg)
            self.kill()
        self.check_view()
        self.rect.x += self.m_x
        self.rect.y += self.m_y


class Wave(Skill):
    def __init__(self, x, y, r, w, group, speed, dmg):
        img = self.create_img(r, w)
        super().__init__(x, y, img, group)
        self.r = r
        self.w = w
        self.speed = speed
        self.dmg = dmg

    def create_img(self, r, w):
        surf = pg.Surface((r * 2, r * 2))
        pg.draw.circle(surf, (255, 255, 255), (r, r), r, width=w)
        surf.set_colorkey((0, 0, 0))
        return surf

    def update(self):
        if pg.sprite.collide_mask(self, hero):
            hero.get_punch(self.dmg)
            self.kill()
        if self.r >= confiq.max_r:
            self.kill()
        self.r += self.speed
        self.image = self.create_img(self.r, self.w)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pg.mask.from_surface(self.image)


def create_random_skill(skills, e_x, e_y, player_pos):
    if not skills:
        return
    s = skills[randint(0, len(skills) - 1)]
    if s == Wave:
        Wave(e_x, e_y, confiq.wave_r, confiq.wave_w,
             skills_group, confiq.wave_speed, confiq.wave_dmg)
    elif s == Fireball:
        Fireball(e_x, e_y, confiq.fireball_img, skills_group,
                 confiq.fireball_speed, player_pos, confiq.fireball_dmg)




skills_group = pg.sprite.Group()