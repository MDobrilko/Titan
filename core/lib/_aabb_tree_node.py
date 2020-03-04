from core.lib.point     import *
from core.lib.rectangle import *

class AABB_TreeNode:
    def __init__(self, rect=None, other=None):
        if not other is None:
            self.__rect = other.__rect
            self.__leftNode = other.__leftNode
            self.__rightNode = other.__rightNode
        else:
            self.setLeaf(rect)

    
    def __eq__(self, value):
        return self.__rect == value.__rect
    

    def __ne__(self, value):
        return not self == value


    def isLeaf(self):
        return (not self.__rect is None and
                self.__leftNode is None and
                self.__rightNode is None)


    def isBranch(self):
        return not self.__leftNode is None and not self.__rightNode is None


    def getLeftNode(self):
        return self.__leftNode


    def getRightNode(self):
        return self.__rightNode
    

    def getRect(self):
        return self.__rect
    

    def setLeaf(self, rect):
        self.__rect = rect
        
        self.__leftNode = None
        self.__rightNode = None

    def setBranch(self, leftNode, rightNode):
        self.__leftNode = leftNode
        self.__rightNode = rightNode

        self.__rect.buildEnclosingRect(leftNode.__rect, rightNode.__rect)
    
    
    def getOtherChild(self, child):
        if self.isBranch():
            if child is self.getLeftNode():
                return self.getRightNode()
            elif child is self.getRightNode():
                return self.getLeftNode()
    

    def isCrossingRect(self, rect):
        return self.__rect.isCrossing(rect)