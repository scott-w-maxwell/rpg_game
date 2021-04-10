import pygame
import time

# initialize pygame
pygame.init()

screen = pygame.display.set_mode(size=(400,400))
pygame.display.set_caption("First Game")

# Used for character
movement = 10

# option of character TODO add girl.png


# Load Guy Character
guy_right = pygame.image.load(r'assets/guy_right.png')
guy_left = pygame.image.load(r'assets/guy_left.png')
guy_walk_right_rfoot = pygame.image.load(r'assets/guy_right_rfoot.png')
guy_walk_right_lfoot = pygame.image.load(r'assets/guy_right_lfoot.png')

guy_right = pygame.transform.scale(guy_right, (100,150))
guy_left = pygame.transform.scale(guy_left, (100,150))
guy_walk_right_rfoot = pygame.transform.scale(guy_walk_right_rfoot,(100,150))
guy_walk_right_lfoot = pygame.transform.scale(guy_walk_right_lfoot,(100,150))

guy_direction = guy_right


# Load objects

#Trees
tree = pygame.image.load(r'assets/tree.png')
tree_x = 100
tree_y = 150
tree = pygame.transform.scale(tree, (100, 150))


# Background (map)
background = pygame.image.load(r'assets/background.png')
background_x = 0
background_y = 0


screen.blit(background, (background_x,background_y))
screen.blit(tree,(tree_x,tree_y))
screen.blit(guy_right, (150,150))

pygame.mixer.music.load(r'assets/music.ogg')
pygame.mixer.music.play()


runing = True
while runing:

	pygame.display.update()

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys = pygame.key.get_pressed()
		

		# Up
		if keys[pygame.K_w]:
			
			tree_y = tree_y + movement
			background_y = background_y + movement

		# Left
		if keys[pygame.K_a]:
			
			guy_direction = guy_left
			tree_x = tree_x + movement
			background_x = background_x + movement
			
		# Down
		if keys[pygame.K_s]:

			tree_y = tree_y - movement
			background_y = background_y - movement
			
		# Right
		if keys[pygame.K_d]:

			guy_direction = guy_right
			tree_x = tree_x - movement
			background_x = background_x - movement

		screen.blit(background, (background_x, background_y))
		screen.blit(guy_direction, (150, 150))
		screen.blit(tree,(tree_x, tree_y))
		