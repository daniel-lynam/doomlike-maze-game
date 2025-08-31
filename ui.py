import pygame as pg
from settings import *

pg.init()

class upgrade:
    def __init__(self, image, location, cost, function, ui, maximum=1):
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (102, 102))
        self.location = location
        self.function = function
        self.cost = cost
        self.ui = ui
        self.max = maximum
        self.money_invested = 0
        self.curbought = 0

    def addmoney(self):
        if self.curbought < self.max and self.ui.game.inventory.money > 10:
            self.ui.game.inventory.removegold(10)
            self.money_invested += 10
            if self.money_invested >= self.cost:
                self.money_invested -= self.cost
                self.curbought += 1
                self.function()


class UI:
    def __init__(self, game):
        self.game = game
        self.cross_hair = 0
        self.selectedpos = 0
         # minimap frame
        self.scaled_minimap = pg.transform.scale(pg.image.load(
            "minimap_outline.png").convert_alpha(), (300, 300))
        self.bank_title = pg.transform.scale(pg.image.load(
            "bank_title.png").convert_alpha(), (300, 90))
        self.upgrade_screen = pg.transform.scale(pg.image.load(
            "upgrade_screen.png").convert_alpha(), (300, 690))

        self.healthbar_frame = pg.transform.scale(pg.image.load(
            "healthbar_frame.png").convert_alpha(), (405, 60))

        self.crossleft = pg.image.load("cross_left.png").convert_alpha()
        self.crossright = pg.image.load("cross_right.png").convert_alpha()
        self.crossdown = pg.image.load("cross_down.png").convert_alpha()
        self.crossup = pg.image.load("cross_up.png").convert_alpha()

        self.goldframe = pg.transform.scale(pg.image.load("maxed_upgrade_frame.png").convert_alpha(), (102, 102))

        self.hotbar = pg.transform.scale(pg.image.load("hotbar.png").convert_alpha(), (483, 99))

        self.hotbarselect = pg.transform.scale(pg.image.load(
            "hotbar_select.png").convert_alpha(), (99, 99))

        self.allupgrades =[upgrade("map_up.png",(WIDTH-291, 570),
                                  50,self.increase_maplvl,self,2),
                           upgrade("speed_up.png",(WIDTH-291, 840),
                                  50,self.increase_speed,self,2),
                           upgrade("health_up.png", (WIDTH - 111, 966),
                                   50, self.increase_health, self, 2),
                           upgrade("vision_up.png", (WIDTH - 111, 705),
                                   50, self.increase_brightness, self, 2)
                           ]



    def draw(self):
        self.game.screen.blit(self.scaled_minimap, (WIDTH - 300, 0))
        self.game.screen.blit(self.bank_title, (WIDTH - 300, 300))
        self.game.screen.blit(self.upgrade_screen, (WIDTH - 300, 390))







    def draw_unpaused(self):
        if self.game.player.health > 0:
            pg.draw.line(self.game.screen, (100, 0, 0), ((EWIDTH - 405) / 2 + 12, 49),
                             ((EWIDTH - 376) / 2 + (376 * self.game.player.health / self.game.player.max_health) + 1, 49), 30)
        self.game.screen.blit(self.healthbar_frame, ((EWIDTH - 405) / 2, 20))
        self.game.screen.blit(self.crossleft, (EWIDTH / 2 - 5 - self.cross_hair, HEIGHT / 2 - 2))
        self.game.screen.blit(self.crossright, (EWIDTH / 2 + self.cross_hair, HEIGHT / 2 - 2))
        self.game.screen.blit(self.crossup, (EWIDTH / 2 - 2, HEIGHT / 2 - 9 - self.cross_hair))
        self.game.screen.blit(self.crossdown, (EWIDTH / 2 - 2, HEIGHT / 2 + self.cross_hair + 1))

        pg.draw.rect(self.game.screen,(0,0,0),(EWIDTH / 2 - 241, HEIGHT - 99, 483, 99))
        self.game.screen.blit(self.game.inventory.revolver_sprite, (EWIDTH / 2 - 241, HEIGHT - 99))
        self.game.screen.blit(self.game.inventory.knuckduster_sprite, (EWIDTH / 2 + 143, HEIGHT - 99))
        self.game.screen.blit(self.game.inventory.shotgun_sprite, (EWIDTH / 2 - 145, HEIGHT - 99))
        self.game.screen.blit(self.game.inventory.sniper_sprite, (EWIDTH / 2 - 49, HEIGHT - 99))
        self.game.screen.blit(self.hotbar,(EWIDTH / 2 - 241, HEIGHT - 99))
        self.game.screen.blit(self.hotbarselect, (EWIDTH / 2 - 241+96*self.selectedpos, HEIGHT - 99))

    def update(self):
        for i in self.allupgrades:
            if i.curbought >= i.max:
                self.game.screen.blit(self.goldframe, i.location)
            self.game.screen.blit(i.image, i.location)

        self.draw()
        if self.cross_hair >= 1:
            self.cross_hair -= 1
        if not self.game.pause:
            self.draw_unpaused()
        keys = pg.key.get_pressed()
        if keys[pg.K_1]:
            self.selectedpos = 0
        if keys[pg.K_2]:
            self.selectedpos = 1
        if keys[pg.K_3]:
            self.selectedpos = 2
        if keys[pg.K_4]:
            self.selectedpos = 3
        if keys[pg.K_5]:
            self.selectedpos = 4
    def increase_maplvl(self):
        self.game.player.maplevel += 1

    def increase_speed(self):
        self.game.player.speed += 0.0004

    def increase_health(self):
        self.game.player.max_health += 50

    def increase_brightness(self):
        self.game.player.visionlvl += 1

    def checkupgradeinteraction(self):
        x,y = pg.mouse.get_pos()
        for i in self.allupgrades:
            if i.location[0] < x < i.location[0] + 102 and i.location[1] < y < i.location[1] + 102:
                i.addmoney()