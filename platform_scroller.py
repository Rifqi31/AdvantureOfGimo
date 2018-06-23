import pygame
 
import constants
import levels
 
from player import Player
 
def main():
	""" Main Program """
	pygame.init()
 
	# Set the height and width of the screen
	size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
 
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
	#if current_level_no == 0:
	#	player.rect.x = 70
	#	player.rect.y = 360
	#	active_sprite_list.add(player)
	#elif current_level_no == 1:
	#	player.rect.x = 1500
	#	player.rect.y = 360
	#	active_sprite_list.add(player)
	
 
	#Loop until the user clicks the close button.
	gameExit = False
	gameOver = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	# config font
	smallfont = pygame.font.SysFont("comicsansms", 25)
	medfont = pygame.font.SysFont("comicsansms", 30)
	largefont = pygame.font.SysFont("comicsansms", 50)

	# function for create text size from variable
	def text_objects(text, color, size):
		# config text size small
		if size == "small":
			textSurface = smallfont.render(text, True, color)
		# config text size medium
		elif size == "medium":
			textSurface = medfont.render(text, True, color)
		# config text size large
		elif size == "large":
			textSurface = largefont.render(text, True, color)
		
		return textSurface, textSurface.get_rect()
	
	# function for render text to the screen
	def msg_to_screen(msg, color, y_displace=0, size = "small"):
		textSurf, textRect = text_objects(msg, color, size)
		textRect.center = (constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2) + y_displace
		screen.blit(textSurf, textRect)
	

	# function to pause game
	def pause():
		# set boolean true
		paused = True
		# bring text to the screen
		msg_to_screen("Paused", constants.BLACK, -100, size="large")
		msg_to_screen("Press C to continue or Q Press to Quit", constants.BLACK, 25)
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
					if event.key == pygame.K_c:
						paused = False
					elif event.key == pygame.K_q:
						pygame.quit()
						quit()
		

			clock.tick(5)



	# -------- Main Program Loop -----------
	while not gameExit:
		if gameOver == True:
			msg_to_screen("You Lose", constants.RED, y_displace=-50, size = "large")
			msg_to_screen("Press Q to Quit and Press C to play again", constants.BLACK, 50, size = "medium")
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
						# this is sucks too
						main()
		
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
					pause()
 
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
		if player.rect.bottom >= constants.SCREEN_HEIGHT or player.rect.bottom < 0 :
			gameOver = True

		# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
		current_level.draw(screen)
		active_sprite_list.draw(screen)
 
		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
		# Limit to 60 frames per second
		clock.tick(60)
 
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
 
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()
	quit()
 
if __name__ == "__main__":
	main()
