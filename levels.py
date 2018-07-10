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
		self.enemy_list = None
		self.portal_list = None
		self.hiragana_A = None
		self.hiragana_I = None

		# Background image
		self.background = None

		# How far this world has been scrolled left/right
		self.world_shift = 0
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.portal_list = pygame.sprite.Group()
		self.hiragana_A = pygame.sprite.Group()
		self.hiragana_I = pygame.sprite.Group()
		self.player = player

	# Update everythign on this level
	def update(self):
		""" Update everything in this level."""
		self.platform_list.update()
		self.portal_list.update()
		self.enemy_list.update()
		self.hiragana_A.update()
		self.hiragana_I.update()

	def draw(self, screen):
		""" Draw everything on this level. """

		screen.blit(self.background,(self.world_shift // 3,0))

		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)
		self.portal_list.draw(screen)
		self.enemy_list.draw(screen)
		self.hiragana_A.draw(screen)
		self.hiragana_I.draw(screen)

	def shift_world(self, shift_x):
		""" When the user moves left/right and we need to scroll everything: """

		# Keep track of the shift amount
		self.world_shift += shift_x

		# Go through all the sprite lists and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x
		
		for platform in self.portal_list:
			platform.rect.x += shift_x

		for platform in self.hiragana_A:
			platform.rect.x += shift_x
		
		for platform in self.hiragana_I:
			platform.rect.x += shift_x
		
		for platform in self.enemy_list:
			platform.rect.x += shift_x



# Create platforms for intro game
# for intro how to play the game
class Level_01(Level):
	""" This class for introduce the player """

	def __init__(self, player):
		""" Create intro """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("spritesheet/intro_background.png").convert_alpha()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -10

		intro = [[platforms.snow_dirt_wall, -140, 0],
			[platforms.snow_dirt_intro, 0 , 460],
			[platforms.snow_dirt_big_wall, 769, 0]]
		
		portal = [[platforms.portal_snow, 670, 380]]

		for platform in intro:
			block = platforms.Platform_snow(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
		
		for platform in portal:
			gate = platforms.Platform_snow(platform[0])
			gate.rect.x = platform[1]
			gate.rect.y = platform[2]
			gate.player = self.player
			self.portal_list.add(gate)


# this level 2 for prototype
# Create platforms for the level
class Level_02(Level):
	""" Definition for level 1. """

	def __init__(self, player):
		""" Create Level 1 """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("spritesheet/day_background.png").convert_alpha()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -1700

			
		# Array with type of platform, and x, y location of the platform.
		# for level 01
		level01 = [[platforms.dirt_wall, -140, 0],
				[platforms.dirt_land_bottom, 0, 460],
				[platforms.dirt_small, 670, 460],
				[platforms.dirt_half_grass, 1110, 460],
				[platforms.dirt_small_half_grass, 1250, 390],
				[platforms.one_dirt, 1320, 320],
				[platforms.dirt_rounded, 1460, 320],
				[platforms.dirt_rounded, 1600, 320],
				[platforms.dirt_land_bottom, 1980, 460],
				[platforms.dirt_big_wall, 2480, 0]]
		
		
		hiragana_a = [[platforms.hiragana_a, 200, 200]]
		hiragana_i = [[platforms.hiragana_i, 400, 200]]

		enemy_skull = [[platforms.skull_ghost, 200, 400]]
		

		for platform in level01:
			block = platforms.Platform_dirt(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
		
		for platform in hiragana_a :
			point = platforms.Platform_hiragana_katakana(platform[0])
			point.rect.x = platform[1]
			point.rect.y = platform[2]
			point.player = self.player
			self.hiragana_A.add(point)
		
		for platform in hiragana_i :
			point = platforms.Platform_hiragana_katakana(platform[0])
			point.rect.x = platform[1]
			point.rect.y = platform[2]
			point.player = self.player
			self.hiragana_I.add(point)
		



		for platform in enemy_skull:
			eaten = platforms.Platform_enemy(platform[0])
			eaten.rect.x = platform[1]
			eaten.rect.y = platform[2]
			eaten.player = self.player
			self.enemy_list.add(eaten)



		# add moving sprites using platform algorithmic
		eaten = platforms.MovingPlatform(platforms.skull_ghost)
		eaten.rect.x = 400
		eaten.rect.y = 400
		eaten.boundary_left = 100
		eaten.boundary_right = 550
		eaten.change_x = 5
		eaten.player = self.player
		eaten.level = self
		self.enemy_list.add(eaten)


