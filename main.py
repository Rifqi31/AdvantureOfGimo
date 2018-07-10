
# Import pygame and libraries
from pygame.locals import *

# import pygame module
import os
import pygame

# import pygameMenu module
import pygameMenu
from pygameMenu.locals import *

import configscreen

# import constants variable
import constants

import platform_scroller


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
								bgfun=platform_scroller.main_background,
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
	play_menu.add_option('Hiragana', platform_scroller.gameplay)
	play_menu.add_option('Katakana', platform_scroller.gameplay)
	play_menu.add_option('Back', PYGAME_MENU_BACK)


	# About Menu
	about_menu = pygameMenu.TextMenu(configscreen.screen,
								bgfun=platform_scroller.main_background,
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
								bgfun=platform_scroller.main_background,
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
	main_menu.add_option('Option' , platform_scroller.option_menu)
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


main_menu()