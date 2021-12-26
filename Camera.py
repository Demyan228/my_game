import pygame
from confiq import DW, DH
import confiq
from Map import map


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - DW // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - DH // 2)
        if map.rect.x + self.dx > 0:
            self.dx = 0
        if map.rect.x + map.rect.w + self.dx < DW:
            self.dx = 0
        if map.rect.y + self.dy > 0:
            self.dy = 0
        if map.rect.y + map.rect.h + self.dy < DH:
            self.dy = 0