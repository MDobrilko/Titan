import pygame as pg

from core.containers.player import Player
from core.components.entity import Entity

class ScneneController:
    def __init__(self, game):
        self.game = game

        self.scenes = {
            'lvl1' : self.lvl1
        }
        self.startScene('lvl1')
    
    def startScene(self, scene : str):
        if not scene in self.scenes:
            raise Exception("Сцены {} не существует".format(scene))
        
        self.game.inputController.clearSubs()
        self.scenes[scene]()
    
    def lvl1(self):
        self.player = Player(self.game, Entity(size=(40, 60), pos=(50, 50)))
        self.player.awake()
    
    def render(self):
        self.game.win.fill((0, 0, 0))
        self.game.win.blit(pg.image.load('D:/Programmes/bin/python/Titan/Titan/assets/textures/furniture/Room estructure.png'), (0, 0))
        self.player.render()