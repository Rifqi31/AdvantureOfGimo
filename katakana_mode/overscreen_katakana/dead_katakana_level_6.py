# file name : dead_hiragana_level_6.py
# python version 3

# Import pygame and libraries
from pygame.locals import *
# import pygame module
import os
import pygame
import pygameMenu
from pygameMenu.locals import *
# import constants variable and main menu variable
import constants
# import game screen module
from game_screens import mainmenu
# import game settings module
from game_settings import configscreen, configsounds
# import hiragana mode level module
from katakana_mode.katakana_level_6 import (
    play_katakana_level_6
)


def show_game_over_katakana():
    clock = pygame.time.Clock()
    # stop the background music
    pygame.mixer.stop()
    # play game over music
    configsounds.game_over_sfx.play()
    configsounds.game_over_sfx.set_volume(0.5)

    game_over_screen = pygameMenu.Menu(
        configscreen.screen,
        dopause=False,
        font=pygameMenu.fonts.FONT_8BIT,
        font_size_title=30,
        font_title=pygameMenu.fonts.FONT_8BIT,
        menu_color_title=constants.BLUE,
        onclose=PYGAME_MENU_DISABLE_CLOSE,
        title='Game Over',
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(
            constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    game_over_screen.add_option('Retry', play_katakana_level_6.gameplay)
    game_over_screen.add_option('Main Menu', mainmenu.main_menu)
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
