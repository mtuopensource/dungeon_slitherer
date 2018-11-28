from models import Entity
from pygame import image
from pygame import Surface

class Player(Entity):
    def __init__(self):
        Entity.__init__(self, "player.png")
