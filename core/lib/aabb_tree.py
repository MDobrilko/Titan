from core.lib._aabb_tree_node import *

class AABB_Tree:
    def __init__(self):
        self.root = None
    

    def insert(self, rect):
        if self.root is None:
            self.root = AABB_TreeNode(rect)
            return

        newLeaf = AABB_TreeNode(rect)
        curNode = self.root
        parentNode = None

        if not curNode.isCrossing(rect):
            self.root = AABB_TreeNode()
            self.root.setBranch(
                leftNode=curNode,
                rightNode=newLeaf)
            return
        
        while not curNode.isLeaf():
            parentNode = curNode
            if curNode.getLeftNode().isCrossing(rect):
                curNode = curNode.getLeftNode()
            elif curNode.getRightNode().isCrossing(rect):
                curNode = curNode.getRightNode()
            else:
                curNode = curNode.getLeftNode()
                break
        
        newBranch = AABB_TreeNode()
        newBranch.setBranch(
            leftNode=newLeaf,
            rightNode=curNode)
        
        if not parentNode is None:
            if curNode is parentNode.getLeftNode():
                parentNode.setBranch(newBranch, parentNode.getRightNode())
            else:
                parentNode.setBranch(parentNode.getLeftNode(), newBranch)
    
    
    def findAllCrossings(self, rect):
        if self.root is None:
            return []
        
        stack = [self.root]
        crossings = []

        while stack:
            curNode = stack.pop()

            if curNode.isCrossing(rect):
                if curNode.isLeaf():
                    crossings.append(curNode.getRect())
                else:
                    stack.append(curNode.getLeftNode())
                    stack.append(curNode.getRightNode())
        
        return crossings
    

    def erase(self, rect):
        if self.root is None:
            return
        
        stack = [self.root]

        curNode = None
        parentNode = None
        greatParentNode = None

        while stack:
            greatParentNode = parentNode
            parentNode = curNode
            curNode = stack.pop()

            if curNode.isCrossing(rect):
                if curNode.isBranch():
                    stack.append(curNode.getLeftNode())
                    stack.append(curNode.getRightNode())
                elif curNode.isLeaf() and curNode.getRect() == rect:
                    self.__eraseNode(greatParentNode, parentNode, curNode)
    

    def __eraseNode(self, greatParentNode, parentNode, node):
        if parentNode is None:
            self.root = None
            return
        elif greatParentNode is None:
            self.root = parentNode.getOtherChild(node)
            return

        otherChild = parentNode.getOtherChild(node)
        if parentNode is greatParentNode.getLeftNode():
            greatParentNode.setBranch(
                leftNode=otherChild,
                rightNode=greatParentNode.getRightNode())
        else:
            greatParentNode.setBranch(
                leftNode=greatParentNode.getLeftNode(),
                rightNode=otherChild)