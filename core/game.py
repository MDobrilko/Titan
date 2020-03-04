import pygame as pg
from core.controllers.input_controller import InputController
from core.controllers.scenes_controller import ScneneController
from core.containers.player import Player
from core.components.entity import Entity

class Game:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((1000, 1000))

        pg.display.set_caption('Cubes Game')

        self.inputController = InputController()
        self.scenesController = ScneneController(self)
    
    def start(self):
        self.gameRun = True
        
        clock = pg.time.Clock()
        while self.gameRun:
            clock.tick(30)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.gameRun = False

            self.inputController.render()
            self.scenesController.render()

            pg.display.update()
        
        pg.quit()