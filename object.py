import pygame


class Object:
	
	def __init__(self, obj_name, image, position_x, position_y, screen):


		self.obj_name = obj_name
		self.position_x = position_x 
		self.position_y = position_y

		object_image = image
		object_image = pygame.transform.scale(object_image, (100, 150))
		screen.blit(object_image,(position_x, position_y))

		self.object_image = object_image

		return None


	def update(self, direction, screen):
		
		if direction == 'up':
			self.position_y = self.position_y + 10
		if direction == 'down':
			self.position_y = self.position_y - 10
		if direction == 'right':
			self.position_x = self.position_x - 10
		if direction == 'left':
			self.position_x = self.position_x + 10
			
		screen.blit(self.object_image, (self.position_x, self.position_y))






