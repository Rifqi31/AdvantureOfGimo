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

	def pause(self):
		"""Function for paused the game """
		# set boolean true
		paused = True
		# for calling it self
		settings = BasicSettings()
		# for frame pause
		clock = pygame.time.Clock()
		# bring text to the screen
		settings.msg_to_screen("Paused", constants.BLACK, -100, size="large")
		settings.msg_to_screen("Press P to continue or Q Press to Quit", constants.BLACK, 25)
		# update the display
		pygame.display.update()

		while paused:
			# logic for quit game
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				# event if keydown
				if event.type == pygame.KEYDOWN:
					# for resume game
					if event.key == pygame.K_p:
						paused = False
					elif event.key == pygame.K_q:
						pygame.quit()
						quit()
		

			clock.tick(5)



def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    configscreen.screen.fill(constants.BLUE)


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
	display_menu.add_option('Return to Main Menu', PYGAME_MENU_BACK)
	
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
	option_menu.add_option('Language', language_menu)
	option_menu.add_option('Display', display_menu)
	option_menu.add_option('Sounds', sounds_menu)
	option_menu.add_option('Return to Main Menu', PYGAME_MENU_BACK)

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


	# Core Menu
	main_menu = pygameMenu.Menu(configscreen.screen,
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
								title='Main Menu',
								window_height=constants.SCREEN_HEIGHT,
								window_width=constants.SCREEN_WIDTH)
	
	main_menu.add_option('Play', play_menu)
	main_menu.add_option('Option', option_menu)
	main_menu.add_option('About', about_menu)
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
	gameExit = False
	gameOver = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	settings = BasicSettings()

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
						# main()
						gameplay()
		
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				gameExit = True # Flag that we are done so we exit this loop
 
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				elif event.key == pygame.K_RIGHT:
					player.go_right()
				elif event.key == pygame.K_UP:
					player.jump()
				elif event.key == pygame.K_p:
					settings.pause()
 
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
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
 
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()
	quit()
 
# if __name__ == "__main__":
#	main()

main_menu()
