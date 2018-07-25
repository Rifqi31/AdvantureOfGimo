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

# for hiragana & katakana
hiragana_a = (0, 0, 70, 70)
hiragana_i = (0, 72, 70, 70)

# for enemys
skull_ghost = (10, 5, 42, 51)
fat_frog = (62, 7, 49, 49)

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
