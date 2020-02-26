import pygame as pg

class InputController:
    def __init__(self):
        self.subscriptions = {}

    def render(self):
        keys = pg.key.get_pressed()
        for key_num in self.subscriptions:
            if keys[key_num]:
                self.publish(self.subscriptions[key_num])
    
    def clearSubs(self):
        self.subscriptions.clear()
    
    def subscribe(self, key, handler):
        if not key in self.subscriptions:
            self.subscriptions[key] = []
        self.subscriptions[key].append(handler)
    
    def publish(self, functions):
        for func in functions:
            func()