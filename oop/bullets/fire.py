import pygame
from oop.bullet import Bullet

class Fire(Bullet):
	max_bullet = 5000000000

	def __init__(self):
		Bullet.__init__(self, Fire.max_bullet)

	def tiles(self):
		return pygame.image.load('resources/images/fire.png')

	def shoot_sound(self):
		tmp = pygame.mixer.Sound("resources/audio/shoot.wav")
		tmp.set_volume(0.05)
		tmp.play()

	def hit_enemy_sound(self):
		pass

	def hit_enemy(self, enemies):
		pass
