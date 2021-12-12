import pygame as pg
import confiq

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, img, group):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect(
            center=(x, y))
        self.add(group)

    def update(self):
        pass

    def move(self, x, y):
        self.rect.x += x
        self.rect.y +=y

def create_group_enemyes(path, cords, group):
    ei = pg.image.load(path)
    ei.set_colorkey(pg.Color("green"))
    enemy_img = pg.transform.scale(ei, (confiq.sprite_w, confiq.sprite_h))
    for c in cords:
        x, y = c
        x = x - confiq.spawn_x * confiq.k_size
        y = y - confiq.spawn_y * confiq.k_size
        Enemy(x, y, enemy_img, group)


enemyes = pg.sprite.Group()

enemyes1_path = r'pictures_need\enemy1.png'
cords_for_e1 = [(280, 280), (240, 240), (280, 200)]
create_group_enemyes(enemyes1_path, cords_for_e1, enemyes)

enemyes2_path = r'pictures_need\enemy2.png'
cords_for_e2 = [(300, 40), (280, 80)]
create_group_enemyes(enemyes2_path, cords_for_e2, enemyes)