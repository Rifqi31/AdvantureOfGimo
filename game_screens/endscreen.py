# file name : endscreen.py
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
# import game screen module
from game_screens import mainmenu
# import hiragana & katakana main modul
from game_settings import configscreen, configsounds
# hiragana mode
from hiragana_mode.hiragana_level_1 import (
    play_hiragana_level_1
)
# katakana mode
from katakana_mode.katakana_level_1 import (
    play_katakana_level_1
)

def show_end_screen_hiragana():
    clock = pygame.time.Clock()
    # stop the background music
    pygame.mixer.stop()
    # play game over music
    configsounds.ending_music.play()
    configsounds.ending_music.set_volume(0.5)

    end_game_screen = pygameMenu.Menu(
        configscreen.screen,
        dopause=False,
        font=pygameMenu.fonts.FONT_8BIT,
        font_size_title=30,
        font_title=pygameMenu.fonts.FONT_8BIT,
        menu_color_title=constants.BLUE,
        onclose=PYGAME_MENU_DISABLE_CLOSE,
        title='Congratulations',
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(
            constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    end_game_screen.add_option('Retry', play_hiragana_level_1.gameplay)
    end_game_screen.add_option('Main Menu', mainmenu.main_menu)
    end_game_screen.add_option('Exit Game', PYGAME_MENU_EXIT)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        end_game_screen.mainloop(events)

        # Flip surface
        pygame.display.flip()


def show_end_screen_katakana():
    clock = pygame.time.Clock()
    # stop the background music
    pygame.mixer.stop()
    # play game over music
    configsounds.ending_music.play()
    configsounds.ending_music.set_volume(0.5)

    end_game_screen = pygameMenu.Menu(
        configscreen.screen,
        dopause=False,
        font=pygameMenu.fonts.FONT_8BIT,
        font_size_title=30,
        font_title=pygameMenu.fonts.FONT_8BIT,
        menu_color_title=constants.BLUE,
        onclose=PYGAME_MENU_DISABLE_CLOSE,
        title='Congratulations',
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    end_game_screen.add_option('Retry', play_katakana_level_1.gameplay)
    end_game_screen.add_option('Main Menu', mainmenu.main_menu)
    end_game_screen.add_option('Exit Game', PYGAME_MENU_EXIT)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        end_game_screen.mainloop(events)

        # Flip surface
        pygame.display.flip()
