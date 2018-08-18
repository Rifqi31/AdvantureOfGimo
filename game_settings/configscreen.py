# file name : configscreen.py
# python version 3

import pygame
import constants

pygame.init()

# Set the height and width of the screen
size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)


# ----- For Display Settings -----
def fullscreen_settings():
    """ This function for fullscreen settings """
    pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.FULLSCREEN)


def windowed_settings():
    """ This function for windowed screen settings """
    pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
