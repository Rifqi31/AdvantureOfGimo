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
# for tutorial
from tutorial_mode import platform_scroller_tutorial
# import level hiragana
from hiragana_mode.hiragana_level_1 import (
    play_hiragana_level_1
)
from hiragana_mode.hiragana_level_2 import (
    play_hiragana_level_2
)
from hiragana_mode.hiragana_level_3 import (
    play_hiragana_level_3
)
from hiragana_mode.hiragana_level_4 import (
    play_hiragana_level_4
)
from hiragana_mode.hiragana_level_5 import (
    play_hiragana_level_5
)
from hiragana_mode.hiragana_level_6 import (
    play_hiragana_level_6
)
from hiragana_mode.hiragana_level_7 import (
    play_hiragana_level_7
)
from hiragana_mode.hiragana_level_8 import (
    play_hiragana_level_8
)
from hiragana_mode.hiragana_level_9 import (
    play_hiragana_level_9
)
from hiragana_mode.hiragana_level_10 import (
    play_hiragana_level_10
)
from hiragana_mode.hiragana_level_11 import (
    play_hiragana_level_11
)


# import level katakana
from katakana_mode.katakana_level_1 import (
    play_katakana_level_1
)
from katakana_mode.katakana_level_2 import (
    play_katakana_level_2
)
from katakana_mode.katakana_level_3 import (
    play_katakana_level_3
)
from katakana_mode.katakana_level_4 import (
    play_katakana_level_4
)
from katakana_mode.katakana_level_5 import (
    play_katakana_level_5
)
from katakana_mode.katakana_level_6 import (
    play_katakana_level_6
)
from katakana_mode.katakana_level_7 import (
    play_katakana_level_7
)
from katakana_mode.katakana_level_8 import (
    play_katakana_level_8
)
from katakana_mode.katakana_level_9 import (
    play_katakana_level_9
)
from katakana_mode.katakana_level_10 import (
    play_katakana_level_10
)
from katakana_mode.katakana_level_11 import (
    play_katakana_level_11
)


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

    control_menu = pygameMenu.TextMenu(
        configscreen.screen,
        bgfun=main_background,
        font=pygameMenu.fonts.FONT_NEVIS,
        font_size_title=30,
        font_title=pygameMenu.fonts.FONT_8BIT,
        menu_color_title=constants.BLUE,
        onclose=PYGAME_MENU_CLOSE,
        text_fontsize=20,
        font_size=30,
        title='Control',
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    control_menu.add_option('Back', PYGAME_MENU_BACK)
    for m in constants.HELP:
        control_menu.add_line(m)
    control_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

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
    option_menu.add_option('Control', control_menu)
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


# about menu
def about_menu():
    """ Function for About Menu """
    clock = pygame.time.Clock()

    # About Menu
    contact_menu = pygameMenu.TextMenu(
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
        title='Contact',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    for m in constants.CONTACT:
        contact_menu.add_line(m)
        contact_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
    contact_menu.add_option('Return to Menu', PYGAME_MENU_BACK)

    credits_menu = pygameMenu.TextMenu(
        configscreen.screen,
        bgfun=main_background,
        font=pygameMenu.fonts.FONT_NEVIS,
        font_size_title=30,
        font_title=pygameMenu.fonts.FONT_8BIT,
        menu_color_title=constants.BLUE,
        onclose=PYGAME_MENU_CLOSE,
        text_fontsize=20,
        font_size=30,
        title='Credits',
        menu_height=int(constants.SCREEN_HEIGHT * 0.6),
        menu_width=int(constants.SCREEN_WIDTH * 0.6),
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    for m in constants.CREDITS:
        credits_menu.add_line(m)
        credits_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
    credits_menu.add_option('Back', PYGAME_MENU_BACK)

    # select about Menu
    select_about_menu = pygameMenu.Menu(
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
        title='About',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    select_about_menu.add_option(contact_menu.get_title(), contact_menu)
    select_about_menu.add_option(credits_menu.get_title(), credits_menu)
    select_about_menu.add_option('Back', main_menu)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_about_menu.mainloop(events)

        # Flip surface
        pygame.display.flip()


# select level hiragana
def select_level_hiragana_display1():
    """ Function for Select level in hiragana mode"""
    clock = pygame.time.Clock()

    # Display Menu
    select_level_hiragana_page1 = pygameMenu.Menu(
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
        title='Select Levels',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    # LEVEL PAGE 1
    select_level_hiragana_page1.add_option(
        'Level 01 ', play_hiragana_level_1.gameplay)
    select_level_hiragana_page1.add_option(
        'Level 02', play_hiragana_level_2.gameplay)
    select_level_hiragana_page1.add_option(
        'Level 03', play_hiragana_level_3.gameplay)
    select_level_hiragana_page1.add_option(
        'Level 04', play_hiragana_level_4.gameplay)
    select_level_hiragana_page1.add_option(
        'Next', select_level_hiragana_display2)
    select_level_hiragana_page1.add_option(
        'Back', play_menu)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_level_hiragana_page1.mainloop(events)

        # Flip surface
        pygame.display.flip()


def select_level_hiragana_display2():
    """ Function for Select level in hiragana mode"""
    clock = pygame.time.Clock()

    select_level_hiragana_page2 = pygameMenu.Menu(
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
        title='Select Levels',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    # LEVEL PAGE 2
    select_level_hiragana_page2.add_option(
        'Level 05', play_hiragana_level_5.gameplay)
    select_level_hiragana_page2.add_option(
        'Level 06', play_hiragana_level_6.gameplay)
    select_level_hiragana_page2.add_option(
        'Level 07', play_hiragana_level_7.gameplay)
    select_level_hiragana_page2.add_option(
        'Level 08', play_hiragana_level_8.gameplay)
    select_level_hiragana_page2.add_option(
        'Level 09', play_hiragana_level_9.gameplay)
    select_level_hiragana_page2.add_option(
        'Next', select_level_hiragana_display3)
    select_level_hiragana_page2.add_option(
        'Back', select_level_hiragana_display1)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_level_hiragana_page2.mainloop(events)

        # Flip surface
        pygame.display.flip()


def select_level_hiragana_display3():
    """ Function for Select level in hiragana mode"""
    clock = pygame.time.Clock()

    select_level_hiragana_page3 = pygameMenu.Menu(
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
        title='Select Levels',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    # LEVEL PAGE 3
    select_level_hiragana_page3.add_option(
        'Level 10', play_hiragana_level_10.gameplay)
    select_level_hiragana_page3.add_option(
        'Level 11', play_hiragana_level_11.gameplay)
    select_level_hiragana_page3.add_option(
        'Back', select_level_hiragana_display2)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_level_hiragana_page3.mainloop(events)

        # Flip surface
        pygame.display.flip()


# select level katakana
def select_level_katakana_display1():
    """ Function for Select level in katakana mode"""
    clock = pygame.time.Clock()

    # Display Menu
    select_level_katakana_page1 = pygameMenu.Menu(
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
        title='Select Levels',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )
    # LEVEL PAGE 1
    select_level_katakana_page1.add_option(
        'Level 01 ', play_katakana_level_1.gameplay)
    select_level_katakana_page1.add_option(
        'Level 02', play_katakana_level_2.gameplay)
    select_level_katakana_page1.add_option(
        'Level 03', play_katakana_level_3.gameplay)
    select_level_katakana_page1.add_option(
        'Level 04', play_katakana_level_4.gameplay)
    select_level_katakana_page1.add_option(
        'Next', select_level_katakana_display2)
    select_level_katakana_page1.add_option(
        'Back', play_menu)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_level_katakana_page1.mainloop(events)

        # Flip surface
        pygame.display.flip()


def select_level_katakana_display2():
    """ Function for Select level in katakana mode"""
    clock = pygame.time.Clock()

    select_level_katakana_page2 = pygameMenu.Menu(
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
        title='Select Levels',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    # LEVEL PAGE 2
    select_level_katakana_page2.add_option(
        'Level 05', play_katakana_level_5.gameplay)
    select_level_katakana_page2.add_option(
        'Level 06', play_katakana_level_6.gameplay)
    select_level_katakana_page2.add_option(
        'Level 07', play_katakana_level_7.gameplay)
    select_level_katakana_page2.add_option(
        'Level 08', play_katakana_level_8.gameplay)
    select_level_katakana_page2.add_option(
        'Level 09', play_katakana_level_9.gameplay)
    select_level_katakana_page2.add_option(
        'Next', select_level_katakana_display3)
    select_level_katakana_page2.add_option(
        'Back', select_level_katakana_display1)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_level_katakana_page2.mainloop(events)

        # Flip surface
        pygame.display.flip()


def select_level_katakana_display3():
    """ Function for Select level in katakana mode"""
    clock = pygame.time.Clock()

    select_level_katakana_page3 = pygameMenu.Menu(
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
        title='Select Levels',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    # LEVEL PAGE 3
    select_level_katakana_page3.add_option(
        'Level 10', play_katakana_level_10.gameplay)
    select_level_katakana_page3.add_option(
        'Level 11', play_katakana_level_11.gameplay)
    select_level_katakana_page3.add_option(
        'Back', select_level_katakana_display2)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        select_level_katakana_page3.mainloop(events)

        # Flip surface
        pygame.display.flip()


# play menu
def play_menu():
    """ Function for Play Menu """
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
    # play_menu.add_option('Hiragana', platform_scroller_hiragana.gameplay)
    play_menu.add_option('Hiragana', select_level_hiragana_display1)
    play_menu.add_option('Katakana', select_level_katakana_display1)
    play_menu.add_option('Back', main_menu)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        play_menu.mainloop(events)

        # Flip surface
        pygame.display.flip()


# confirm exit
def confirm_exit():
    """ Function for Exit Confirmation """
    # set clock
    clock = pygame.time.Clock()

    confirm_exit = pygameMenu.Menu(
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
        title='Are You Sure',
        window_height=constants.SCREEN_HEIGHT,
        window_width=constants.SCREEN_WIDTH
    )

    confirm_exit.add_option('Yes', PYGAME_MENU_EXIT)
    confirm_exit.add_option('No', main_menu)

    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

        # Main menu
        confirm_exit.mainloop(events)

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

    # stop the background music
    pygame.mixer.stop()

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
    main_menu.add_option('How To Play', platform_scroller_tutorial.gameplay)
    main_menu.add_option('Option', option_menu)
    main_menu.add_option('About', about_menu)
    main_menu.add_option('Exit', confirm_exit)

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
