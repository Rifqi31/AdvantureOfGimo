# file name : mainmenu.py
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
# import game settings module
from game_settings import configscreen
# import hiragana & katakana main module
from hiragana_mode import platform_scroller_hiragana
from katakana_mode import platform_scroller_katakana


def main_background():
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    background_position = [0, 0]
    background_image = pygame.image.load(
        "spritesheet/menu_background.png").convert_alpha()
    configscreen.screen.blit(background_image, background_position)

# Option Menu


def option_menu():
    """ Function for Option Menu """
    clock = pygame.time.Clock()

    # Display Menu
    display_menu = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )
    display_menu.add_option('Windowed', configscreen.windowed_settings)
    display_menu.add_option('Fullscreen', configscreen.fullscreen_settings)
    display_menu.add_option('Return to Option', PYGAME_MENU_BACK)

    # Option Menu
    option_menu = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )
    option_menu.add_option('Display', display_menu)
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
    # hide mouse cursor
    pygame.mouse.set_visible(False)

    # set clock
    clock = pygame.time.Clock()

    # Play Menu
    play_menu = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )
    play_menu.add_option('Hiragana', platform_scroller_hiragana.gameplay)
    play_menu.add_option('Katakana', platform_scroller_katakana.gameplay)
    play_menu.add_option('Back', PYGAME_MENU_BACK)

    # About Menu
    about_menu = pygameMenu.TextMenu(
        configscreen.screen,
        bgfun=main_background,
        color_selected=constants.WHITE,
        font=pygameMenu.fonts.FONT_NEVIS,
        font_color=constants.DARK_GRASS_GREEN,
        font_size_title=30,
        font_title=pygameMenu.fonts.FONT_8BIT,
        menu_color=constants.LIGHT_BROWN_DIRT,
        menu_color_title=constants.LIGHT_GREEN,
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(constants.SCREEN_WIDTH * 0.6),
        onclose=PYGAME_MENU_DISABLE_CLOSE,
        option_shadow=False,
        text_color=constants.WHITE,
        text_fontsize=15,
        font_size=30,
        title='About',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    for m in constants.ABOUT:
        about_menu.add_line(m)
        about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
    about_menu.add_option('Return to Menu', PYGAME_MENU_BACK)

    # Core Menu
    main_menu = pygameMenu.Menu(
        configscreen.screen,
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
        window_width=constants.SCREEN_WIDTH
    )

    main_menu.add_option('Play', play_menu)
    main_menu.add_option('Option', option_menu)
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
