import pygame as pg
import random
from settings import *


class Coin:
    def __init__(self, pos, game):
        self.pos = pos
        self.game = game
        self.colour = random.choice(goldcolour)
        self.move()

    def move(self):
        cc = []
        if self.game.screen.get_at((self.pos[0], self.pos[1] + 3)) not in goldinter:
            self.pos = (self.pos[0], self.pos[1] + 3)
        else:
            if self.game.screen.get_at((self.pos[0] - 3, self.pos[1] + 3)) not in goldinter:
                cc.append((self.pos[0] - 3, self.pos[1] + 3))
            if self.game.screen.get_at((self.pos[0] + 3, self.pos[1] + 3)) not in goldinter:
                cc.append((self.pos[0] + 3, self.pos[1] + 3))
            if cc:
                self.pos = random.choice(cc)


class Inventory:
    def __init__(self, game):
        self.game = game
        self.inventory = []
        self.money = 0
        self.allmoney = []
        self.invgunselect = 0
        self.gridx = 0
        self.gridy = 0

        self.selectsquare = pg.transform.scale(pg.image.load(
            "select_square.png").convert_alpha(), (99, 99))

        self.revolver_sprite = pg.transform.scale(pg.image.load(
            "revolver_sprite.png").convert_alpha(), (99, 99))
        self.knuckduster_sprite =pg.transform.scale(pg.image.load(
            "knuckle_duster_sprite.png").convert_alpha(), (99, 99))
        self.shotgun_sprite = pg.transform.scale(pg.image.load(
            "shotgun_sprite.png").convert_alpha(), (99, 99))
        self.sniper_sprite = pg.transform.scale(pg.image.load(
            "sniper_sprite.png").convert_alpha(), (99, 99))
        self.inventory_frame = pg.transform.scale(pg.image.load(
            "inventory_frame.png").convert_alpha(), (1500, 900))

        self.shotgun_frame = pg.transform.scale(
            pg.image.load("unholy_shotgun_frame.png").convert_alpha(), (300, 180))
        self.shotgun_frame_small = pg.transform.scale(
            pg.image.load("unholy_shotgun_frame.png").convert_alpha(), (200, 120))
        self.shotgun_shell = pg.transform.scale(
            pg.image.load("slug.png").convert_alpha(), (90, 90))

        self.shot_shotgun_shell = pg.transform.scale(
            pg.image.load("shot_shell.png").convert_alpha(), (90, 90))

        self.shotgun_shell_small = pg.transform.scale(
            pg.image.load("slug.png").convert_alpha(), (60, 60))

        self.shot_shotgun_shell_small = pg.transform.scale(
            pg.image.load("shot_shell.png").convert_alpha(), (60, 60))

        self.shotgun_location = ((EWIDTH - 390), (HEIGHT - 360))
        self.shotgun_location_small = (50, HEIGHT-150)

        self.slug_locations = [(self.shotgun_location[0]+45, self.shotgun_location[1]+45), (self.shotgun_location[0]+165, self.shotgun_location[1]+45)]
        self.slug_locations_small = [(self.shotgun_location_small[0]+30, self.shotgun_location_small[1]+30), (self.shotgun_location_small[0]+110, self.shotgun_location_small[1]+30)]

        self.slugs = ["loaded","loaded"]

        self.revolver_cylinder = pg.transform.scale(
            pg.image.load("revolver_cylinder.png").convert_alpha(), (300, 300))

        self.revolver_cartridge = pg.transform.scale(
            pg.image.load("revolver_cartridge.png").convert_alpha(), (54, 54))

        self.revolver_cartridge_empty = pg.transform.scale(
            pg.image.load("revolver_cartridge_empty.png").convert_alpha(), (54, 54))

        self.revolver_cylinder_small = pg.transform.scale(
            pg.image.load("revolver_cylinder.png").convert_alpha(), (200, 200))

        self.revolver_cartridge_small = pg.transform.scale(
            pg.image.load("revolver_cartridge.png").convert_alpha(), (36, 36))

        self.revolver_cartridge_empty_small = pg.transform.scale(
            pg.image.load("revolver_cartridge_empty.png").convert_alpha(), (36, 36))

        self.bullets = [None, None, None, None, None, None]
        self.revolver_bulletpos = [
            ((EWIDTH - 267), (HEIGHT - 399)),
            ((EWIDTH - 180), (HEIGHT - 351)),
            ((EWIDTH - 180), (HEIGHT - 243)),
            ((EWIDTH - 267), (HEIGHT - 195)),
            ((EWIDTH - 354), (HEIGHT - 243)),
            ((EWIDTH - 354), (HEIGHT - 351))
        ]
        self.bulletpos_small = [
            (132, (HEIGHT - 236)),
            (190, (HEIGHT - 204)),
            (190, (HEIGHT - 132)),
            (132, (HEIGHT - 100)),
            (74, (HEIGHT - 132)),
            (74, (HEIGHT - 204))
        ]


        self.shell_shot = 0

    def draw(self):
        self.game.screen.blit(self.inventory_frame, ((EWIDTH - 1500) // 2, (HEIGHT - 900) // 2))
        self.game.screen.blit(self.game.ui.hotbarselect, ((EWIDTH - 1500) // 2 + 954+96*self.invgunselect, (HEIGHT - 900) // 2 + 63))
        self.game.screen.blit(self.revolver_sprite, ((EWIDTH - 1500) // 2 + 954, (HEIGHT - 900) // 2 + 63))
        self.game.screen.blit(self.shotgun_sprite, ((EWIDTH - 1500) // 2 + 1050, (HEIGHT - 900) // 2 + 63))
        self.game.screen.blit(self.sniper_sprite, ((EWIDTH - 1500) // 2 + 1146, (HEIGHT - 900) // 2 + 63))
        self.game.screen.blit(self.knuckduster_sprite, ((EWIDTH - 1500) // 2 + 1338, (HEIGHT - 900) // 2 + 63))


        if self.gridy < 5:
            self.game.screen.blit(self.selectsquare, (((EWIDTH - 1500) // 2 + 63 + self.gridx*96), ((HEIGHT - 900) // 2 + 63 + self.gridy * 96)))
        else:

            if self.gridx == 0:
                self.game.screen.blit(self.selectsquare, (((EWIDTH - 1500) // 2 + 120), ((HEIGHT - 900) // 2 + 705)))
            elif self.gridx == 1:
                self.game.screen.blit(self.selectsquare, (((EWIDTH - 1500) // 2 + 408), ((HEIGHT - 900) // 2 + 705)))
            else:
                self.game.screen.blit(self.selectsquare, (((EWIDTH - 1500) // 2 + 546), ((HEIGHT - 900) // 2 + 705)))
        if self.invgunselect == 0:
            self.game.screen.blit(self.revolver_cylinder, ((EWIDTH - 390), (HEIGHT - 420)))
            for i in range(len(self.bullets)):
                if self.bullets[i] is None:
                    continue
                elif self.bullets[i] == "loaded":
                    self.game.screen.blit(self.revolver_cartridge, self.revolver_bulletpos[i])
                else:
                    self.game.screen.blit(self.revolver_cartridge_empty, self.revolver_bulletpos[i])
        elif self.invgunselect == 1:
            self.game.screen.blit(self.shotgun_frame, self.shotgun_location)
            for i in range(len(self.slugs)):
                if self.slugs[i] is None:
                    continue
                if self.slugs[i] == "loaded":
                    self.game.screen.blit(self.shotgun_shell, self.slug_locations[i])
                else:
                    self.game.screen.blit(self.shot_shotgun_shell, self.slug_locations[i])



    def draw_unpause(self):
        if self.game.ui.selectedpos == 0:
            self.game.screen.blit(self.revolver_cylinder_small, (50, (HEIGHT - 250)))
            for i in range(len(self.bullets)):
                if self.bullets[i] is None:
                    continue
                elif self.bullets[i] == "loaded":
                    self.game.screen.blit(self.revolver_cartridge_small, self.bulletpos_small[i])
                else:
                    self.game.screen.blit(self.revolver_cartridge_empty_small, self.bulletpos_small[i])
        if self.game.ui.selectedpos == 1:
            self.game.screen.blit(self.shotgun_frame_small, self.shotgun_location_small)
            for i in range(len(self.slugs)):
                if self.slugs[i] is None:
                    continue
                elif self.slugs[i] == "loaded":
                    self.game.screen.blit(self.shotgun_shell_small, self.slug_locations_small[i])
                else:
                    self.game.screen.blit(self.shot_shotgun_shell_small, self.slug_locations_small[i])

    def update(self):
        for i in self.allmoney:
            i.move()
            pg.draw.rect(self.game.screen, i.colour, (i.pos[0], i.pos[1], 3, 3))
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.givegold(10)

    def givegold(self, amt):
        if self.money < 600:
            i = 0
            tt = 0
            while i < amt:
                if (WIDTH - 165 + tt * 3) < WIDTH - 3:
                    if self.game.screen.get_at((WIDTH - 165 + tt * 3, 423)) in goldinter:
                        tt += 1
                    else:
                        self.allmoney.append(Coin((WIDTH - 165 + tt * 3, 423), self.game))
                        i += 1
                        tt += 1
                else:
                    self.money += i
                    return
            self.money += amt

    def removegold(self, amt):
        temp = []
        self.money -= amt
        for i in range(len(self.allmoney) - amt):
            temp.append(self.allmoney[i])
        self.allmoney = temp

    def rotate_cylinder(self):
        self.bullets = self.bullets[-1:] + self.bullets[:-1]

    def on_shot_shell(self):
        self.shell_shot = (self.shell_shot+1)%2

    def check_inv_click(self, whichclick):

        x, y = pg.mouse.get_pos()
        if (HEIGHT - 900) // 2 + 66 < y < (HEIGHT - 900) // 2 + 66 + 96 * 5 and (EWIDTH - 1500) // 2 + 954 < x < (EWIDTH - 1500) // 2 + 954+96:
            self.invgunselect = ((x-((EWIDTH - 1500) // 2 + 954))//96)

        if ((EWIDTH - 1500) // 2 + 66 < x < (EWIDTH - 1500) // 2 + 66 + 96*8 and (HEIGHT - 900) // 2 + 66 < y <
                (HEIGHT - 900) // 2 + 66 + 96 * 5):

            self.gridx = ((x-((EWIDTH - 1500) // 2 + 66))//96)
            self.gridy = ((y-((HEIGHT - 900) // 2 + 66))//96)
        elif (((EWIDTH - 1500) // 2 + 120) < x < ((EWIDTH - 1500) // 2 + 216) and (HEIGHT - 900) // 2 + 705 < y <
              (HEIGHT - 900) // 2 + 801):

            self.gridx = 0
            self.gridy = 5
        elif (((EWIDTH - 1500) // 2 + 408) < x < ((EWIDTH - 1500) // 2 + 504) and (HEIGHT - 900) // 2 + 705 < y <
              (HEIGHT - 900) // 2 + 801):

            self.gridx = 1
            self.gridy = 5
        elif (((EWIDTH - 1500) // 2 + 546) < x < ((EWIDTH - 1500) // 2 + 642) and (HEIGHT - 900) // 2 + 705 < y <
              (HEIGHT - 900) // 2 + 801):

            self.gridx = 2
            self.gridy = 5
        if self.invgunselect == 0:
            for i in range(len(self.bullets)):
                if (self.revolver_bulletpos[i][0] < x < self.revolver_bulletpos[i][0] + 54 and
                        self.revolver_bulletpos[i][1] < y < self.revolver_bulletpos[i][1] + 54):
                    if whichclick == 1:
                        if self.bullets[i] is None:
                            self.bullets[i] = "loaded"
                    else:
                        if self.bullets[i] == "loaded":
                            self.bullets[i] = "fired"
                        else:
                            self.bullets[i] = None
            if (((EWIDTH - 390) + 150 - x) ** 2 + ((HEIGHT - 420) + 150 - y) ** 2) < 625:
                if whichclick != 1:
                    self.bullets = [None, None, None, None, None, None]
        if self.invgunselect == 1:
            for i in range(len(self.slugs)):
                if (self.slug_locations[i][0] < x < self.slug_locations[i][0] + 90 and
                        self.slug_locations[i][1] < y < self.slug_locations[i][1] + 90):
                    if whichclick == 1:
                        if self.slugs[i] is None:
                            self.slugs[i] = "loaded"
                    else:
                        if self.slugs[i] == "loaded":
                            self.slugs[i] = "fired"
                        else:
                            self.slugs[i] = None

