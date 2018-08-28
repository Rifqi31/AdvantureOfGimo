# name file : platforms_item.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# portal
portal_snow = (219, 511, 70, 70)

# restore health
restore_health = (730, 732, 45, 39)


class Platform_snow(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # dirt tileset
        sprite_sheet_dirt = SpriteSheet("spritesheet/snow_tile_assets.png")

        # Grab the image for this platform
        self.image = sprite_sheet_dirt.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()


class Platform_hiragana_katakana(pygame.sprite.Sprite):
    """ Platform the user can take the point """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # hiragana&katakana tileset
        sprite_sheet_wibu = SpriteSheet(
            "spritesheet/hiragana_katakana_tileset.png")

        # Grab the image for this platform
        self.image = sprite_sheet_wibu.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()
