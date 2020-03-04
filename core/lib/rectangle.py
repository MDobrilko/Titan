from core.lib.point import *

class Rectangle:
    def __init__(self, point1, point2):
        self.__point1 = Point(
                min(point1.x, point2.x),
                min(point1.y, point2.y))
        self.__point2 = Point(
                max(point1.x, point2.x),
                max(point1.y, point2.y))
    
    
    def __eq__(self, value):
        return self.__point1 == value.__point1 and self.__point2 == value.__point2
    

    def getMinX(self):
        return self.__point1.x


    def getMinY(self):
        return self.__point1.y


    def getMaxX(self):
        return self.__point2.x


    def getMaxY(self):
        return self.__point2.y
    
    
    def buildEnclosingRect(self, rect1, rect2):
        point1 = Point(
            min(rect1.getMinX(), rect2.getMinX()),
            min(rect1.getMinY(), rect2.getMinY()))

        point2 = Point(
            max(rect1.getMaxX(), rect2.getMaxX()),
            max(rect1.getMaxY(), rect2.getMaxY()))

        self.__rect = Rectangle(point1, point2)
    

    def isCrossing(self, other):
        if other is None:
            return False

        return (self.getMaxX() > other.minX() and 
            self.getMinX() < other.getMaxX() and 
            self.getMaxY() > other.getMinY() and 
            self.getMinY() < other.getMaxY())