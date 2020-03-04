import pygame as pg

from core.components.movement import Movement

class Player:
    def __init__(self, game, entity, vel=5):
        self.game = game
        self.entity = entity
        self.movements = Movement(self.entity, vel)
    
    def awake(self, entity=None, velocity=None):
        self.game.inputController.subscribe(pg.K_w, self.movements.moveUp)
        self.game.inputController.subscribe(pg.K_a, self.movements.moveLeft)
        self.game.inputController.subscribe(pg.K_d, self.movements.moveRight)
        self.game.inputController.subscribe(pg.K_s, self.movements.moveDown)

    def render(self):
        pg.draw.rect(self.game.win, (255, 0, 0), (self.entity.x, self.entity.y, self.entity.width, self.entity.length))