"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""

# Import pygame and libraries
from pygame.locals import *

# import pygame module
import os
import pygame

import constants

# import sounds module
import configsounds

import gameoverscreen

from platforms import MovingPlatform, MovingPlatform_snow, MovingPlatform_dirt_sand, MovingPlatform_brick_red, MovingPlatform_ancient_brick
from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
	""" This class represents the bar at the bottom that the player
	controls. """
	# -- Methods
	def __init__(self):
		""" Constructor function """

		# Call the parent's constructor
		super().__init__()

		# -- Attributes
		# set score for player
		self.scores = 0
		# set health number for player
		self.health_number = 100
		# set damage for enemy
		self.general_enemy_dmg = 50
		self.false_point_dmg = 40
		# Set speed vector of player
		self.change_x = 0
		self.change_y = 0
 
		# This holds all the images for the animated walk left/right
		# of our player
		self.walking_frames_l = []
		self.walking_frames_r = []
 
		# What direction is the player facing?
		self.direction = "R"

		# removing special enemy
		self.special_remove_A = False
		self.special_remove_I = False
 
		# List of sprites we can bump against
		self.level = None
 
		sprite_sheet = SpriteSheet("spritesheet/player.png")
		# Load all the right facing images into a list
		image = sprite_sheet.get_image(10, 7, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 7, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(160, 7, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(10, 106, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 106, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(160, 106, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(10, 208, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 208, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(160, 208, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(10, 305, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 305, 66, 90)
		self.walking_frames_r.append(image)

		# Load all the right facing images, then flip them
		# to face left.
		image = sprite_sheet.get_image(10, 7, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 7, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(160, 7, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(10, 106, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 106, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(160, 106, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(10, 208, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 208, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(160, 208, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(10, 305, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 305, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
 
		# Set the image the player starts with
		self.image = self.walking_frames_r[0]
 
		# Set a reference to the image rect.
		self.rect = self.image.get_rect()
 
	def update(self):
		""" Move the player. """
		# Gravity
		self.calc_grav()
 
		# Move left/right
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]
 
		# for platform_list
		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If we are moving right,
			# set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right

		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
 
			# Stop our vertical movement
			self.change_y = 0
 
			if isinstance(block, MovingPlatform):
				self.rect.x += block.change_x
			
			if isinstance(block, MovingPlatform_ancient_brick):
				self.rect.x += block.change_x

			if isinstance(block, MovingPlatform_brick_red):
				self.rect.x += block.change_x
			
			if isinstance(block, MovingPlatform_dirt_sand):
				self.rect.x += block.change_x
			
			if isinstance(block, MovingPlatform_snow):
				self.rect.x += block.change_x
 

		# for general enemy list
		hit_by_enemy_list = pygame.sprite.spritecollide(self, self.level.enemy_list, True)
		for eaten in hit_by_enemy_list:
			self.health_number -= self.general_enemy_dmg
			configsounds.ouch_sfx.play()
			
			if self.health_number == 0:
				gameoverscreen.show_game_over()


		# for special enemy list
		# Symbol hiragana A
		special_hit_enemy_list_A = pygame.sprite.spritecollide(self, self.level.special_enemy_list, True)
		for special_eaten_A in special_hit_enemy_list_A:

			if self.special_remove_A == False:
				gameoverscreen.show_game_over()
		

		# for portal list
		go_to_portal_list = pygame.sprite.spritecollide(self, self.level.portal_list, True)
		for gate in go_to_portal_list:
			configsounds.portal_sfx.play()
		

		# for death sprite
		you_die_in_hell = pygame.sprite.spritecollide(self, self.level.death_place_list, False)
		for water_suicide in you_die_in_hell:
			self.rect.y += 20
			if self.rect.bottom >= constants.SCREEN_HEIGHT or self.rect.bottom < 0:
				gameoverscreen.show_game_over()
		
		for sharp_rock in you_die_in_hell:
			self.rect.y += 20
			if self.rect.bottom >= constants.SCREEN_HEIGHT or self.rect.bottom < 0:
				gameoverscreen.show_game_over()
		
		for lava_water_suicide in you_die_in_hell:
			self.rect.y += 20
			if self.rect.bottom >= constants.SCREEN_HEIGHT or self.rect.bottom < 0:
				gameoverscreen.show_game_over()


		# for hiragana and katakana list
		# FOR LEVEL 1
		point_wibu_list1 = pygame.sprite.spritecollide(self, self.level.hiragana_A, True)
		point_wibu_list2 = pygame.sprite.spritecollide(self, self.level.hiragana_I, True)
		
		for true_point in point_wibu_list1:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 1
			self.special_remove_A = True
		
		for false_point in point_wibu_list2:
			configsounds.ouch_sfx.play()
			self.scores -= 1
			# self.special_remove_I = True
			self.health_number -= self.false_point_dmg
			if self.health_number == 0:
				gameoverscreen.show_game_over()




	def calc_grav(self):
		""" Calculate effect of gravity. """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35

		# See if we are on the ground.
		if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
	
	def jump(self):
		""" Called when user hits 'jump' button. """

		# move down a bit and see if there is a platform below us.
		# Move down 2 pixels because it doesn't work well if we only move down 1
		# when working with a platform moving down.
		
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2

		# If it is ok to jump, set our speed upwards
		if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
			# play the sound
			configsounds.jump_sfx.play()
			self.change_y = -10
		
	# Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -6
		self.direction = "L"

	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 6
		self.direction = "R"

	def stop(self):
		""" Called when the user lets off the keyboard. """
		self.change_x = 0
	


# class for bullet
class Bullet(Player):
	""" This Class represent the bullet from player"""
	def __init__(self, player):
		super().__init__()

		self.image = pygame.Surface([4, 10])
		self.image.fill(constants.MAGIC_BULLET)

		self.rect = self.image.get_rect()

		self.bullet_list = pygame.sprite.Group()

		# access variable from player class
		self.direction = player.direction
		self.level = player.level
		self.special_remove_A = player.special_remove_A

	def update(self):
		""" move the bullet """
		if self.direction == "R":
			self.rect.x += 5

		elif self.direction == "L":
			self.rect.x -= 5

		# when hit enemy the bullet is gone
		hitting_enemy = pygame.sprite.spritecollide(self, self.level.enemy_list, True)

		for eaten in hitting_enemy:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		# just for special enemy list they are immune
		# if the player not get point mission enemy are immnune
		# for point mission hiragana symbol A
		if self.special_remove_A == False:
			hitting_special_enemy_A = pygame.sprite.spritecollide(self, self.level.special_enemy_list, False)
		# if the player get point mission enemy are not immnune
		elif self.special_remove_A == True:
			hitting_special_enemy_A = pygame.sprite.spritecollide(self, self.level.special_enemy_list, True)
			#self.special_remove_A = False

		# attack an enemy
		for special_eaten_A in hitting_special_enemy_A:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		# when hit platform the bullet is gone
		hitting_platform = pygame.sprite.spritecollide(self, self.level.platform_list, False)

		for block in hitting_platform:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
