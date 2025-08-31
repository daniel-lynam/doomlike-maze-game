import pygame as pg
import sys
from player import *
from map import *
from settings import *
from raycasting import *
from ui import *
from inventory import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.ui = UI(self)
        self.inventory = Inventory(self)
        self.pause = False
    def update(self):

        self.raycasting.update()
        self.ui.update()
        self.inventory.update()
        if not self.pause:
            self.player.update()
            self.inventory.draw_unpause()
        else:
            self.inventory.draw()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")
    def draw(self):
        self.screen.fill('black')
        #pg.draw.rect(self.screen, (80, 80, 80), (0, 0, 1620, HEIGHT / 2))
        #pg.draw.rect(self.screen, (12, 12, 12), (0, HEIGHT / 2, 1620, HEIGHT / 2))
        self.map.draw_minimap()

        #self.player.draw()
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_TAB:
                self.pause = not self.pause
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.ui.checkupgradeinteraction()
                    if not self.pause:
                        if self.ui.selectedpos == 0:
                            self.player.shoot_revolver()
                        if self.ui.selectedpos == 1:
                            self.player.shoot_shotgun()

                if self.pause:
                    self.inventory.check_inv_click(event.button)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()