import sys, pygame
pygame.init()

wt = 1366
ht = 768
resolution = wt, ht
screen = pygame.display.set_mode(resolution)

black = 0, 0, 0

def update():
	'''game logic'''
	handle_events()

def render():
	'''draw entities and flip the buffer'''
	screen.fill(black)
	pygame.display.flip()

def handle_events():
	'''capture events that we're interested in'''
	for event in pygame.event.get():
		# If the close button was pressed, exit the game.
		if event.type == pygame.QUIT:
			sys.exit()

def main():
	'''main game loop'''
	while True:
		update()
		render()
	
if __name__ == "__main__": main()