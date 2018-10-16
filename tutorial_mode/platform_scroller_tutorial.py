# name file : platform_scroller_tutorial.py
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
# import levels
from hiragana_mode.level_stage_hiragana import (
    level_tutorial, level_tutorial_gameplay,
    level_tutorial_kill, level_tutorial_kill_special,
    level_ending_tutorial
    )
# import config font and screen
from game_settings import configfont, configscreen, configsounds, fontsettings
# import player module
from tutorial_mode.player import Player, Bullet
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
    level_list.append(level_tutorial.Level_Tutorial(player))
    level_list.append(level_tutorial_gameplay.Level_Tutorial_Gameplay(player))
    level_list.append(level_tutorial_kill.Level_Tutorial_Kill(player))
    level_list.append(level_tutorial_kill_special.Level_Tutorial_Kill_Special(player))
    level_list.append(level_ending_tutorial.Level_Ending_Tutorial(player))

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
    # gameOver = False

    # stop ending sound
    pygame.mixer.stop()

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

    # Prototype for floating text
    orig_surf = configfont.smallfont.render('hiragana benar', True, constants.WHITE)
    text_surf = orig_surf.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pygame.Surface(text_surf.get_size(), pygame.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    timer = 20  # To get a 20 frame delay.

    # -------- Main Program Loop -----------
    while not gameExit:
        # if gameOver:

        #    gameoverscreen.show_game_over_hiragana()

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

        # if player in the intro
        if current_level == level_list[0]:

            settings.msg_to_screen(
                "Tutorial", constants.WHITE, 0, 0, size="small")
            settings.msg_to_screen("Control :",
                                   constants.WHITE,
                                   100, 50, size="small")
            settings.msg_to_screen("Tombol tanda panah ----> : jalan ke kanan",
                                   constants.WHITE,
                                   100, 100, size="small")
            settings.msg_to_screen("Tombol tanda panah <---- : jalan ke kiri",
                                   constants.WHITE,
                                   100, 150, size="small")
            settings.msg_to_screen("Tombol tanda panah ^ : melompat",
                                   constants.WHITE,
                                   100, 200, size="small")
            settings.msg_to_screen("|", constants.WHITE,
                                   296, 210, size="small")
            settings.msg_to_screen(
                "Tombol Spasi : Menembak",
                constants.WHITE,
                100, 250,
                size="small"
            )
            settings.msg_to_screen("Esc : Pause/Resume",
                                   constants.WHITE, 100, 300, size="small")

            # process each snow flake in the list
            for i in range(len(snow_list)):

                # draw the snow flake
                pygame.draw.circle(configscreen.screen,
                                   constants.WHITE, snow_list[i], 2)

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

        # for how to play
        if current_level == level_list[1]:

            settings.msg_to_screen(
                "Jenis Musuh dan Point :", constants.WHITE, 0, 0, size="small")
            settings.msg_to_screen(
                "Special Enemy : reduce health -40%",
                constants.WHITE,
                150, 100,
                size="small"
            )
            settings.msg_to_screen(
                "General Enemy : reduce health -30%",
                constants.WHITE,
                150, 180,
                size="small"
            )
            settings.msg_to_screen(
                "Restore Health : increase health +20%",
                constants.WHITE,
                150, 270,
                size="small"
            )

            # process each snow flake in the list
            for i in range(len(snow_list)):

                # draw the snow flake
                pygame.draw.circle(configscreen.screen,
                                   constants.WHITE, snow_list[i], 2)

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

        # for how to play
        if current_level == level_list[2]:

            settings.msg_to_screen(
                "Tutorial", constants.WHITE, 0, 0, size="small")

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
                "Cara Bermain :",
                constants.WHITE,
                100, 50, size="small"
            )
            settings.msg_to_screen(
                "1.Gerakan Player dan Arahkan ke depan musuh",
                constants.WHITE,
                100, 100, size="small"
            )
            settings.msg_to_screen(
                "2.Tekan tombol [spasi] untuk menghancurkan musuh",
                constants.WHITE,
                100, 150, size="small"
            )
            settings.msg_to_screen(
                "3.Jika Player terkena gerakan musuh",
                constants.WHITE,
                100, 200, size="small"
            )
            settings.msg_to_screen(
                "maka health player berkurang -30%", constants.WHITE,
                100, 250, size="small"
            )

            # process each snow flake in the list
            for i in range(len(snow_list)):

                # draw the snow flake
                pygame.draw.circle(configscreen.screen,
                                   constants.WHITE, snow_list[i], 2)

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


        if current_level == level_list[3]:

            settings.msg_to_screen(
                "Tutorial", constants.WHITE, 0, 0, size="small")

            settings.msg_to_screen(
                "Scores : " + str(player.scores),
                constants.WHITE,
                600, 0,
                size="small"
            )

            settings.msg_to_screen(
                "hiragana :",
                constants.WHITE,
                300, 0,
                size="small"
            )            
            # for confirm text hiragana
            if player.special_remove_A == True:
                if bullet.confirm_hiragana == True:
                    settings.msg_to_screen(
                        "benar",
                        constants.GREEN,
                        400, 0,
                        size="small"
                    )
                    # process floating font
                    if timer > 0:
                        timer -= 1
                    else:
                        if alpha > 4:
                            # Reduce alpha each frame, but make sure it doesn't get below 0.
                            alpha -= 4
                            text_surf = orig_surf.copy()
                            # Fill alpha_surf with this color to set its alpha value.
                            alpha_surf.fill((255, 255, 255, alpha))
                            # To make the text surface transparent, blit the transparent
                            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
                            text_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    
                            configscreen.screen.blit(text_surf, (490, 350))
                
            elif player.special_remove_U == False:
                if bullet.confirm_hiragana == False:
                    settings.msg_to_screen(
                        "salah",
                        constants.RED,
                        400, 0,
                        size="small"
                    )
            
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
                "Cara Bermain :",
                constants.WHITE,
                100, 50, size="small"
            )
            settings.msg_to_screen(
                "1.Tebak dan ambil point huruf jepang, lalu tembakan ke musuh",
                constants.WHITE,
                100, 100, size="small"
            )
            settings.msg_to_screen(
                "2.Jika benar, point bertambah sebanyak +100, dan musuh mati",
                constants.WHITE,
                100, 150, size="small"
            )
            settings.msg_to_screen(
                "3.Jika salah, point berkurang sebanyak -100,",
                constants.WHITE,
                100, 200, size="small"
            )
            settings.msg_to_screen(
                "health player berkurang sebanyak -40%, dan musuh tidak mati",
                constants.WHITE,
                100, 250, size="small"
            )

            # process each snow flake in the list
            for i in range(len(snow_list)):

                # draw the snow flake
                pygame.draw.circle(
                    configscreen.screen,
                    constants.WHITE, snow_list[i], 2)

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

        if current_level == level_list[4]:

            # process each snow flake in the list
            for i in range(len(snow_list)):

                settings.msg_to_screen(
                    "Tutorial", constants.WHITE, 0, 0, size="small")

                settings.msg_to_screen(
                    "Selamat anda telah menyelesaikan semua level",
                    constants.WHITE,
                    100, 100, size="small"
                )
                settings.msg_to_screen(
                    "Sentuh npc untuk mengulang atau keluar dari level tutorial",
                    constants.WHITE,
                    100, 150, size="small"
                )

                # draw the snow flake
                pygame.draw.circle(configscreen.screen,
                                   constants.WHITE, snow_list[i], 2)

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

        # Limit to 60 frames per second
        clock.tick(60)

        menu.mainloop(events)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    quit()
