# name file : platforms_sand_dirt.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# asset for tileset level 06
sand_dirt_wall = (0, 0, 140, 630)
sand_dirt_medium_long_land = (146, 0, 350, 140)
sand_dirt_tall_small = (512, 0, 70, 210)
sand_dirt_tall_large_medium = (146, 147, 140, 210)
sand_dirt_half = (295, 147, 72, 34)
sand_dirt_tall_long = (434, 147, 70, 350)
sand_dirt_tall_medium = (512, 221, 70, 280)
sand_dirt_basic_medium = (145, 584, 140, 70)
sand_dirt_long_soft_up_down = (0, 676, 560, 70)
sand_dirt_medium_small_land = (0, 751, 280, 140)
sand_dirt_big_wall = (626, 0, 280, 630)


class Platform_dirt_sand(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # brick grass tileset
        sprite_sheet_red_brick = SpriteSheet(
            "spritesheet/sand_tiles_assets.png")

        # Grab the omage for this platform
        self.image = sprite_sheet_red_brick.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()


class MovingPlatform_dirt_sand(Platform_dirt_sand):
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
