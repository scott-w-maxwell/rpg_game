import pygame
import time

pygame.init()

screen = pygame.display.set_mode(size=(720,400))
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
# pygame.key.set_repeat(10,100)


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_w]:
			
			tree_y = tree_y + movement
			background_y = background_y + movement

			# Walking Animation
			screen.blit(background, (background_x, background_y))
			screen.blit(guy_walk_right_rfoot, (150, 150))
			screen.blit(tree,(tree_x, tree_y))
			pygame.display.update()
			time.sleep(.05)
			screen.blit(background, (background_x, background_y))
			screen.blit(tree,(tree_x, tree_y))
			screen.blit(guy_walk_right_lfoot, (150, 150))
			pygame.display.update()
			time.sleep(.05)

		if keys[pygame.K_a]:
			
			guy_direction = guy_left
			tree_x = tree_x + movement
			background_x = background_x + movement
			

		if keys[pygame.K_s]:

			tree_y = tree_y - movement
			background_y = background_y - movement
			
			# Walking Animation
			screen.blit(background, (background_x, background_y))
			screen.blit(guy_walk_right_rfoot, (150, 150))
			screen.blit(tree,(tree_x, tree_y))
			pygame.display.update()
			time.sleep(.05)
			screen.blit(background, (background_x, background_y))
			screen.blit(tree,(tree_x, tree_y))
			screen.blit(guy_walk_right_lfoot, (150, 150))
			pygame.display.update()
			time.sleep(.05)

		if keys[pygame.K_d]:

			guy_direction = guy_right
			tree_x = tree_x - movement
			background_x = background_x - movement

			# Walking Animation
			screen.blit(background, (background_x, background_y))
			screen.blit(guy_walk_right_rfoot, (150, 150))
			screen.blit(tree,(tree_x, tree_y))
			pygame.display.update()
			time.sleep(.05)
			screen.blit(background, (background_x, background_y))
			screen.blit(tree,(tree_x, tree_y))
			screen.blit(guy_walk_right_lfoot, (150, 150))
			pygame.display.update()
			time.sleep(.05)

		screen.blit(background, (background_x, background_y))
		screen.blit(guy_direction, (150, 150))
		screen.blit(tree,(tree_x, tree_y))
		pygame.display.update()