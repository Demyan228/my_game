import pygame as pg
import os
import confiq


class Item:
    def __init__(self, name, img):
        self.name = name
        self.img = img
        self.characteristics = {}

    def get_characteristics(self):
        return self.characteristics

class Armor(Item):
    def __init__(self, name, img, armor, speed):
        super().__init__(name, img)
        self.characteristics = {"armor": armor, "speed": speed}

class Sword(Item):
    def __init__(self, name, img, power):
        super().__init__(name, img)
        self.characteristics = {"power": power}


def create_sword(name, file_name, power):
    fullname = os.path.join('pictures_need', file_name)
    si = pg.image.load(fullname)
    si.set_colorkey(si.get_at((0, 0)))
    sword = Sword(name, si, power)
    return sword


sword1 = create_sword("pixel sword", "sword1.png", 5)
sword2 = create_sword("common sword", "sword2.png", 7)
sword3 = create_sword("long sword", "sword3.png", 10)



