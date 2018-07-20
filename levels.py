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
		self.special_enemy_list = None
		self.portal_list = None
		self.death_place_list = None
		self.hiragana_A = None
		self.hiragana_I = None

		# Background image
		self.background = None

		# How far this world has been scrolled left/right
		self.world_shift = 0
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.special_enemy_list = pygame.sprite.Group()
		self.portal_list = pygame.sprite.Group()
		self.death_place_list = pygame.sprite.Group()
		self.hiragana_A = pygame.sprite.Group()
		self.hiragana_I = pygame.sprite.Group()
		self.player = player
		
	# Update everythign on this level
	def update(self):
		""" Update everything in this level."""
		self.platform_list.update()
		self.portal_list.update()
		self.death_place_list.update()
		self.enemy_list.update()
		self.special_enemy_list.update()
		self.hiragana_A.update()
		self.hiragana_I.update()

	def draw(self, screen):
		""" Draw everything on this level. """

		screen.blit(self.background,(self.world_shift // 3,0))

		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)
		self.portal_list.draw(screen)
		self.death_place_list.draw(screen)
		self.enemy_list.draw(screen)
		self.special_enemy_list.draw(screen)
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
		
		for platform in self.death_place_list:
			platform.rect.x += shift_x

		for platform in self.hiragana_A:
			platform.rect.x += shift_x
		
		for platform in self.hiragana_I:
			platform.rect.x += shift_x
		
		for platform in self.enemy_list:
			platform.rect.x += shift_x
		
		for platform in self.special_enemy_list:
			platform.rect.x += shift_x




# Create platforms for intro game
# for intro how to play the game
class Level_Tutorial(Level):
	""" This class for introduce the player """

	def __init__(self, player):
		""" Create intro """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("spritesheet/intro_background.png").convert_alpha()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = 165

		intro = [[platforms.snow_dirt_wall, -140, 0],
			[platforms.snow_dirt_intro, 0 , 460],
			[platforms.snow_dirt_big_wall, 769, 0]]
		
		portal = [[platforms.portal_snow, 700, 380]]

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


# Create platforms for the level
# Level 01
class Level_01(Level):
	""" Definition for level 1. """

	def __init__(self, player):
		""" Create Level 1 """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("spritesheet/day_background.png").convert_alpha()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -1166

			
		# Array with type of platform, and x, y location of the platform.
		# for level 01
		level01 = [[platforms.dirt_wall, -140, 0],
				[platforms.dirt_medium_long_land, 0, 460],
				[platforms.dirt_medium_long_land, 700, 460],
				[platforms.dirt_medium_short_land, 770, 196],
				[platforms.dirt_short_land, 1330, 460],
				[platforms.dirt_grass_rounded, 1146, 319],
				[platforms.dirt_medium_short_land, 1218, 125],
				[platforms.dirt_medium_long_land, 1680, 460],
				[platforms.dirt_big_wall, 2100, 0]]
		
		water_level01 = [[platforms.medium_long_water, 490, 531],
						[platforms.medium_short_water, 1190, 531],
						[platforms.medium_long_water, 1470, 531]]
		
		portal = [[platforms.portal_snow, 2030, 380]]
		
		"""hiragana_a = [[platforms.hiragana_a, 200, 200]]
		hiragana_i = [[platforms.hiragana_i, 400, 200]]

		enemy_skull = [[platforms.skull_ghost, 300, 400]]

		# for prototye special enemy
		fat_frog = [[platforms.fat_frog, 600, 400]]"""

		

		for platform in level01:
			block = platforms.Platform_dirt(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
		

		for platform in water_level01:
			water_suicide = platforms.Platform_dirt(platform[0])
			water_suicide.rect.x = platform[1]
			water_suicide.rect.y = platform[2]
			water_suicide.player = self.player
			self.death_place_list.add(water_suicide)
		

		for platform in portal:
			gate = platforms.Platform_snow(platform[0])
			gate.rect.x = platform[1]
			gate.rect.y = platform[2]
			gate.player = self.player
			self.portal_list.add(gate)

		
		
		"""for platform in hiragana_a :
			true_point = platforms.Platform_hiragana_katakana(platform[0])
			true_point.rect.x = platform[1]
			true_point.rect.y = platform[2]
			true_point.player = self.player
			self.hiragana_A.add(true_point)
		
		for platform in hiragana_i :
			false_point = platforms.Platform_hiragana_katakana(platform[0])
			false_point.rect.x = platform[1]
			false_point.rect.y = platform[2]
			false_point.player = self.player
			self.hiragana_I.add(false_point)
		
		for platform in enemy_skull:
			eaten = platforms.Platform_enemy(platform[0])
			eaten.rect.x = platform[1]
			eaten.rect.y = platform[2]
			eaten.player = self.player
			self.enemy_list.add(eaten)
		
		# for prototype
		for platform in fat_frog:
			special_eaten_A = platforms.Platform_enemy(platform[0])
			special_eaten_A.rect.x = platform[1]
			special_eaten_A.rect.y = platform[2]
			special_eaten_A.player = self.player
			self.special_enemy_list.add(special_eaten_A)

		# add moving sprites using platform algorithmic
		eaten = platforms.MovingPlatform(platforms.skull_ghost)
		eaten.rect.x = 400
		eaten.rect.y = 400
		eaten.boundary_left = 100
		eaten.boundary_right = 550
		eaten.change_x = 5
		eaten.player = self.player
		eaten.level = self
		self.enemy_list.add(eaten)"""


# Level 02
class Level_02(Level):
	
	def __init__(self, player):
		""" Create Level 1 """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("spritesheet/night_background.png").convert_alpha()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -1700


		# Array with type of platform, and x, y location of the platform.
		# for level 02
		level02 = [[platforms.brick_dark_wall, -140, 0],
				[platforms.brick_medium_short_land, 0, 529],
				[platforms.brick_medium_large_land, 0, 141],
				[platforms.brick_dark_small_stairs1, 281, 459],
				[platforms.brick_dark_small_stairs2, 351, 389],
				[platforms.brick_dark_small_stairs3, 421, 319],
				[platforms.brick_dark_grass_rounded, 281, 214],
				[platforms.brick_small_short_land, 642, 102],
				[platforms.brick_dark_grass_rounded, 713, 384],
				[platforms.brick_medium_long_land, 840, 528],
				[platforms.brick_medium_large_long_land, 869, 272],
				[platforms.brick_half_short_land, 943, 131],
				#[platforms.brick_half_small_land, 1302, 483],
				[platforms.brick_dark_small_stairs1, 1680, 480],
				[platforms.brick_large_high_land, 1750, 410],
				[platforms.brick_dark_big_wall, 2100, 0]]
		
		sharp_rock_level02 = [[platforms.medium_sharp_rock, 490, 540],
							[platforms.small_sharp_rock, 700, 540],
							[platforms.medium_sharp_rock, 1260, 540],
							[platforms.medium_sharp_rock, 1470, 540]]



		for platform in level02:
			block = platforms.Platform_dark_brick(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
		
		for platform in sharp_rock_level02:
			sharp_rock = platforms.Platform_dark_brick(platform[0])
			sharp_rock.rect.x = platform[1]
			sharp_rock.rect.y = platform[2]
			sharp_rock.player = self.player
			self.death_place_list.add(sharp_rock)
		

		# add moving sprites
		block = platforms.MovingPlatform(platforms.brick_half_small_land)
		block.rect.x = 1302
		block.rect.y = 483
		block.boundary_left = 1302
		block.boundary_right = 1600
		block.change_x = 3
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
