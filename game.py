import pygame
pygame.init()
white = (255,255,255)
screen = pygame.display.set_mode(size=(400,400))

# Used for character
positionY = 200
positionX =  200
movement = 10


image = pygame.image.load(r'guy.png')
image = pygame.transform.scale(image, (100,150))
screen.fill(white)
screen.blit(image, (200,200))

pygame.mixer.music.load("assets/Black Parade.mp3")
pygame.mixer.music.play()
while True:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			
			positionY -= movement
			screen.fill(white)
			screen.blit(image, (positionX, positionY))

		if keys[pygame.K_a]:
			positionX -= movement
			screen.fill(white)
			screen.blit(image, (positionX, positionY))
		if keys[pygame.K_s]:
			positionY += movement
			screen.fill(white)
			screen.blit(image, (positionX, positionY))
		if keys[pygame.K_d]:
			positionX += movement
			screen.fill(white)
			screen.blit(image, (positionX, positionY))
			
		
		pygame.display.update()