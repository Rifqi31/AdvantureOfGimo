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

		def push_tiles_screen(name_tiles):
			for platform in name_tiles:
				block = platforms.Platform(platform[0])
				block.rect.x = platform[1]
				block.rect.y = platform[2]
				block.player = self.player
				self.platform_list.add(block)

		# optimation code fucking this !!!!
		# go mastrubate dude!!!!

		# Array with type of platform, and x, y location of the platform.

		# for base bottom dirt
		for base_dirt in range(0, 390, 70):
			dirt_down = [[platforms.DIRT, base_dirt, 530]]
			push_tiles_screen(dirt_down)

		# for left wall dirt
		for wall_dirt in range(0, 600, 70):
			wall_left = [[platforms.DIRT, 0, wall_dirt], [platforms.DIRT, -70, wall_dirt]]
			push_tiles_screen(wall_left)

		# for grass bottom near left wall
		for grass_dirt_middle in range(70, 350, 70):
			grass_middle = [[platforms.GRASS_MIDDLE, grass_dirt_middle, 460]]
			push_tiles_screen(grass_middle)

		# for long grass corner right
		grass_right = [[platforms.GRASS_RIGHT, 350, 460]]
		push_tiles_screen(grass_right)

		# for top dirt
		for base_up_dirt in range(0, 180, 70):
			dirt_up = [[platforms.DIRT, 70, base_up_dirt], [platforms.DIRT, 140, base_up_dirt]]
			push_tiles_screen(dirt_up)
		
		# for top dirt
		for base_up_dirt2 in range(0, 110, 70):
			dirt_up2 = [[platforms.DIRT, 210, base_up_dirt2], [platforms.DIRT, 280, base_up_dirt2]]
			push_tiles_screen(dirt_up2)
		
		# for top dirt
		dirt_top3 = [[platforms.DIRT, 350, 0]]
		push_tiles_screen(dirt_top3)
		

		# new line dirt
		for short_base_dirt in range(600, 740, 70):
			dirt_down_short = [[platforms.DIRT, short_base_dirt, 530]]
			push_tiles_screen(dirt_down_short)


		# new line dirt
		for long_base_dirt in range(900, 1180, 70):
			dirt_down_long = [[platforms.DIRT, long_base_dirt, 530]]
			push_tiles_screen(dirt_down_long)
		
		
		# for two line up grass
		grass_corner_left = [[platforms.GRASS_LEFT, 600, 460], [platforms.GRASS_LEFT, 900, 460]]
		push_tiles_screen(grass_corner_left)

		grass_corner_right = [[platforms.GRASS_RIGHT, 670, 460], [platforms.GRASS_RIGHT, 970, 460]]
		push_tiles_screen(grass_corner_right)


		for some_dirt in range(1040, 1180, 70):
			dirt_short = [[platforms.DIRT, some_dirt, 460]]
			push_tiles_screen(dirt_short)


		one_grass_middle = [[platforms.GRASS_MIDDLE, 1040, 390]]
		push_tiles_screen(one_grass_middle)

		one_dirt = [[platforms.DIRT, 1110, 390]]
		push_tiles_screen(one_dirt)

		one_grass_right = [[platforms.GRASS_RIGHT, 1110, 320]]
		push_tiles_screen(one_grass_right)

		single_tiles_grass_rounded = [[platforms.GRASS_ROUNDED, 1250, 320], [platforms.GRASS_ROUNDED, 1390, 320]]
		push_tiles_screen(single_tiles_grass_rounded)


		# new line dirt
		for long_end_base_dirt in range(1700, 2050, 70):
			dirt_down_long_end = [[platforms.DIRT, long_end_base_dirt, 530]]
			push_tiles_screen(dirt_down_long_end)
		
		# then the grass
		grass_corner_end = [[platforms.GRASS_LEFT, 1700, 460], [platforms.GRASS_RIGHT, 1980, 460]]
		push_tiles_screen(grass_corner_end)

		for long_grass_end in range(1770, 1980, 70):
			grass_end = [[platforms.GRASS_MIDDLE, long_grass_end, 460]]
			push_tiles_screen(grass_end)

		# for end wall
		for end_wall_down in range(2050, 2400, 70):
			wall_dirt_end_down = [[platforms.DIRT, end_wall_down, 530], 
								[platforms.DIRT, end_wall_down, 460],
								[platforms.DIRT, end_wall_down, 390]]
			push_tiles_screen(wall_dirt_end_down)
		
		# wall
		for tall_wall_end in range(-30, 390, 70):
			wall_right_corner = [[platforms.DIRT, 2050, tall_wall_end],
								[platforms.DIRT, 2120,  tall_wall_end],
								[platforms.DIRT, 2190, tall_wall_end],
								[platforms.DIRT, 2260, tall_wall_end],
								[platforms.DIRT, 2330, tall_wall_end]]
			push_tiles_screen(wall_right_corner)

