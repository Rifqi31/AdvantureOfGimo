# name file : platforms_red_brick.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# asset for tileset level 03 and level 04
brick_red_wall = (0, 0, 140, 630)
brick_red_big_wall = (625, 0, 280, 630)
brick_red_medium_tall = (147, 0, 140, 210)
brick_red_medium_short_land = (294, 0, 140, 70)
brick_red_medium_long_land = (294, 76, 280, 70)
brick_red_small_half = (521, 0, 70, 45)
brick_red_snow_small_half = (441, 151, 72, 45)
brick_red_grass_left_right_long = (147, 221, 70, 420)
brick_red_medium_high_land = (221, 221, 70, 140)
brick_red_medium_high_large_land = (297, 226, 210, 140)
brick_red_snow_medium_short_land = (297, 373, 210, 70)
brick_red_snow_high_small_left_right = (219, 515, 74, 144)
brick_red_snow_medium_short_land = (0, 675, 280, 70)
brick_red_medium_bottom = (0, 749, 280, 70)
brick_red_medium_short_grass_snow = (0, 823, 210, 70)
brick_basic = (219, 824, 70, 70)
brick_red_grass_snow_medium_land = (626, 675, 280, 70)
brick_red_grass_rounded = (443, 0, 70, 70)


class Platform_grass_brick(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # brick grass tileset
        sprite_sheet_red_brick = SpriteSheet(
            "spritesheet/brick_red_castle.png")

        # Grab the omage for this platform
        self.image = sprite_sheet_red_brick.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()


class MovingPlatform_brick_red(Platform_grass_brick):
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
