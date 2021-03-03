import pygame
import time

pygame.init()
background = (123, 196, 88)
screen = pygame.display.set_mode(size=(400,400))
pygame.display.set_caption("First Game")
# Used for character
positionY = 150
positionX = 150
movement = 10

# option of character TODO add girl.png


# Load Guy Character
guy_right = pygame.image.load(r'assets/guy_right.png')
guy_left = pygame.image.load(r'assets/guy_left.png')
guy_right = pygame.transform.scale(guy_right, (100,150))
guy_left = pygame.transform.scale(guy_left, (100,150))

# Load objects
tree = pygame.image.load(r'assets/tree.png')

tree_x = 100
tree_y = 150

tree = pygame.transform.scale(tree, (100, 150))

guy_direction = guy_right

screen.fill(background)
screen.blit(tree,(tree_x,tree_y))
screen.blit(guy_right, (positionX,positionY))
pygame.key.set_repeat(10,100)
# pygame.mixer.music.load("assets/Black Parade.mp3") #TODO Create your own music
# pygame.mixer.music.play()


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_w]:
		
			screen.fill(background)
			tree_y = tree_y + movement
			

		if keys[pygame.K_a]:
		
			screen.fill(background)
			guy_direction = guy_left
			tree_x = tree_x + movement
			

		if keys[pygame.K_s]:

			screen.fill(background)
			tree_y = tree_y - movement
			

		if keys[pygame.K_d]:

			screen.fill(background)
			guy_direction = guy_right
			tree_x = tree_x - movement
			
		screen.blit(guy_direction, (positionX, positionY))
		screen.blit(tree,(tree_x, tree_y))
		pygame.display.update()