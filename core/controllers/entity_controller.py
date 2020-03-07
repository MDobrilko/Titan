from core.lib.aabb_tree import AABB_Tree

class EntityController:
    def __init__(self, game):
        self.game = game
        self.tree = AABB_Tree()
        self.objects = {}


    def add(self, *args):
        for obj in args:
            self.objects[obj.entity] = obj
            self.tree.insert(obj.entity)
    

    def render(self):
        for obj in self.objects.values():
            obj.render()


    def delAllCrossings(self, entity):
        crossings = self.tree.findAllCrossings(entity)
        for entity in crossings:
            self.tree.erase(entity)
            self.objects.pop(entity)