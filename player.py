from settings import *
import pygame as pg
import math
import random


class Player:
    def __init__(self, game):
        self.speed = player_base_speed
        self.game = game
        self.visionlvl = 1
        self.max_health = 100
        self.health = self.max_health
        self.x, self.y = (
        random.randint(0, availibledimensions - 1) * 2 + 1.5, random.randint(0, availibledimensions - 1) * 2 + 1.5)
        self.angle = player_angle
        self.maplevel = 1

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx = dy = 0
        speed = self.speed * self.game.delta_time
        speed_sin = sin_a * speed
        speed_cos = cos_a * speed

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pg.K_a]:
            self.angle -= player_rotation_speed * self.game.delta_time

        if keys[pg.K_d]:
            self.angle += player_rotation_speed * self.game.delta_time

        self.check_wall_collision(dx, dy)

        self.angle %= math.tau

    def draw(self):
        # pg.draw.line(self.game.screen,'yellow', (self.x * tile_size, self.y * tile_size),
        #             (self.x * tile_size + WIDTH * math.cos(self.angle),
        #              (self.y * tile_size) + WIDTH * math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen, "green", (self.x * tile_size, self.y * tile_size), 15)

    def update(self):
        self.movement()

    def shoot_revolver(self):
        if self.game.ui.cross_hair < 1:
            x, y = pg.mouse.get_pos()
            if x <= EWIDTH:
                if self.game.inventory.bullets[0] == "loaded":
                    self.game.inventory.bullets[0] = "fired"
                    self.game.ui.cross_hair = 6
                self.game.inventory.rotate_cylinder()
    def shoot_shotgun(self):
        if self.game.ui.cross_hair < 1:
            x, y = pg.mouse.get_pos()
            if x <= EWIDTH:
                if self.game.inventory.slugs[self.game.inventory.shell_shot] == "loaded":
                    self.game.inventory.slugs[self.game.inventory.shell_shot] = "fired"
                    self.game.ui.cross_hair = 15
                self.game.inventory.on_shot_shell()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
