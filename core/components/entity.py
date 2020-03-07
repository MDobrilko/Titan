from core.lib.rectangle import Rectangle
from core.lib.point     import Point

class Entity:
    def __init__(self, size, pos):
        self.width = size[0]
        self.length = size[1]
        # self.height = size[2]

        self.x = pos[0]
        self.y = pos[1]
        # self.z = pos[2]
    

    def getRect(self):
        point1 = Point(self.x, self.y)
        point2 = Point(self.x + self.width, self.y + self.height)
        return Rectangle(point1, point2)  

    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        # self.z = pos[2]