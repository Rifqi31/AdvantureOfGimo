# name file: levels.py
# python version 3

import pygame

import constants
import platforms
import platform_scroller

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

# Create platforms for the level
class Level_01(Level):
	""" Definition for level 1. """

	def __init__(self, player):
		""" Create Level 1 """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("spritesheet/day_background.png").convert_alpha()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -2500

		# Array with type of platform, and x, y location of the platform.
		level = [[platforms.DIRT, 0, 530],
				[platforms.DIRT, 70, 530],
				[platforms.DIRT, 140, 530],
				[platforms.DIRT, 210, 530],
				[platforms.DIRT, 280, 530],
				[platforms.DIRT, 350, 530],
				# for dirty wall
				[platforms.DIRT, -70, 530],
				[platforms.DIRT, -70, 460],
				[platforms.DIRT, -70, 390],
				[platforms.DIRT, -70, 320],
				[platforms.DIRT, -70, 250],
				[platforms.DIRT, -70, 180],
				[platforms.DIRT, -70, 110],
				[platforms.DIRT, -70, 40],
				[platforms.DIRT, -70, -30],
				# for wall dirt grassy
				[platforms.GRASS_LEFT_RIGHT, 0, 390],
				[platforms.GRASS_LEFT_RIGHT, 0, 320],
				[platforms.GRASS_LEFT_RIGHT, 0, 250],
				[platforms.GRASS_LEFT_RIGHT, 0, 180],
				# for dirt up wall
				[platforms.DIRT, 0, 110],
				[platforms.DIRT, 0, 40],
				# [platforms.DIRT_HALF, 0, 0],
				[platforms.DIRT, 0, -30],
				[platforms.DIRT, 70, 110],
				[platforms.DIRT, 70, 40],
				# [platforms.DIRT_HALF, 70, 0],
				[platforms.DIRT, 70, -30],
				[platforms.DIRT, 140, 110],
				[platforms.DIRT, 140, 40],
				# [platforms.DIRT_HALF, 140, 0],
				[platforms.DIRT, 140, -30],
				[platforms.DIRT, 210, 40],
				[platforms.DIRT, 210, -30],
				# [platforms.DIRT_HALF, 210, 0],
				# new line up platforms
				[platforms.DIRT, 0, 460],
				[platforms.GRASS_MIDDLE, 70, 460],
				[platforms.GRASS_MIDDLE, 140, 460],
				[platforms.GRASS_MIDDLE, 210, 460],
				[platforms.GRASS_MIDDLE, 280, 460],
				[platforms.GRASS_MIDDLE, 350, 460],
				# new line bottom platforms
				[platforms.DIRT, 600, 530],
				[platforms.DIRT, 670, 530],
				[platforms.GRASS_LEFT, 600, 460],
				[platforms.GRASS_RIGHT, 670, 460],
				# new line bottom platforms
				[platforms.DIRT, 900, 530],
				[platforms.DIRT, 970, 530],
				[platforms.DIRT, 1040, 530],
				[platforms.DIRT, 1110, 530],
				[platforms.DIRT, 1040, 460],
				[platforms.DIRT, 1110, 460],
				[platforms.DIRT, 1110, 390],
				[platforms.GRASS_LEFT, 900, 460],
				[platforms.GRASS_MIDDLE, 970, 460],
				[platforms.GRASS_MIDDLE, 1040, 390],
				[platforms.GRASS_RIGHT, 1110, 320],
				# new flying dirt grass
				[platforms.GRASS_ROUNDED, 1250, 320],
				[platforms.GRASS_ROUNDED, 1390, 320],
				# new line platform]
				[platforms.DIRT,  1700, 530],
				[platforms.DIRT, 1770, 530],
				[platforms.DIRT, 1840, 530],
				[platforms.DIRT, 1910, 530],
				[platforms.DIRT, 1980, 530],
				[platforms.GRASS_LEFT, 1700, 460],
				[platforms.GRASS_MIDDLE, 1770, 460],
				[platforms.GRASS_MIDDLE, 1840, 460],
				[platforms.GRASS_MIDDLE, 1910, 460],
				[platforms.GRASS_RIGHT, 1980, 460]]


		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)

