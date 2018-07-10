# name file : platforms.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

# asset for tileset level 01
# for wall dirt
dirt_wall = (0, 219, 140, 630)
dirt_big_wall = (584, 219, 350, 630)
# for landing dirt
dirt_land_bottom = (0, 0, 502, 140)
dirt_small = (584, 0, 140, 140)
# one platforms
dirt_half_grass = (219, 365, 280, 140)
dirt_small_half_grass = (219, 219, 140, 70)
one_dirt = (365, 219, 70, 70)
# for flying dirt
dirt_rounded = (438, 219, 70, 70)


# for snow dirt
snow_dirt_wall = (770, 162, 140, 630)
snow_dirt_big_wall = (325, 162, 350, 630)
snow_dirt_intro = (0, 0, 770, 140)

# proto portal
portal_snow = (228, 523, 70, 70)


# for hiragana & katakana
hiragana_a = (0, 0, 70, 70)
hiragana_i = (0, 72, 70, 70)

# for enemys
skull_ghost = (10, 5, 42, 51)


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





class MovingPlatform(Platform_dirt):
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
class MovingPlatform(Platform_enemy):
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
