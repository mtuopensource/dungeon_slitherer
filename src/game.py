from models import Player
import sys, pygame
from pygame import display
pygame.init()

wt = 1366
ht = 768
resolution = wt, ht
screen = display.set_mode(resolution)
title = "Dungeon Slitherer"
black = 0, 0, 0

entities = [Player()]

def update():
	'''game logic'''
	handle_events()
	for entity in entities:
		entity.update(0)

def render():
	'''draw entities and flip the buffer'''
	screen.fill(black)
	for entity in entities:
		entity.render(0, screen)
	display.flip()

def handle_events():
	'''capture events that we're interested in'''
	for event in pygame.event.get():
		# If the close button was pressed, exit the game.
		if event.type == pygame.QUIT:
			sys.exit()

def main():
	'''main game loop'''
	display.set_caption(title)
	while True:
		update()
		render()
	
if __name__ == "__main__": main()