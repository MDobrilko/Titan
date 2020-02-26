class Entity:
    def __init__(self, size, pos):
        self.width = size[0]
        self.height = size[1]

        self.x = pos[0]
        self.y = pos[1]
    
    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]