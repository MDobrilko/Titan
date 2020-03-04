class Entity:
    def __init__(self, size, pos):
        self.width = size[0]
        self.length = size[1]
        # self.height = size[2]

        self.x = pos[0]
        self.y = pos[1]
        # self.z = pos[2]
    
    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        # self.z = pos[2]