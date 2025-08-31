import pygame as pg
from settings import *
from player import *



class Map:
    def __init__(self,game):
        with open("maze.txt", "r") as file:

            minimap = [[(x) for x in line.split()] for line in file]

        for i in range(len(minimap)):
            minimap[i] = (list(minimap[i][0]))
        self.game = game
        self.mini_map = minimap
        self.world_map = {}
        self.get_map()
        self.oob = pg.transform.scale(pg.image.load(
            "out_of_bounds.png").convert_alpha(), (300, 300))

        self.mapplayer = pg.transform.scale(pg.image.load("player_map_icon.png").convert_alpha(), (48, 48))
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value == "1":
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, "darkgrey",(pos[0]*tile_size,pos[1]*tile_size,tile_size,tile_size), 2)
         for pos in self.world_map]
    def draw_minimap(self):

        map_rad = [4, 6, 8, 12, 16, 24]
        detail = 96
        checkwi = 288 // detail
        mapPerm = map_rad[self.game.player.maplevel - 1]
        # mapwidth = 288
        mpy = 6 + 144
        mpx = WIDTH - 294 + 144

        starty = self.game.player.y - mapPerm
        startx = self.game.player.x - mapPerm

        #self.game.screen.blit(self.oob, (WIDTH-300, 0))
        y = 0

        while y < detail:
            x = 0
            cy = starty + y / detail * 2 * mapPerm
            while x < detail:
                cx = startx + x / detail * 2 * mapPerm
                if 0 <= cy < mazedimensions and 0 <= cx < mazedimensions:
                    if lines[int(cy)][int(cx)] == "1":
                        pg.draw.rect(self.game.screen, (144, 144, 144),
                                         (*(WIDTH - 294 + x * checkwi, 6 + y * checkwi), checkwi, checkwi))

                    else:
                        pg.draw.rect(self.game.screen, (0, 0, 0),
                                     (*(WIDTH - 294 + x * checkwi, 6 + y * checkwi), checkwi, checkwi))


                else:
                    pass

                x += 1

            y += 1
        #self.game.screen.blit(self.mapplayer, (mpx, mpy))

        pg.draw.line(self.game.screen,(244,244,244),(mpx-1,mpy-1),
                     (mpx-1+math.cos(self.game.player.angle)*15,mpy-1+math.sin(self.game.player.angle)*15),2)

        pg.draw.circle(self.game.screen,(144,50,50),(mpx,mpy),6)