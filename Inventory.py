import pygame as pg
import confiq
import os
import sys
from copy import copy
from confiq import draw_text, check_surf_collide
from Items import Sword, Armor


class Inventory:
    def __init__(self, closed_img, closed_x, closed_y, closed_w, closed_h):
        self.inventory = []
        self.equip_sword = None
        self.equip_armor = None
        self.target = None
        self.opened = False
        self.close_x = confiq.DW - confiq.close_w
        self.close_img = confiq.close_img
        self.close_y = 0
        self.closed_x = closed_x
        self.closed_y = closed_y
        self.opened_surf = self.create_opened_surf()
        self.closed_surf = pg.transform.scale(closed_img, (closed_w, closed_h))

    def create_opened_surf(self):
        surf = pg.Surface((confiq.DW, confiq.DH))
        surf.fill(confiq.inv_color)
        view_area_surf = self.create_view_area_surf(confiq.view_area_w,
                                                    confiq.view_area_h)
        surf.blit(view_area_surf, (confiq.view_area_x, confiq.view_area_y))
        surf.blit(self.create_inventory_items(confiq.inv_w, confiq.inv_h),
                 (confiq.inv_x, confiq.inv_y))
        surf.blit(self.close_img, (self.close_x, self.close_y))
        return surf

    def create_view_area_surf(self, w, h):
        surf = pg.Surface((w, h))
        surf.fill(confiq.view_area_color)
        if not self.target:
            return surf
        characteristic_text = []
        target_characteristics = self.target.get_characteristics()
        for i in target_characteristics:
            string = f"{i}: {target_characteristics[i]}"
            characteristic_text.append(string)
        draw_text(surf, 25, 25, [self.target.name], 30, pg.Color("black"))
        img = pg.transform.scale(self.target.img, confiq.view_area_img_scale)
        surf.blit(img, (w // 2 - img.get_rect().w // 2, 200))
        draw_text(surf, 10, 350, characteristic_text, 20, pg.Color("black"))
        equip_btn = pg.Surface((confiq.equip_btn_w, confiq.equip_btn_h))
        equip_btn.fill(pg.Color("green"))
        if self.target not in [self.equip_sword, self.equip_armor]:
            equip_btn_text = "equip"
        else:
            equip_btn_text = "equiped"
        draw_text(equip_btn, 0, 0, [equip_btn_text], equip_btn.get_height(), pg.Color("black"))
        surf.blit(equip_btn, (confiq.equip_btn_x, confiq.equip_btn_y))
        unequip_btn = pg.Surface((confiq.unequip_btn_w, confiq.unequip_btn_h))
        unequip_btn.fill(pg.Color("red"))
        draw_text(unequip_btn, 0, 0, ["unequip"], unequip_btn.get_height(), pg.Color("black"))
        surf.blit(unequip_btn, (confiq.unequip_btn_x, confiq.unequip_btn_y))
        return surf

    def create_inventory_items(self, w, h):
        surf = pg.Surface((w, h))
        for y in range(confiq.opened_inv_h):
            for x in range(confiq.opened_inv_w):
                indx = y * confiq.opened_inv_w + x
                item = self.create_inventory_item(indx)
                surf.blit(item, (x * (confiq.inv_item_w + confiq.inv_void_w),
                                 y * (confiq.inv_item_h + confiq.inv_void_h)))
        return surf

    def create_inventory_item(self, indx):
        surf = pg.Surface((confiq.inv_item_w, confiq.inv_item_h))
        surf.fill(confiq.inv_item_color)
        if indx >= len(self.inventory):
            return surf
        item = self.inventory[indx]
        img = pg.transform.scale(item.img, (confiq.inv_item_w, confiq.inv_item_h))
        surf.blit(img, (0, 0))
        if item in [self.equip_sword, self.equip_armor]:
            pg.draw.circle(surf, pg.Color("green"), (confiq.inv_equip_circle_x, confiq.inv_equip_circle_y),
                           confiq.inv_equip_circle_r)
        return surf

    def add_item(self, item):
        if len(self.inventory) < confiq.opened_inv_w * confiq.opened_inv_h:
            self.inventory.append(item)
            self.inventory.sort(key=lambda a: list(a.get_characteristics().values()),
                                reverse=True)
            self.opened_surf = self.create_opened_surf()

    def click(self):
        mouse_pos = pg.mouse.get_pos()
        if self.opened:
            if check_surf_collide(self.close_x, self.close_y,
                                  self.close_img, *mouse_pos):
                self.opened = False
            if pg.rect.Rect(confiq.equip_btn_x, confiq.equip_btn_y,
                            confiq.equip_btn_w, confiq.equip_btn_h).collidepoint(*mouse_pos):
                self.equip_item(self.target)

            if pg.rect.Rect(confiq.unequip_btn_x, confiq.unequip_btn_y,
                            confiq.unequip_btn_w, confiq.unequip_btn_h).collidepoint(*mouse_pos):
                self.unequip_item(self.target)

            if check_surf_collide(confiq.inv_x, confiq.inv_y,
                                  self.opened_surf, *mouse_pos):
                mouse_x = mouse_pos[0] - confiq.inv_x
                mouse_y = mouse_pos[1] - confiq.inv_y
                self.check_inv_collide(mouse_x, mouse_y)
        else:
            if check_surf_collide(self.closed_x, self.closed_y,
                                  self.closed_surf, *mouse_pos):
                self.opened = True

    def equip_item(self, item):
        if item.__class__ == Sword and not self.equip_sword:
            self.equip_sword = item
            self.opened_surf = self.create_opened_surf()
        elif item.__class__ == Armor and not self.equip_armor:
            self.equip_armor = item
            self.opened_surf = self.create_opened_surf()

    def unequip_item(self, item):
        if item.__class__ == Sword and self.equip_sword == item:
            self.equip_sword = None
            self.opened_surf = self.create_opened_surf()
        elif item.__class__ == Armor and self.equip_armor == item:
            self.equip_armor = None
            self.opened_surf = self.create_opened_surf()

    def check_inv_collide(self, x, y):
        dx = x % (confiq.inv_item_w + confiq.inv_void_w)
        dy = y % (confiq.inv_item_h + confiq.inv_void_h)
        item_x = x // (confiq.inv_item_w + confiq.inv_void_w)
        item_y = y // (confiq.inv_item_h + confiq.inv_void_h)
        item_indx = item_x + item_y * confiq.opened_inv_w
        if dx <= confiq.inv_item_w and dy <= confiq.inv_item_h and item_indx < len(self.inventory):
            self.target = self.inventory[item_indx]
            self.opened_surf = self.create_opened_surf()


    def draw(self, surf):
        if self.opened:
            surf.blit(self.opened_surf, (0, 0))
        else:
            surf.blit(self.closed_surf, (self.closed_x, self.closed_y))

    def get_equip_characteristics(self):
        charac = {}
        for item in [self.equip_sword, self.equip_armor]:
            if item:
                item_c = item.get_characteristics()
                for c in item_c:
                    charac[c] = charac.get(c, 0) + item_c[c]
        return charac



inv_img_path = r'pictures_need\inv_icon.png'
inv_img = pg.image.load(inv_img_path)
inv_img.set_colorkey(pg.Color("white"))
inventory = Inventory(inv_img, confiq.closed_inv_x, confiq.closed_inv_y,
                      confiq.closed_inv_w, confiq.closed_inv_h)
