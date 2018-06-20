# name file : levels01.py
# python version 3

import pygame

import constants
import platforms
import levels

# Create platforms for the level
class Level_01(levels.Level):
	""" Definition for level 1. """

	def __init__(self, player):
		""" Create Level 1 """

		# Call the parent constructor
		levels.Level.__init__(self, player)

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
				[platforms.DIRT, 0, 390],
				[platforms.DIRT, 0, 320],
				[platforms.DIRT, 0, 250],
				[platforms.DIRT, 0, 180],
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
				[platforms.GRASS_RIGHT, 1980, 460],
				# end wall
				[platforms.DIRT, 2050, 530],
				[platforms.DIRT, 2120, 530],
				[platforms.DIRT, 2190, 530],
				[platforms.DIRT, 2260, 530],
				[platforms.DIRT, 2330, 530],
				[platforms.DIRT, 2050, 460],
				[platforms.DIRT, 2120, 460],
				[platforms.DIRT, 2190, 460],
				[platforms.DIRT, 2260, 460],
				[platforms.DIRT, 2330, 460],
				# ---
				[platforms.DIRT, 2050, 390],
				[platforms.DIRT, 2120, 390],
				[platforms.DIRT, 2190, 390],
				[platforms.DIRT, 2260, 390],
				[platforms.DIRT, 2330, 390],
				# wall
				[platforms.DIRT, 2050, 320],
				[platforms.DIRT, 2050, 250],
				[platforms.DIRT, 2050, 180],
				[platforms.DIRT, 2050, 110],
				[platforms.DIRT, 2050, 40],
				[platforms.DIRT, 2050, -30],
				# --
				[platforms.DIRT, 2120, 320],
				[platforms.DIRT, 2120, 250],
				[platforms.DIRT, 2120, 180],
				[platforms.DIRT, 2120, 110],
				[platforms.DIRT, 2120, 40],
				[platforms.DIRT, 2120, -30],
				# --
				[platforms.DIRT, 2190, 320],
				[platforms.DIRT, 2190, 250],
				[platforms.DIRT, 2190, 180],
				[platforms.DIRT, 2190, 110],
				[platforms.DIRT, 2190, 40],
				[platforms.DIRT, 2190, -30],
				# --
				[platforms.DIRT, 2260, 320],
				[platforms.DIRT, 2260, 250],
				[platforms.DIRT, 2260, 180],
				[platforms.DIRT, 2260, 110],
				[platforms.DIRT, 2260, 40],
				[platforms.DIRT, 2260, -30],
				# --
				[platforms.DIRT, 2330, 320],
				[platforms.DIRT, 2330, 250],
				[platforms.DIRT, 2330, 180],
				[platforms.DIRT, 2330, 110],
				[platforms.DIRT, 2330, 40],
				[platforms.DIRT, 2330, -30],]


		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
