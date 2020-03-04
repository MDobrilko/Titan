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
        self.entity.y -= self.vel
        print(self.entity.x, self.entity.y)
    
    def moveRight(self):
        self.entity.x += self.vel
        print(self.entity.x, self.entity.y)
    
    def moveLeft(self):
        self.entity.x -= self.vel
        print(self.entity.x, self.entity.y)
    
    def moveDown(self):
        self.entity.y += self.vel
        print(self.entity.x, self.entity.y)