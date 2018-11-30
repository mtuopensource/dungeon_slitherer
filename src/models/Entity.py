from abc import ABC, abstractmethod
from pygame import image
from pygame import Surface

class Entity(ABC):
    def __init__(self, path):
		#Rendering vars
        self.sprite = image.load(path)
        self.pos = 0, 0
        self.rot = 0, 0
        self.size = 32, 32
        self.children = []

    def update(self, delta):
        pass

    def render(self, delta, screen):
        bounds = self.sprite.get_rect()
        screen.blit(self.sprite, bounds)