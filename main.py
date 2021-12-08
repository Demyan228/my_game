import pygame as pg

class Hero:
    def __init__(self, screen, x, y, img):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = img

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


class Enemy:
    def __init__(self, screen, x, y, img):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = img

    def draw(self):
        screen.blit(self.img, (self.x, self.y))



if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Forgoten world')
    map = """
            1111111111
            1121113111
            1111111131
            1111111211
            1113112111
            1111111111
            1112111131
            1111111111
            1113111311
            1311131111
            """
    map = map.split()
    MW, MH = len(map), len(map[0])
    k_size = 40
    size = DW, DH = MW * k_size, MH * k_size
    screen = pg.display.set_mode(size)
    running = True


    clock = pg.time.Clock()
    blue = pg.Color("blue")
    white = pg.Color("white")
    green = pg.Color("green")

    hi = pg.image.load(r'pictures_need\character0.png')
    hi.set_colorkey(green)
    hero_img = pg.transform.scale(hi, (30, 30))
    hero = Hero(screen, 100, 100, hero_img)

    ei1 = pg.image.load(r'pictures_need\enemy1.png')
    ei1.set_colorkey(green)
    enemy_img1 = pg.transform.scale(ei1, (30, 30))
    cords_for_e1 = [(200, 200), (240, 240), (280, 200)]
    enemys1 = []
    for c in cords_for_e1:
        enemys1.append(Enemy(screen, *c, enemy_img1))

    ei2 = pg.image.load(r'pictures_need\enemy2.png')
    ei2.set_colorkey(green)
    enemy_img2 = pg.transform.scale(ei2, (30, 30))
    cords_for_e2 = [(300, 40), (280, 80)]
    enemys2 = []
    for c in cords_for_e2:
        enemys2.append(Enemy(screen, *c, enemy_img2))


    grass = pg.transform.scale(pg.image.load(r'pictures_need\tile_0050.png'), (k_size, k_size))
    tree = pg.transform.scale(pg.image.load(r'pictures_need\tile_0048.png'), (k_size, k_size))
    bush = pg.transform.scale(pg.image.load(r'pictures_need\tile_0036.png'), (k_size, k_size))
    background = {"1": grass, "2": tree, "3": bush}


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(white)
        for i in range(len(map)):
            for j in range(len(map[0])):
                cords = (k_size * i, k_size * j)
                screen.blit(background[map[i][j]], cords)
        for e in enemys1:
            e.draw()
        for e in enemys2:
            e.draw()
        hero.draw()
        pg.display.flip()
    pg.quit()
