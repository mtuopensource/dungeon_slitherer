from models import Entity
from pygame import image
from pygame import Surface

class Player(Entity):
    def __init__(self):
		'''https://opengameart.org/content/hero-spritesheets-ars-notoria'''
        Entity.__init__(self, "player.png")
