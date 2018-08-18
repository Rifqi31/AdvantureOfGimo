# name file : spritesheet_function.py
# python version 3

# this file for pull sprites from file sprite sheet

# import pygame module
import pygame
# import contstant file
import constants


class SpriteSheet(object):
    """ Put an all images from sprite sheets """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        # Load the sprite sheet.
        # self.sprite_sheet = pygame.image.load(file_name).convert()
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image
