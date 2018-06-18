# name file: levels.py
# python version 3

import pygame

import constant
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
		self.enemy_list = pygame.sprite.Group()
		self.player = player

	# Update everythign on this level
	def update(self):
		""" Update everything in this level."""
		self.platform_list.update()

	def draw(self, screen):
		""" Draw everything on this level. """

		screen.fill(constant.BLUE)
		screen.blit(self.background,(self.world_shift // 0,3))

		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)

	def shift_world(self, shift_x):
		""" When the user moves left/right and we need to scroll everything: """

		# Keep track of the shift amount
		self.world_shift += shift_x

		# Go through all the sprite lists and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
	""" Definition for level 1. """

	def __init__(self, player):
		""" Create Level 1 """

		# Call the parent constructor
		Level.__init__(self, player)

		# self.background = pygame.image.load("background_01.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -2500

		# Array with type of platform, and x, y location of the platform.
		level = [[platform.GRASS_MIDDLE, 500, 500]]

		for platform in level:
			block = platfrom.Platforms(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)

