# name file : platform_scroller.py
# python version 3

# Import pygame and libraries
from pygame.locals import *

# import pygame module
import os
import pygame

# import pygameMenu module
import pygameMenu
from pygameMenu.locals import *

# import constants variable
import constants
# import levels
import levels
# import config font and screen
import configfont
import configscreen
# import sounds file
import configsounds
# import player module
from player import Player

from spritesheet_functions import SpriteSheet

import random

import fontsettings

# ----- For Display Settings -----
def fullscreen_settings():
	""" This function for fullscreen settings """
	pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.FULLSCREEN)

def windowed_settings():
	""" This function for windowed screen settings """
	pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


# ----- For Sounds Settings -----
def turn_off_sounds():
	""" This function for turn off all sounds """
	pygame.mixer.stop()

def turn_on_sounds():
	""" This function for turn on all sounds """
	configsounds.background_music.play(-1)
	configsounds.background_music.set_volume(0.5)


# ----- Main Menu ----- 
def main_background():
	"""
	Function used by menus, draw on background while menu is active.

	:return: None
	"""
	background_position = [0, 0]
	background_image = pygame.image.load("spritesheet/menu_background.png").convert_alpha()
	configscreen.screen.blit(background_image, background_position)


def pause_background():
	""" Function for pause background color """

	configscreen.screen.fill(constants.BLUE)


# Option Menu
def option_menu():
	""" Function for Option Menu """
	clock = pygame.time.Clock()
	
	# Display Menu
	display_menu = pygameMenu.Menu(configscreen.screen,
									bgfun=main_background,
									color_selected=constants.WHITE,
									font=pygameMenu.fonts.FONT_8BIT,
									font_size=25,
									font_size_title=30,
									menu_alpha=100,
									menu_color=constants.DARK_BROWN_DIRT,
									menu_height=int(constants.SCREEN_HEIGHT * 0.6),
									menu_width=int(constants.SCREEN_WIDTH * 0.6),
									onclose=PYGAME_MENU_DISABLE_CLOSE,
									option_shadow=False,
									title='Display Settings',
									window_height=constants.SCREEN_HEIGHT,
									window_width=constants.SCREEN_WIDTH)
	display_menu.add_option('Windowed', windowed_settings)
	display_menu.add_option('Fullscreen', fullscreen_settings)
	display_menu.add_option('Return to Option', PYGAME_MENU_BACK)

	# Option Menu
	option_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_8BIT,
								font_size=25,
								font_size_title=30,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title="Option",
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	option_menu.add_option('Display', display_menu)
	# option_menu.add_option('Sounds', sounds_menu)
	option_menu.add_option('Back', main_menu)

	while True:

		# Tick
		clock.tick(60)

		# Application events
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				exit()

		# Main menu
		option_menu.mainloop(events)

		# Flip surface
		pygame.display.flip()



# Main Menu
def main_menu():
	""" Function for Main Menu """
	
	# initialize
	pygame.init()
	
	# set for title my game
	pygame.display.set_caption("Advanture of Gimo")
	
	# set clock
	clock = pygame.time.Clock()
	
	# Play Menu
	play_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_8BIT,
								font_size=25,
								font_size_title=30,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title='Select Mode',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	play_menu.add_option('Hiragana', gameplay)
	play_menu.add_option('Katakana', gameplay)
	play_menu.add_option('Back', PYGAME_MENU_BACK)


	# About Menu
	about_menu = pygameMenu.TextMenu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_NEVIS,
								font_color=constants.DARK_GRASS_GREEN,
								font_size_title=30,
								font_title=pygameMenu.fonts.FONT_8BIT,
								menu_color=constants.LIGHT_BROWN_DIRT,
								menu_color_title=constants.LIGHT_GRASS_GREEN,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								text_color=constants.WHITE,
								text_fontsize=15,
								font_size=30,
								title='About',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	for m in constants.ABOUT:
		about_menu.add_line(m)
		about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
	about_menu.add_option('Return to Menu', PYGAME_MENU_BACK)

	# Core Menu
	main_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_8BIT,
								font_size=30,
								font_size_title=30,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title='Main Menu',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)

	main_menu.add_option('Play', play_menu)
	main_menu.add_option('Option' , option_menu)
	main_menu.add_option(about_menu.get_title(), about_menu)
	main_menu.add_option('Exit', PYGAME_MENU_EXIT)

	while True:

		# Tick
		clock.tick(60)

		# Application events
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				exit()

		# Main menu
		main_menu.mainloop(events)

		# Flip surface
		pygame.display.flip()




def gameplay():
	""" Main Program """
	pygame.init()

	# set for title my game
	pygame.display.set_caption("Advanture of Gimo")

	# Create the player
	player = Player()

	# Create all the levels
	level_list = []
	level_list.append(levels.Level_01(player))
	level_list.append(levels.Level_02(player))

	# Set the current level
	current_level_no = 0
	current_level = level_list[current_level_no]

	active_sprite_list = pygame.sprite.Group()
	player.level = current_level

	# player position
	player.rect.x = 70
	player.rect.y = 360
	active_sprite_list.add(player)


	#Loop until the user clicks the close button.
	# variable for game exit of course
	gameExit = False
	# variabel for game over of course
	gameOver = False

	# play the sound
	turn_on_sounds()

	# call BasicSettings class
	settings = fontsettings.BasicSettings()
	# access_sprite_level = levels.Level(player)
	# access_level_2 = levels.Level_02(player)

	# creating a snows
	# create an empty array
	snow_list = []

	for i in range(50):
		x = random.randrange(0, 790)
		y = random.randrange(0, 590)
		# pygame.draw.circle(screen, WHITE, [x, y], 2)
		snow_list.append([x, y])

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	# display in game settings
	option_display_settings = pygameMenu.Menu(configscreen.screen,
					   bgfun=pause_background,
					   enabled=False,
					   font=pygameMenu.fonts.FONT_8BIT,
					   menu_alpha=90,
					   font_size=25,
					   font_size_title=30,
					   onclose=PYGAME_MENU_CLOSE,
					   title='Display',
					   title_offsety=5,
					   menu_height=int(constants.SCREEN_HEIGHT * 0.6),
					   menu_width=int(constants.SCREEN_WIDTH * 0.6),
					   window_height=constants.SCREEN_HEIGHT,
					   window_width=constants.SCREEN_WIDTH)
	
	option_display_settings.add_option('Fullscreen', fullscreen_settings)
	option_display_settings.add_option('Windowed', windowed_settings)
	option_display_settings.add_option('Back', PYGAME_MENU_BACK)

	# sounds in game settings
	option_sounds_settings = pygameMenu.Menu(configscreen.screen,
							bgfun=pause_background,
							enabled=False,
							font=pygameMenu.fonts.FONT_8BIT,
							font_size=25,
							font_size_title=30,
							menu_alpha=90,
							onclose=PYGAME_MENU_CLOSE,
							title='Sounds',
							title_offsety=5,
							menu_height=int(constants.SCREEN_HEIGHT * 0.6),
							menu_width=int(constants.SCREEN_WIDTH * 0.6),
							window_height=constants.SCREEN_HEIGHT,
							window_width=constants.SCREEN_WIDTH)

	option_sounds_settings.add_option('On Music', turn_on_sounds)
	option_sounds_settings.add_option('Off Music', turn_off_sounds)
	option_sounds_settings.add_option('Back', PYGAME_MENU_BACK)
	
	# help in game setitings
	help_menu = pygameMenu.TextMenu(configscreen.screen,
									bgfun=pause_background,
									font=pygameMenu.fonts.FONT_NEVIS,
									font_size_title=30,
									font_title=pygameMenu.fonts.FONT_8BIT,
									menu_color_title=constants.BLUE,
									onclose=PYGAME_MENU_CLOSE,
									text_fontsize=20,
									font_size=30,
									title='Help',
									menu_height=int(constants.SCREEN_HEIGHT * 0.6),
									menu_width=int(constants.SCREEN_WIDTH * 0.6),
									window_height=constants.SCREEN_HEIGHT,
									window_width=constants.SCREEN_WIDTH
									)
	help_menu.add_option('Back', PYGAME_MENU_BACK)
	for m in constants.HELP:
		help_menu.add_line(m)
	help_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)


	# pause menu
	menu = pygameMenu.Menu(configscreen.screen,
					   bgfun=pause_background,
					   enabled=False,
					   font=pygameMenu.fonts.FONT_8BIT,
					   font_size=25,
					   font_size_title=30,
					   menu_alpha=90,
					   onclose=PYGAME_MENU_CLOSE,
					   title='Pause Menu',
					   title_offsety=5,
					   menu_height=int(constants.SCREEN_HEIGHT * 0.6),
					   menu_width=int(constants.SCREEN_WIDTH * 0.6),
					   window_height=constants.SCREEN_HEIGHT,
					   window_width=constants.SCREEN_WIDTH)
	
	menu.add_option(option_sounds_settings.get_title(), option_sounds_settings)
	menu.add_option(option_display_settings.get_title(), option_display_settings)
	menu.add_option(help_menu.get_title(), help_menu)
	menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function

	# -------- Main Program Loop -----------
	while not gameExit:
		if gameOver == True:
			# stop the background music
			pygame.mixer.stop()
			# play game over music
			configsounds.game_over_sfx.play()
			configsounds.game_over_sfx.set_volume(0.5)

			game_over_screen = pygameMenu.Menu(configscreen.screen,
								 dopause=False,
								 font=pygameMenu.fonts.FONT_8BIT,
								 font_size_title=30,
								 font_title=pygameMenu.fonts.FONT_8BIT,
								 menu_color_title=constants.BLUE,
								 onclose=PYGAME_MENU_DISABLE_CLOSE,
								 title='Game Over',
								 menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								 menu_width=int(constants.SCREEN_WIDTH * 0.6),
								 window_height=constants.SCREEN_HEIGHT,
								 window_width=constants.SCREEN_WIDTH
								 )
			game_over_screen.add_option('Retry', gameplay)
			game_over_screen.add_option('Exit Game', PYGAME_MENU_EXIT)

			while True:

				# Tick
				clock.tick(60)

				# Application events
				events = pygame.event.get()
				for event in events:
					if event.type == QUIT:
						exit()

				# Main menu
				game_over_screen.mainloop(events)

				# Flip surface
				pygame.display.flip()
			
		events = pygame.event.get()
		for event in events: # User did something
			if event.type == pygame.QUIT: # If user clicked close
				gameExit = True # Flag that we are done so we exit this loop

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				elif event.key == pygame.K_RIGHT:
					player.go_right()
				elif event.key == pygame.K_UP:
					player.jump()
				elif event.key == pygame.K_ESCAPE:
					menu.enable()
					
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				elif event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()

		# Update the player.
		active_sprite_list.update()
		# Update items in the level
		current_level.update()

		# If the player gets near the right side, shift the world left (-x)
		if player.rect.right >= 500:
			diff = player.rect.right - 500
			player.rect.right = 500
			current_level.shift_world(-diff)

		# If the player gets near the left side, shift the world right (+x)
		if player.rect.left <= 120:
			diff = 120 - player.rect.left
			player.rect.left = 120
			current_level.shift_world(diff)

		current_position = player.rect.x + current_level.world_shift
		if current_position < current_level.level_limit:
			player.rect.x = 120
			if current_level_no < len(level_list)-1:
				current_level_no += 1
				current_level = level_list[current_level_no]
				player.level = current_level
				
		# if player fall is game over
		if player.rect.bottom >= constants.SCREEN_HEIGHT or player.rect.bottom < 0:
			if current_level == level_list[0] or level_list[1]:
				gameOver = True

		# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
		current_level.draw(configscreen.screen)
		active_sprite_list.draw(configscreen.screen)

		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# if player in the level 01
		if current_level == level_list[0]:

			settings.msg_to_screen("Level 1", constants.WHITE, 0, 0, size = "small")
			settings.msg_to_screen("Cara Bermain :",
									constants.WHITE,
									100, 50, size= "small")
			settings.msg_to_screen("Tombol tanda panah ----> : jalan ke kanan", 
									constants.WHITE,
									100, 100, size= "small")
			settings.msg_to_screen("Tombol tanda panah <---- : jalan ke kiri",
									constants.WHITE,
									100, 150, size="small")
			settings.msg_to_screen("Tombol tanda panah ^ : melompat",
									constants.WHITE,
									100, 200, size="small")
			settings.msg_to_screen("|", constants.WHITE, 340, 210, size="small")
			settings.msg_to_screen("Esc : Pause/Resume", constants.WHITE, 100, 250, size="small")
			

			# process each snow flake in the list
			for i in range(len(snow_list)):

				# draw the snow flake
				pygame.draw.circle(configscreen.screen, constants.WHITE, snow_list[i], 2)

				# move the snow flake down one pixel
				snow_list[i][1] += 1

				# if the snow flake has moved off the bottom of the screen
				if snow_list[i][1] > 450:
					# reset it just above the top
					y = random.randrange(-50, -10)
					snow_list[i][1] = y
					# give it new x position
					x = random.randrange(0, 790)
					snow_list[i][0] = x

		# if the player in the level 02
		if current_level == level_list[1]:
			
			settings.msg_to_screen("Level 2", constants.WHITE, 0, 0, size = "small")
			settings.msg_to_screen("Misi : Cari Huruf A", constants.WHITE, 0, 50, size="small")
			settings.msg_to_screen("Scores : " + str(player.scores), constants.WHITE, 600, 0, size="small")
			
		# Limit to 60 frames per second
		clock.tick(60)

		menu.mainloop(events)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()
	quit()

main_menu()
