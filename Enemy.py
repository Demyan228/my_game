import pygame as pg
import confiq
import Effect

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, img, group, hp):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))
        self.add(group)
        self.hp = hp

    def update(self):
        pass

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def punch(self, power):
        Effect.Effect(self.rect.centerx, self.rect.centery, Effect.punch_effect, Effect.effects)
        self.hp -= power

def create_group_enemyes(path, cords, group, hp):
    ei = pg.image.load(path)
    ei.set_colorkey(pg.Color("green"))
    enemy_img = pg.transform.scale(ei, (confiq.sprite_w, confiq.sprite_h))
    for c in cords:
        x, y = c
        x = x - confiq.spawn_x * confiq.k_size
        y = y - confiq.spawn_y * confiq.k_size
        Enemy(x, y, enemy_img, group, hp)


enemyes = pg.sprite.Group()

enemyes1_path = r'pictures_need\enemy1.png'
cords_for_e1 = [(280, 280), (240, 240), (280, 200)]
create_group_enemyes(enemyes1_path, cords_for_e1, enemyes, 100)

enemyes2_path = r'pictures_need\enemy2.png'
cords_for_e2 = [(300, 40), (280, 80)]
create_group_enemyes(enemyes2_path, cords_for_e2, enemyes, 200)