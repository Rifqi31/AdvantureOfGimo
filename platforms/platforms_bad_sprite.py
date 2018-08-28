# name file : platforms_bad_sprite.py
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

# death sprite water
small_water = (591, 0, 70, 70)
medium_short_water = (592, 73, 140, 70)
medium_long_water = (665, 0, 210, 70)

# death sprite rock
medium_sharp_rock = (662, 126, 210, 70)
small_sharp_rock = (667, 188, 140, 70)

# death sprite lava
lava_water = (511, 219, 72, 70)
lava_water_long = (0, 676, 216, 70)
lava_water_medium = (221, 676, 144, 70)


class Platform_dirt(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # dirt tileset
        sprite_sheet_dirt = SpriteSheet("spritesheet/dirt_tile_assets.png")

        # Grab the image for this platform
        self.image = sprite_sheet_dirt.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()


class Platform_dark_brick(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # dirt tileset
        sprite_sheet_dirt = SpriteSheet("spritesheet/brick_castle_night.png")

        # Grab the image for this platform
        self.image = sprite_sheet_dirt.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()

class Platform_lava_rock(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # brick grass tileset
        sprite_sheet_red_brick = SpriteSheet(
            "spritesheet/lava_tile_assets.png")

        # Grab the omage for this platform
        self.image = sprite_sheet_red_brick.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()
