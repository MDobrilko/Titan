import pygame as pg

class Movement:
    def __init__(self, entity, velocity):
        self.vel = velocity
        self.entity = entity

        self.conditions = { 'up' : [], 'left' : [], 'right' : [], 'down' : [] }
    
    def addCondition(self, direction : str, cond : callable):
        self.conditions[direction].append(cond)
    
    def isPossible(self, direction, arg):
        for cond in self.conditions[direction]:
            if not cond(arg):
                return False
        return True

    def moveUp(self):
        print('w')
        self.entity.y -= self.vel
    
    def moveRight(self):
        print('d')
        self.entity.x += self.vel
    
    def moveLeft(self):
        print('a')
        self.entity.x -= self.vel
    
    def moveDown(self):
        print('s')
        self.entity.y += self.vel