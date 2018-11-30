from models import Entity
from pygame import image
from pygame import Surface

class Player(Entity):
    def __init__(self):
		'''https://opengameart.org/content/hero-spritesheets-ars-notoria'''
        Entity.__init__(self, "player.png")

		#Game Vars (Values subject to change)
		self.max_HP = 100
		self.curr_HP = 100
		self.max _MP = 100
		self.curr_MP = 100
		self.attack_range = (1, 8)
		
