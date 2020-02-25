import pygame
pygame.init()
background = (123, 196, 88)
screen = pygame.display.set_mode(size=(400,400))
pygame.display.set_caption("First Game")
# Used for character
positionY = 200
positionX =  200
movement = 10

# option of character TODO add girl.png
# character = input("guy or girl:")


# Load Guy Character
guy_right = pygame.image.load(r'assets/guy_right.png')
guy_left = pygame.image.load(r'assets/guy_left.png')
guy_right = pygame.transform.scale(guy_right, (100,150))
guy_left = pygame.transform.scale(guy_left, (100,150))
current = guy_right

screen.fill(background)
screen.blit(guy_right, (200,200))
pygame.key.set_repeat(10,100)
pygame.mixer.music.load("assets/Black Parade.mp3") #TODO Create your own music
pygame.mixer.music.play()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_w]:
		
			positionY -= movement
			screen.fill(background)
			screen.blit(current, (positionX, positionY))

		if keys[pygame.K_a]:
		
			positionX -= movement
			screen.fill(background)
			screen.blit(guy_left, (positionX, positionY))
			current = guy_left

		if keys[pygame.K_s]:
			positionY += movement
			screen.fill(background)
			screen.blit(current, (positionX, positionY))
		if keys[pygame.K_d]:
			positionX += movement
			screen.fill(background)
			screen.blit(guy_right, (positionX, positionY))
			current = guy_right
			
		
		pygame.display.update()