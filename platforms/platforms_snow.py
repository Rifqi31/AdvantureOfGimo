# name file : platforms_snow.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

# asset for tileset Intro Game and level 05
# for snow dirt
snow_dirt_wall = (770, 162, 140, 630)
snow_dirt_big_wall = (325, 162, 350, 630)
snow_dirt_intro = (0, 0, 770, 140)
snow_dirt_half = (231, 162, 70, 38)
snow_dirt_grass_basic = (231, 203, 70, 70)
snow_dirt_grass_rounded = (155, 162, 70, 70)
snow_dirt_tall_grass_left_right = (0, 308, 70, 350)
snow_dirt_grass_medium_tall = (75, 308, 70, 280)
snow_dirt_grass_short_tall = (155, 238, 70, 210)
snow_dirt_grass_medium_large = (0, 676, 280, 140)
snow_dirt_grass_up_down = (0, 829, 210, 70)
snow_dirt_grass_small_large = (0, 162, 140, 140)


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


class MovingPlatform_snow(Platform_snow):
    """ This is a fancier platform that can actually move. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or \
                self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
