# name file : platform_scroller.py
# python version 3

# import pygame module
import pygame

import constants

import levels
import levels01

from player import Player

# this is a main program
# initialize
pygame.init()

# set the height and width of the screen
size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

# title game
pygame.display.set_caption("Advanture of Gimo")

# create a player
player = Player()

# create all levels
level_list = []
level_list.append(levels01.Level_01(player))

# set the current level
current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player.level = current_level

# player position
player.rect.x = 70
player.rect.y = 360
active_sprite_list.add(player)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# config font
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 30)
largefont = pygame.font.SysFont("comicsansms", 50)


# fungsi config render ukuran font ke layar dengan parameternya adalah text, warna, dan ukuran
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



# function for render text for screen
def msg_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2) + y_displace
    screen.blit(textSurf, textRect)


# core function
def gameloop():
    
    #Loop until the user clicks the close button.
    # create game over logic here
    # when player has mistaken or die

    gameOver = False
    gameExit = False


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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()


        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                gameExit = True # Flag that we are done so we exit this loop
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
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
        
        # if player fall is game over
        if player.rect.bottom >= constants.SCREEN_HEIGHT or player.rect.bottom < 0 :
            gameOver = True



        # this code for portal to the next level

        # If the player gets to the end of the level, go to the next level
        # current_position = player.rect.x + current_level.world_shift
        # if current_position < current_level.level_limit:
        #    player.rect.x = 120
        #    if current_level_no < len(level_list)-1:
        #        current_level_no += 1
        #        current_level = level_list[current_level_no]
        #        player.level = current_level



        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.update()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


gameloop()