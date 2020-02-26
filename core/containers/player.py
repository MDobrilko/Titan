import pygame as pg

from core.components.movement import Movement
from core.components.entity import Entity

class Player:
    def __init__(self, game, entity, vel=20):
        self.game = game
        self.entity = entity
        self.movements = Movement(self.entity, 20)
    
    def awake(self, entity=None, velocity=None):
        if not entity is None:
            self.entity = entity
            self.movements.entity = entity
        elif not velocity is None:
            self.movements.vel = velocity

        self.game.inputController.subscribe(pg.K_w, self.movements.moveUp)
        self.game.inputController.subscribe(pg.K_a, self.movements.moveLeft)
        self.game.inputController.subscribe(pg.K_d, self.movements.moveRight)
        self.game.inputController.subscribe(pg.K_s, self.movements.moveDown)

    def render(self):
        pg.draw.rect(self.game.win, (255, 0, 0), (self.entity.x, self.entity.y, self.entity.width, self.entity.height))