import pygame
import time
import random
from object import Object

# initialize pygame
pygame.init()

screen = pygame.display.set_mode(size=(700,400))
middle_x = screen.get_width() / 2.5
middle_y = screen.get_height() / 2.5

pygame.display.set_caption("First Game")

# Used for character
movement = 10

# option of character TODO add girl.png


# Load Guy Character
guy_right = pygame.image.load(r'assets/guy_right.png')
guy_left = pygame.image.load(r'assets/guy_left.png')

# Scale
guy_right = pygame.transform.scale(guy_right, (100,150))
guy_left = pygame.transform.scale(guy_left, (100,150))

# Which direction his hair points initially
guy_direction = guy_right


# Load objects

#Trees
tree = pygame.image.load(r'assets/tree.png')
list_of_trees = []

def create_random_trees(num):

	global screen

	for _ in range(0,num):
		x = random.randint(0,1000)
		y = random.randint(0,1000)
		tree_obj = Object('tree', tree, x, y, screen)
		list_of_trees.append(tree_obj)


def update_trees(direction, screen):
	for tree in list_of_trees:
		tree.update(direction, screen)




# Background (map)
background = pygame.image.load(r'assets/background.png')
background = pygame.transform.scale(background, (800,800))
background_x = -1 * middle_x
background_y = -1 * middle_y


# For Menu Screen Text
color_dark = (100,100,100)
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Play Game' , True , color_dark)


# Menu Screen
running = True
while running:

	screen.blit(text , (middle_x, middle_y))
	pygame.display.update()

	for ev in pygame.event.get():
	  
		if ev.type == pygame.QUIT:
			pygame.quit()
	          
	    #checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			running = False


# Load Game Graphics
screen.blit(background, (background_x,background_y))
screen.blit(guy_right, (middle_x, middle_y))
create_random_trees(5)

pygame.mixer.music.load(r'assets/music.ogg')
pygame.mixer.music.play()


runing = True
while runing:

	pygame.display.update()

	direction = None 

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys = pygame.key.get_pressed()
		
		# Up
		if keys[pygame.K_w]:
			direction = 'up'
			background_y = background_y + movement

		# Left
		if keys[pygame.K_a]:
			direction = 'left'
			guy_direction = guy_left
			background_x = background_x + movement
			
		# Down
		if keys[pygame.K_s]:
			direction = 'down'
			background_y = background_y - movement
			
		# Right
		if keys[pygame.K_d]:
			direction = 'right'
			guy_direction = guy_right
			background_x = background_x - movement

		screen.blit(background, (background_x, background_y))
		screen.blit(guy_direction, (middle_x, middle_y))
		update_trees(direction, screen)
		