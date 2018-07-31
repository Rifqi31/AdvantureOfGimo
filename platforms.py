# name file : platforms.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

import gameoverscreen

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

# asset for tileset Intro Game and level 05
# for snow dirt
snow_dirt_wall = (770, 162, 140, 630)
snow_dirt_big_wall = (325, 162, 350, 630)
snow_dirt_intro = (0, 0, 770, 140)
snow_dirt_half = (231, 162, 70, 38)
snow_dirt_grass_basic = (231, 203, 70, 70)
snow_dirt_grass_rounded = (155, 162, 70, 70)
snow_dirt_tall_grass_left_right = (0, 308, 70, 350)
snow_dirt_grass_medium_tall = (75, 308, 70, 280)
snow_dirt_grass_short_tall = (155, 238, 70, 210)
snow_dirt_grass_medium_large = (0, 676, 280, 140)
snow_dirt_grass_up_down = (0, 829, 210, 70)
snow_dirt_grass_small_large = (0, 162, 140, 140)

# portal
portal_snow = (219, 511, 70, 70)

# asset for tileset level 01
dirt_wall = (0, 0, 140, 630)
dirt_big_wall = (584, 149, 350, 630)
dirt_medium_long_land = (0, 777, 490, 140)
dirt_medium_short_land = (148, 0, 280, 140)
dirt_short_land = (445, 0, 140, 140)
dirt_grass_rounded = (744, 73, 70, 70)
dirt_medium_long_top = (0, 692, 490, 70)
dirt_large_land = (148, 149, 420, 280)
# death sprite
small_water = (591, 0, 70, 70)
medium_short_water = (592, 73, 140, 70)
medium_long_water = (665, 0, 210, 70)


# asset for tileset level 02
brick_dark_wall = (0, 0, 140, 630)
brick_dark_big_wall = (374, 230, 280, 630)
brick_medium_short_land = (148, 0, 280, 70)
brick_medium_large_land = (146, 80, 210, 140)
brick_medium_long_land = (440, 0, 420, 70)
brick_medium_large_long_land = (368, 80, 280, 140)
brick_small_short_land = (224, 528, 140, 70)
brick_half_short_land = (662, 80, 140, 43)
brick_half_small_land = (815, 80, 70, 43)
brick_dark_grass_rounded = (146, 528, 70, 70)
brick_dark_small_stairs1 = (146, 374, 70, 140)
brick_dark_small_stairs2 = (218, 302, 70, 210)
brick_dark_small_stairs3 = (290, 230, 70, 280)
brick_large_high_land = (0, 687, 350, 210)
# death sprite
medium_sharp_rock = (662, 126, 210, 70)
small_sharp_rock = (667, 188, 140, 70)


# asset for tileset level 03 and level 04
brick_red_wall = (0, 0, 140, 630)
brick_red_big_wall = (625, 0, 280, 630)
brick_red_medium_tall = (147, 0, 140, 210)
brick_red_medium_short_land = (294, 0, 140, 70)
brick_red_medium_long_land = (294, 76, 280, 70)
brick_red_small_half = (521, 0, 70, 45)
brick_red_snow_small_half = (441, 151, 72, 45)
brick_red_grass_left_right_long = (147, 221, 70, 420)
brick_red_medium_high_land = (221, 221, 70, 140)
brick_red_medium_high_large_land = (297, 226, 210, 140)
brick_red_snow_medium_short_land = (297, 373, 210, 70)
brick_red_snow_high_small_left_right = (219, 515, 74, 144)
brick_red_snow_medium_short_land = (0, 675, 280, 70)
brick_red_medium_bottom = (0, 749, 280, 70)
brick_red_medium_short_grass_snow = (0, 823, 210, 70)
brick_basic = (219, 824, 70, 70)
brick_red_grass_snow_medium_land = (626, 675, 280, 70)
brick_red_grass_rounded = (443, 0, 70, 70)


# asset for tileset level 06
sand_dirt_wall = (0, 0, 140, 630)
sand_dirt_medium_long_land = (146, 0, 350, 140)
sand_dirt_tall_small = (512, 0, 70, 210)
sand_dirt_tall_large_medium = (146, 147, 140, 210)
sand_dirt_half = (295, 147, 72, 34)
sand_dirt_tall_long = (434, 147, 70, 350)
sand_dirt_tall_medium = (512, 221, 70, 280)
sand_dirt_basic_medium = (145, 584, 140, 70)
sand_dirt_long_soft_up_down = (0, 676, 560, 70)
sand_dirt_medium_small_land = (0 ,751, 280, 140) 
sand_dirt_big_wall = (626, 0, 280, 630)


# asset for tileset level 07
ancient_brick_wall = (0, 0, 140, 630)
ancient_brick_short_land = (366, 147, 140, 70)
ancient_brick_tall_large_long = (146, 0, 210, 70)
ancient_brick_tall_large_medium = (366, 0, 140, 140)
ancient_brick_half = (514, 0, 72, 40)
ancient_brick_long_tall_sand_left_right = (146, 146, 70, 420)
ancient_brick_medium_sand_top_down = (219, 146, 140, 70)
ancient_brick_short_tall_sand_left_right = (219, 220, 70, 210)
ancient_brick_basic = (292, 220, 70, 70)
ancient_brick_tall_large_small = (219, 438, 70, 210)
ancient_brick_big_wall = (626, 0, 280, 630)

# asset for tileset level 08
lava_rock_wall = (0, 0, 140, 630)
lava_rock_small_tall = (145, 362, 70, 210)
lava_rock_medium_tall = (145, 0, 70, 350)
lava_rock_long_tall = (218, 0, 70, 490)
lava_rock_medium_large_land = (292, 0, 280, 210)
lava_rock_short_small_land = (292, 219, 210, 140)
lava_rock_tall_small_land = (292, 366, 210, 210)
lava_rock_basic = (145, 583, 70, 70)
lava_rock_basic_medium = (292, 586, 140, 70)
lava_rock_half = (439, 586, 72, 38)
lava_water = (511, 219, 72, 70)
lava_water_long = (0, 676, 216, 70)
lava_water_medium = (221, 676, 144, 70)
lava_rock_big_wall = (626, 0, 280, 630) 


# for hiragana & katakana
# hiragana symbol
# vocal
hiragana_a = (0, 0, 70, 70)
hiragana_i = (0, 72, 70, 70)
hiragana_u = (0, 146, 70, 70)
hiragana_e = (0, 219, 70, 70)
hiragana_o = (0, 292, 70, 70)

# vocal K
hiragana_ka = (73, 0, 70, 70)
hiragana_ki = (73, 73, 70, 70)
hiragana_ku = (73, 146, 70, 70)
hiragana_ke = (73, 219, 70, 70)
hiragana_ko = (73, 292, 70, 70)

# vocal S
hiragana_sa = (146, 0, 70, 70)
hiragana_si = (146, 73, 70, 70)
hiragana_su = (146, 146, 70, 70)
hiragana_se = (146, 219, 70, 70)
hiragana_so = (146, 292, 70, 70)

# vocal T
hiragana_ta = (219, 0, 70, 70)
hiragana_ti = (219, 73, 70, 70)
hiragana_tu = (219, 146, 70, 70)
hiragana_te = (219, 219, 70, 70)
hiragana_to = (219, 292, 70, 70)

# vocal N
hiragana_na = (292, 0, 70, 70)
hiragana_ni = (292, 73, 70, 70)
hiragana_nu = (292, 146, 70, 70)
hiragana_ne = (292, 219, 70, 70)
hiragana_no = (292, 292, 70, 70)

# vocal H
hiragana_ha = (365, 0, 70, 70)
hiragana_hi = (365, 73, 70, 70)
hiragana_hu = (365, 146, 70, 70)
hiragana_he = (365, 219, 70, 70)
hiragana_ho = (365, 292, 70, 70)

# vocal M
hiragana_ma = (438, 0, 70, 70)
hiragana_mi = (438, 73, 70, 70)
hiragana_mu = (438, 146, 70, 70)
hiragana_me = (438, 219, 70, 70)
hiragana_mo = (438, 292, 70, 70)

# vocal Y
hiragana_ya = (511, 0, 70, 70)
hiragana_yu = (511, 73, 70, 70)
hiragana_yo = (511, 146, 70, 70)

# vocal R
hiragana_ra = (584, 0, 70, 70)
hiragana_ri = (584, 73, 70, 70)
hiragana_ru = (584, 146, 70, 70)
hiragana_re = (584, 219, 70, 70)
hiragana_ro = (584, 292, 70, 70)

# vocal W
hiragana_wa = (657, 0, 70, 70)
hiragana_wo = (657, 73, 70, 70)

# vocal N
hiragana_n = (730, 0, 70, 70)


# Katakana Symbol
katakana_a = (0, 438, 70, 70)
katakana_i = (0, 511, 70, 70)
katakana_u = (0, 584, 70, 70)
katakana_e = (0, 657, 70, 70)
katakana_o = (0, 730, 70, 70)

# vocal K
katakana_ka = (73, 438, 70, 70)
katakana_ki = (73, 511, 70, 70)
katakana_ku = (73, 584, 70, 70)
katakana_ke = (73, 657, 70, 70)
katakana_ko = (73, 730, 70, 70)

# vocal S
katakana_sa = (146, 438, 70, 70)
katakana_si = (146, 511, 70, 70)
katakana_su = (146, 584, 70, 70)
katakana_se = (146, 657, 70, 70)
katakana_so = (146, 730, 70, 70)

# vocal T
katakana_ta = (219, 438, 70, 70)
katakana_ti = (219, 511, 70, 70)
katakana_tu = (219, 584, 70, 70)
katakana_te = (219, 657, 70, 70)
katakana_to = (219, 730, 70, 70)

# vocal N
katakana_na = (292, 438, 70, 70)
katakana_ni = (292, 511, 70, 70)
katakana_nu = (292, 584, 70, 70)
katakana_ne = (292, 657, 70, 70)
katakana_no = (292, 730, 70, 70)

# vocal H
katakana_ha = (365, 438, 70, 70)
katakana_hi = (365, 511, 70, 70)
katakana_hu = (365, 484, 70, 70)
katakana_he = (365, 657, 70, 70)
katakana_ho = (365, 730, 70, 70)

# vocal M
katakana_ma = (438, 438, 70, 70)
katakana_mi = (438, 511, 70, 70)
katakana_mu = (438, 484, 70, 70)
katakana_me = (438, 657, 70, 70)
katakana_mo = (438, 730, 70, 70)

# vocal Y
katakana_ya = (584, 438, 70, 70)
katakana_yu = (584, 511, 70, 70)
katakana_yo = (584, 484, 70, 70)

# vocal R
katakana_ra = (511, 438, 70, 70)
katakana_ri = (511, 511, 70, 70)
katakana_ru = (511, 484, 70, 70)
katakana_re = (511, 657, 70, 70)
katakana_ro = (511, 730, 70, 70)

# vocal W
katakana_wa = (657, 438, 70, 70)
katakana_wo = (657, 511, 70, 70)

# vocal N
katakana_Na = (730, 438, 70, 70)


# for enemys
skull_ghost = (10, 5, 42, 51)
fat_frog = (62, 7, 49, 49)
old_skull = (122, 7, 31, 49)
dark_bat = (158, 8, 57, 48)
orange_slime = (14, 60, 33, 33)
bad_mushroom = (65, 60, 42, 42)
bad_octo = (122, 60, 31, 33)
bad_ogre = (167, 60, 39, 42)

# special enemys
# basic vokal
big_ogre_a = (5, 5, 65, 109)
big_ogre_i = (79, 5, 65, 109)
big_ogre_u = (152, 5, 65, 109)
big_ogre_e = (225, 5, 65, 109)
big_ogre_o = (301, 5, 65, 109)

# Vocal K
dark_rabbit_ka = (5, 117, 71, 108)
dark_rabbit_ki = (79, 117, 71, 108)
dark_rabbit_ku = (152, 117, 71, 108)
dark_rabbit_ke = (225, 117, 71, 108)
dark_rabbit_ko = (301, 117, 71, 108)

# Vocal S
orange_slime_sa = (5, 234, 80, 99)
orange_slime_si = (88, 234, 80, 99)
orange_slime_su = (170, 234, 80, 99)
orange_slime_se = (254, 234, 80, 99)
orange_slime_so = (336, 234, 80, 99)

# vocal T
big_ogre_ta = (380, 5, 65, 109)
big_ogre_ti = (452, 5, 65, 109)
big_ogre_tu = (523, 5, 65, 109)
big_ogre_te = (596, 5, 65, 109)
big_ogre_to = (670, 5, 65, 109)

# Vocal N
dark_rabbit_na = (380, 117, 71, 108)
dark_rabbit_ni = (452, 117, 71, 108)
dark_rabbit_nu = (523, 117, 71, 108)
dark_rabbit_ne = (596, 117, 71, 108)
dark_rabbit_no = (670, 117, 71, 108)

# Vocal H
orange_slime_ha = (420, 234, 80, 99)
orange_slime_hi = (504, 234, 80, 99)
orange_slime_hu = (588, 234, 80, 99)
orange_slime_he = (674, 234, 80, 99)
orange_slime_ho = (758, 234, 80, 99)

# Vocal M
zombie_skull_ma = (5, 348, 65, 96)
zombie_skull_mi = (79, 348, 65, 96)
zombie_skull_mu = (152, 348, 65, 96)
zombie_skull_me = (223, 348, 65, 96)
zombie_skull_mo = (297, 348, 65, 96)

# Vocal Yo
zombie_skull_ya = (372, 348, 65, 96)
zombie_skull_yu = (445, 348, 65, 96)
zombie_skull_yo = (517, 348, 65, 96)

# Vocal R
slime_lava_ra = (5, 456, 80, 99)
slime_lava_ri = (91, 456, 80, 99)
slime_lava_ru = (176, 456, 80, 99)
slime_lava_re = (260, 456, 80, 99)
slime_lava_ro = (344, 456, 80, 99)

# Vocal W
slime_lava_wa = (430, 456, 80, 99)
slime_lava_wo = (517, 456, 80, 99)

# Vocal N
slime_lava_n = (603, 456, 80, 99)



class Platform_enemy(pygame.sprite.Sprite):
	""" Platform for enemy """
	
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			 an array of 5 numbers like what's defined at the top of this
			code. """
		
		super().__init__()

		# enemy tileset
		sprite_sheet_enemys = SpriteSheet("spritesheet/enemy.png")

		# Grab the image for this platform
		self.image = sprite_sheet_enemys.get_image(sprite_sheet_data[0],
												sprite_sheet_data[1],
												sprite_sheet_data[2],
												sprite_sheet_data[3])
		
		self.rect = self.image.get_rect()


class Platform_special_enemy(pygame.sprite.Sprite):
	""" Platform for enemy """
	
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			 an array of 5 numbers like what's defined at the top of this
			code. """
		
		super().__init__()

		# enemy tileset
		sprite_sheet_enemys = SpriteSheet("spritesheet/special_enemy_characters.png")

		# Grab the image for this platform
		self.image = sprite_sheet_enemys.get_image(sprite_sheet_data[0],
												sprite_sheet_data[1],
												sprite_sheet_data[2],
												sprite_sheet_data[3])
		
		self.rect = self.image.get_rect()


class Platform_hiragana_katakana(pygame.sprite.Sprite):
	""" Platform the user can take the point """
	
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()

		# hiragana&katakana tileset
		sprite_sheet_wibu = SpriteSheet("spritesheet/hiragana_katakana_tileset.png")

		# Grab the image for this platform
		self.image = sprite_sheet_wibu.get_image(sprite_sheet_data[0],
												sprite_sheet_data[1],
												sprite_sheet_data[2],
												sprite_sheet_data[3])
		
		self.rect = self.image.get_rect()


class Platform_snow(pygame.sprite.Sprite):
	""" Platform the user can jump on """
 
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()
		
		# dirt tileset
		sprite_sheet_dirt = SpriteSheet("spritesheet/snow_tile_assets.png")
		
		# Grab the image for this platform
		self.image = sprite_sheet_dirt.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])
			
		self.rect = self.image.get_rect()


class Platform_dirt(pygame.sprite.Sprite):
	""" Platform the user can jump on """
 
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()
		
		# dirt tileset
		sprite_sheet_dirt = SpriteSheet("spritesheet/dirt_tile_assets.png")
		
		# Grab the image for this platform
		self.image = sprite_sheet_dirt.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])
			
		self.rect = self.image.get_rect()


class Platform_dark_brick(pygame.sprite.Sprite):
	""" Platform the user can jump on """
 
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()
		
		# dirt tileset
		sprite_sheet_dirt = SpriteSheet("spritesheet/brick_castle_night.png")
		
		# Grab the image for this platform
		self.image = sprite_sheet_dirt.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])
			
		self.rect = self.image.get_rect()


class Platform_grass_brick(pygame.sprite.Sprite):
	""" Platform the user can jump on """

	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()

		# brick grass tileset
		sprite_sheet_red_brick = SpriteSheet("spritesheet/brick_red_castle.png")

		# Grab the omage for this platform
		self.image = sprite_sheet_red_brick.get_image(sprite_sheet_data[0],
													sprite_sheet_data[1],
													sprite_sheet_data[2],
													sprite_sheet_data[3])

		self.rect = self.image.get_rect()


class Platform_dirt_sand(pygame.sprite.Sprite):
	""" Platform the user can jump on """

	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()

		# brick grass tileset
		sprite_sheet_red_brick = SpriteSheet("spritesheet/sand_tiles_assets.png")

		# Grab the omage for this platform
		self.image = sprite_sheet_red_brick.get_image(sprite_sheet_data[0],
													sprite_sheet_data[1],
													sprite_sheet_data[2],
													sprite_sheet_data[3])

		self.rect = self.image.get_rect()


class Platform_ancient_brick(pygame.sprite.Sprite):
	""" Platform the user can jump on """

	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()

		# brick grass tileset
		sprite_sheet_red_brick = SpriteSheet("spritesheet/ancient_brick_tile_assets.png")

		# Grab the omage for this platform
		self.image = sprite_sheet_red_brick.get_image(sprite_sheet_data[0],
													sprite_sheet_data[1],
													sprite_sheet_data[2],
													sprite_sheet_data[3])

		self.rect = self.image.get_rect()


class Platform_lava_rock(pygame.sprite.Sprite):
	""" Platform the user can jump on """

	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """

		super().__init__()

		# brick grass tileset
		sprite_sheet_red_brick = SpriteSheet("spritesheet/lava_tile_assets.png")

		# Grab the omage for this platform
		self.image = sprite_sheet_red_brick.get_image(sprite_sheet_data[0],
													sprite_sheet_data[1],
													sprite_sheet_data[2],
													sprite_sheet_data[3])

		self.rect = self.image.get_rect()



class MovingPlatform(Platform_dark_brick):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
		""" Move the platform.
			If the player is in the way, it will shove the player
			out of the way. This does NOT handle what happens if a
			platform shoves a player into another object. Make sure
			moving platforms have clearance to push the player around
			or add code to handle what happens if they don't. """
 
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1


class MovingPlatform_brick_red(Platform_grass_brick):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
		""" Move the platform.
			If the player is in the way, it will shove the player
			out of the way. This does NOT handle what happens if a
			platform shoves a player into another object. Make sure
			moving platforms have clearance to push the player around
			or add code to handle what happens if they don't. """
 
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1



class MovingPlatform_snow(Platform_snow):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
		""" Move the platform.
			If the player is in the way, it will shove the player
			out of the way. This does NOT handle what happens if a
			platform shoves a player into another object. Make sure
			moving platforms have clearance to push the player around
			or add code to handle what happens if they don't. """
 
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1



class MovingPlatform_dirt_sand(Platform_dirt_sand):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
		""" Move the platform.
			If the player is in the way, it will shove the player
			out of the way. This does NOT handle what happens if a
			platform shoves a player into another object. Make sure
			moving platforms have clearance to push the player around
			or add code to handle what happens if they don't. """
 
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1



class MovingPlatform_ancient_brick(Platform_ancient_brick):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
		""" Move the platform.
			If the player is in the way, it will shove the player
			out of the way. This does NOT handle what happens if a
			platform shoves a player into another object. Make sure
			moving platforms have clearance to push the player around
			or add code to handle what happens if they don't. """
 
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1



class MovingPlatform_lava_rock(Platform_lava_rock):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
		""" Move the platform.
			If the player is in the way, it will shove the player
			out of the way. This does NOT handle what happens if a
			platform shoves a player into another object. Make sure
			moving platforms have clearance to push the player around
			or add code to handle what happens if they don't. """
 
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# We did hit the player. Shove the player around and
			# assume he/she won't hit anything else.
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1


# for prototype
class MovingEnemy(Platform_enemy):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# if the player just stand up/ not move
			# in front of enemy, he/she will die!
			# need to fix this
			gameoverscreen.show_game_over()
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# if the player just stand up/ not move
			# in front of enemy, he/she will die!
			gameoverscreen.show_game_over()
 
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1


# for special enemy
class MovingEnemySpecial(Platform_enemy):
	""" This is a fancier platform that can actually move. """
 
	def __init__(self, sprite_sheet_data):
 
		super().__init__(sprite_sheet_data)
 
		self.change_x = 0
		self.change_y = 0
 
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
 
		self.level = None
		self.player = None
 
	def update(self):
 
		# Move left/right
		self.rect.x += self.change_x
 
		# See if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# if the player just stand up/ not move
			# in front of enemy, he/she will die!
			# need to fix this
			gameoverscreen.show_game_over()
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# if the player just stand up/ not move
			# in front of enemy, he/she will die!
			gameoverscreen.show_game_over()
 
 
		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
 
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1
