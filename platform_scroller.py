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

class BasicSettings(object):
	"""this is basic settings"""

	def text_objects(self ,text, color, size):
		"""Function for store variable size font"""

		# config text size small
		if size == "small":
			textSurface = configfont.smallfont.render(text, True, color)
		# config text size medium
		elif size == "medium":
			textSurface = configfont.medfont.render(text, True, color)
		# config text size large
		elif size == "large":
			textSurface = configfont.largefont.render(text, True, color)

		return textSurface, textSurface.get_rect()

	def msg_to_screen(self, msg, color, y_displace=0, size = "small"):
		"""Function for render text to the screen """

		# for calling it self
		settings = BasicSettings()

		textSurf, textRect = settings.text_objects(msg, color, size)
		textRect.center = (constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2) + y_displace
		configscreen.screen.blit(textSurf, textRect)


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
	pygame.mixer.music.stop()

def turn_on_sounds():
	""" This function for turn on all sounds """
	pygame.mixer.music.play()


# ----- Main Menu ----- 
def main_background():
	"""
	Function used by menus, draw on background while menu is active.

	:return: None
	"""
	background_position = [0, 0]
	background_image = pygame.image.load("spritesheet/menu_background.png").convert_alpha()
	configscreen.screen.blit(background_image, background_position)


# Option Menu
def option_menu():
	""" Function for Option Menu """
	clock = pygame.time.Clock()
	# Language Menu
	language_menu = pygameMenu.Menu(configscreen.screen,
									bgfun=main_background,
									color_selected=constants.WHITE,
									font=pygameMenu.fonts.FONT_BEBAS,
									font_size=30,
									menu_alpha=100,
									menu_color=constants.DARK_BROWN_DIRT,
									menu_height=int(constants.SCREEN_HEIGHT * 0.6),
									menu_width=int(constants.SCREEN_WIDTH * 0.6),
									onclose=PYGAME_MENU_DISABLE_CLOSE,
									option_shadow=False,
									title='Language Settings',
									window_height=constants.SCREEN_HEIGHT,
									window_width=constants.SCREEN_WIDTH)
	language_menu.add_option('Return to Main Menu', PYGAME_MENU_BACK)

	# Display Menu
	display_menu = pygameMenu.Menu(configscreen.screen,
									bgfun=main_background,
									color_selected=constants.WHITE,
									font=pygameMenu.fonts.FONT_BEBAS,
									font_size=30,
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

	# Sounds Menu
	sounds_menu = pygameMenu.Menu(configscreen.screen,
									bgfun=main_background,
									color_selected=constants.WHITE,
									font=pygameMenu.fonts.FONT_BEBAS,
									font_size=30,
									menu_alpha=100,
									menu_color=constants.DARK_BROWN_DIRT,
									menu_height=int(constants.SCREEN_HEIGHT * 0.6),
									menu_width=int(constants.SCREEN_WIDTH * 0.6),
									onclose=PYGAME_MENU_DISABLE_CLOSE,
									option_shadow=False,
									title='Sounds Settings',
									window_height=constants.SCREEN_HEIGHT,
									window_width=constants.SCREEN_WIDTH)
	sounds_menu.add_option('On', turn_on_sounds)
	sounds_menu.add_option('Off', turn_off_sounds)
	sounds_menu.add_option('Return to Main Menu', PYGAME_MENU_BACK)

	# Option Menu
	option_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_BEBAS,
								font_size=30,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title="Option",
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	option_menu.add_option(language_menu.get_title(), language_menu)
	option_menu.add_option(display_menu.get_title(), display_menu)
	option_menu.add_option(sounds_menu.get_title(), sounds_menu)
	option_menu.add_option('Return to Main Menu', main_menu)

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
	clock = pygame.time.Clock()
	# Play Menu
	play_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_BEBAS,
								font_size=30,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title='Play Menu',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	play_menu.add_option('Start', gameplay)
	play_menu.add_option('Return to Main Menu', PYGAME_MENU_BACK)


	# About Menu
	about_menu = pygameMenu.TextMenu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_BEBAS,
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
								text_fontsize=20,
								title='About',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	for m in constants.ABOUT:
		about_menu.add_line(m)
		about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
	about_menu.add_option('Return to menu', PYGAME_MENU_BACK)


	# How to play Menu
	how_to_play_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_BEBAS,
								font_size=30,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title='How To Play',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)


	# Core Menu
	main_menu = pygameMenu.Menu(configscreen.screen,
								bgfun=main_background,
								color_selected=constants.WHITE,
								font=pygameMenu.fonts.FONT_BEBAS,
								font_size=40,
								menu_alpha=100,
								menu_color=constants.DARK_BROWN_DIRT,
								menu_height=int(constants.SCREEN_HEIGHT * 0.6),
								menu_width=int(constants.SCREEN_WIDTH * 0.6),
								onclose=PYGAME_MENU_DISABLE_CLOSE,
								option_shadow=False,
								title='Main Menu',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)

	main_menu.add_option(play_menu.get_title(), play_menu)
	main_menu.add_option('Option' , option_menu)
	main_menu.add_option(how_to_play_menu.get_title(), how_to_play_menu)
	main_menu.add_option(about_menu.get_title(), about_menu)
	main_menu.add_option('Quit', PYGAME_MENU_EXIT)

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

	configscreen.size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
	configscreen.screen = pygame.display.set_mode(configscreen.size)

	# set for title my game
	pygame.display.set_caption("Advanture of Gimo")

	# Create the player
	player = Player()

	# Create all the levels
	level_list = []
	level_list.append(levels.Level_01(player))
	level_list.append(levels.Level_02(player))

	# Set the current level
	current_level_no = 0 # dis is suck # mentok disini
	current_level = level_list[current_level_no]

	active_sprite_list = pygame.sprite.Group()
	player.level = current_level

	# player position
	if current_level == level_list[0]:
		player.rect.x = 70
		player.rect.y = 360
		active_sprite_list.add(player)
	elif current_level == level_list[1]:
		player.rect.x = 70
		player.rect.y = 360
		active_sprite_list.add(player)


	#Loop until the user clicks the close button.
	# variable for game exit of course
	gameExit = False
	# variabel for game over of course
	gameOver = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	# call a class with a variable
	settings = BasicSettings()

	# display in game settings
	option_display_settings = pygameMenu.Menu(configscreen.screen,
					   bgfun=main_background,
					   enabled=False,
					   font=pygameMenu.fonts.FONT_NEVIS,
					   menu_alpha=90,
					   onclose=PYGAME_MENU_CLOSE,
					   title='Display',
					   title_offsety=5,
					   window_height=constants.SCREEN_HEIGHT,
					   window_width=constants.SCREEN_WIDTH)
	
	option_display_settings.add_option('Fullscreen', fullscreen_settings)
	option_display_settings.add_option('Windowed', windowed_settings)
	option_display_settings.add_option('Back', PYGAME_MENU_BACK)

	# sounds in game settings
	option_sounds_settings = pygameMenu.Menu(configscreen.screen,
							bgfun=main_background,
							enabled=False,
							font=pygameMenu.fonts.FONT_NEVIS,
							menu_alpha=90,
							onclose=PYGAME_MENU_CLOSE,
							title='Sounds',
							title_offsety=5,
							window_height=constants.SCREEN_HEIGHT,
							window_width=constants.SCREEN_WIDTH)

	option_sounds_settings.add_option('On', turn_on_sounds)
	option_sounds_settings.add_option('Off', turn_off_sounds)
	option_sounds_settings.add_option('Back', PYGAME_MENU_BACK)
	
	# help in game setitings
	help_menu = pygameMenu.TextMenu(configscreen.screen,
									bgfun=main_background,
									font=pygameMenu.fonts.FONT_NEVIS,
									font_size_title=30,
									font_title=pygameMenu.fonts.FONT_8BIT,
									menu_color_title=constants.BLUE,
									onclose=PYGAME_MENU_CLOSE,
									text_fontsize=20,
									title='Help',
									window_height=constants.SCREEN_HEIGHT,
									window_width=constants.SCREEN_WIDTH
									)
	help_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
	for m in constants.HELP:
		help_menu.add_line(m)
	help_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)


	# pause menu
	menu = pygameMenu.Menu(configscreen.screen,
					   bgfun=main_background,
					   enabled=False,
					   font=pygameMenu.fonts.FONT_NEVIS,
					   menu_alpha=90,
					   onclose=PYGAME_MENU_CLOSE,
					   title='Main Menu',
					   title_offsety=5,
					   window_height=constants.SCREEN_HEIGHT,
					   window_width=constants.SCREEN_WIDTH)

	menu.add_option(option_sounds_settings.get_title(), option_sounds_settings)
	menu.add_option(option_display_settings.get_title(), option_display_settings)
	menu.add_option(help_menu.get_title(), help_menu)
	menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function

	# -------- Main Program Loop -----------
	while not gameExit:
		if gameOver == True:
			settings.msg_to_screen("You Lose", constants.RED, y_displace=-50, size = "large")
			settings.msg_to_screen("Press Q to Quit and Press C to play again", constants.BLACK, 50, size = "medium")
			pygame.display.update()

		while gameOver == True:
			for event in pygame.event.get():
				# event game quit
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					elif event.key == pygame.K_c:
						gameplay()

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
					# jump sound has been activated
					configsounds.jump_sfx.play()
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

		# if player got to portal # this is sucks
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
