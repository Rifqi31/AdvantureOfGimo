# name file : play_katakana_level_9.py
# python version 3

# Import pygame and libraries
from pygame.locals import *

# import pygame module
import os
import pygame
import pygameMenu
from pygameMenu.locals import *

# import constants variable
import constants
# import random module
import random
# import game screen module
from game_screens import mainmenu
from katakana_mode.overscreen_katakana import dead_katakana_level_9
# import levels
from katakana_mode.level_stage_katakana import (
    level_09, level_10, 
    level_11, level_ending
)
# import config font and screen
from game_settings import configfont, configscreen, configsounds, fontsettings
# import player module
from katakana_mode.katakana_level_9.player_level_9 \
    import Player, Bullet
# import spritesheet functions
from spritesheet_functions import SpriteSheet


# ----- Main Menu -----
def pause_background():
    """ Function for pause background color """

    configscreen.screen.fill(constants.BLUE)


def gameplay():
    """ Main Program """
    pygame.init()

    # set for title my game
    pygame.display.set_caption("Advanture of Gimo")

    # set icon game
    icon = pygame.image.load("spritesheet/gimo.png")
    pygame.display.set_icon(icon)

    # hide mouse cursor
    pygame.mouse.set_visible(False)

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(level_09.Level_09(player))
    level_list.append(level_10.Level_10(player))
    level_list.append(level_11.Level_11(player))
    level_list.append(level_ending.Level_Ending(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    # player position
    player.rect.x = 70
    player.rect.y = 360
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    # variable for game exit of course
    gameExit = False
    # variabel for game over of course
    gameOver = False

    # play the sound
    configsounds.turn_on_sounds()

    # call BasicSettings class
    settings = fontsettings.BasicSettings()

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
    option_display_settings = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )

    option_display_settings.add_option(
        'Fullscreen', configscreen.fullscreen_settings)
    option_display_settings.add_option(
        'Windowed', configscreen.windowed_settings)
    option_display_settings.add_option('Back', PYGAME_MENU_BACK)

    # sounds in game settings
    option_sounds_settings = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )

    option_sounds_settings.add_option('On Music', configsounds.turn_on_sounds)
    option_sounds_settings.add_option(
        'Off Music', configsounds.turn_off_sounds)
    option_sounds_settings.add_option('Back', PYGAME_MENU_BACK)

    # help in game setitings
    help_menu = pygameMenu.TextMenu(
        configscreen.screen,
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

    # confirm exit pause and main menu
    confirm_exit_pause = pygameMenu.Menu(
        configscreen.screen,
        bgfun=pause_background,
        enabled=False,
        font=pygameMenu.fonts.FONT_8BIT,
        font_size=25,
        font_size_title=30,
        menu_alpha=90,
        onclose=PYGAME_MENU_CLOSE,
        title='Are You Sure',
        title_offsety=5,
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    confirm_exit_pause.add_option('Yes', PYGAME_MENU_EXIT)
    confirm_exit_pause.add_option('No', PYGAME_MENU_BACK)

    confirm_back_tomenu = pygameMenu.Menu(
        configscreen.screen,
        bgfun=pause_background,
        enabled=False,
        font=pygameMenu.fonts.FONT_8BIT,
        font_size=25,
        font_size_title=30,
        menu_alpha=90,
        onclose=PYGAME_MENU_CLOSE,
        title='Are You Sure',
        title_offsety=5,
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    confirm_back_tomenu.add_option('Yes', mainmenu.main_menu)
    confirm_back_tomenu.add_option('No', PYGAME_MENU_BACK)

    # pause menu
    menu = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )

    menu.add_option('Back to Main Menu', confirm_back_tomenu)
    menu.add_option(option_sounds_settings.get_title(), option_sounds_settings)
    menu.add_option(option_display_settings.get_title(),
                    option_display_settings)
    menu.add_option(help_menu.get_title(), help_menu)
    menu.add_option('Exit', confirm_exit_pause)  # Add exit function

    # -------- Main Program Loop -----------
    while not gameExit:
        if gameOver:

            dead_hiragana_level_1.show_game_over_hiragana()

        events = pygame.event.get()
        for event in events:  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                gameExit = True  # Flag that we are done so we exit this loop

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                elif event.key == pygame.K_UP:
                    player.jump()

                # for player skill
                elif event.key == pygame.K_SPACE:

                    bullet = Bullet(player)
                    # play the sounds skill
                    configsounds.magic_sfx.play()
                    configsounds.magic_sfx.set_volume(0.5)

                    # Set the bullet so it is where the player is
                    if player.direction == "R":
                        bullet.rect.x = player.rect.x + 50
                        bullet.rect.y = player.rect.y + 30
                    elif player.direction == "L":
                        bullet.rect.x = player.rect.x
                        bullet.rect.y = player.rect.y + 30

                    # Add the bullet to the lists
                    active_sprite_list.add(bullet)
                    bullet.bullet_list.add(bullet)

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

        # debugging purpose
        # print(current_position)
        # check the position x and y
        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        if current_position == current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(configscreen.screen)
        active_sprite_list.draw(configscreen.screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # stage advanture for player
        def print_level_info(level_number):
            settings.msg_to_screen(
            # level number
                "Level {}".format(level_number), constants.WHITE, 0, 0, size="small")

            settings.msg_to_screen(
                "Misi Level {} :".format(level_number),
                constants.WHITE, 0, 25,
                size="small"
            )

            settings.msg_to_screen(
                "Tebak, temukan huruf katakana",
                constants.WHITE, 0, 50, size="small")

            # for player health
            if player.health_number == 100 or player.health_number == 90 \
                    or player.health_number == 80:
                settings.msg_to_screen(
                    "Health : " + str(player.health_number),
                    constants.GREEN,
                    90, 0,
                    size="small"
                )
            elif player.health_number == 70 or player.health_number == 60 \
                    or player.health_number == 50:
                settings.msg_to_screen(
                    "Health : " + str(player.health_number),
                    constants.YELLOW,
                    90, 0,
                    size="small"
                )
            elif player.health_number == 40 or player.health_number == 30 \
                    or player.health_number == 20 \
                    or player.health_number == 10:
                settings.msg_to_screen(
                    "Health : " + str(player.health_number),
                    constants.RED,
                    90, 0,
                    size="small"
                )

            settings.msg_to_screen(
                "Scores : " + str(player.scores),
                constants.WHITE,
                600, 0,
                size="small"
            )

        # if the player in the level 09
        if current_level == level_list[0]:
            # level number
            print_level_info(9)
            settings.msg_to_screen(
                "YA, YU, dan YO",
                constants.WHITE, 0, 75, size="small"
            )

        elif current_level == level_list[1]:
            # level number
            print_level_info(10)
            settings.msg_to_screen(
                "RA, RI, RU, RE, dan RO",
                constants.WHITE, 0, 75, size="small"
            )

        elif current_level == level_list[2]:
            # level number
            print_level_info(11)
            settings.msg_to_screen(
                "WA, WO, dan N",
                constants.WHITE, 0, 75, size="small"
            )

        # Limit to 60 frames per second
        clock.tick(60)

        menu.mainloop(events)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    quit()
