# name file: levels.py
# python version 3

import pygame

import constants
import platforms

class Level():

	def __init__(self, player):

		# Lists of sprites used in all levels. Add or remove
		# lists as needed for your game.
		self.platform_list = None
		# self.enemy_list = None

		# Background image
		self.background = None

		# How far this world has been scrolled left/right
		self.world_shift = 0
		self.level_limit = -1000
		self.platform_list = pygame.sprite.Group()
		# self.enemy_list = pygame.sprite.Group()
		self.player = player

	# Update everythign on this level
	def update(self):
		""" Update everything in this level."""
		self.platform_list.update()

	def draw(self, screen):
		""" Draw everything on this level. """

		screen.fill(constants.BLUE)
		screen.blit(self.background,(self.world_shift // 3,0))

		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)

	def shift_world(self, shift_x):
		""" When the user moves left/right and we need to scroll everything: """

		# Keep track of the shift amount
		self.world_shift += shift_x

		# Go through all the sprite lists and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x
