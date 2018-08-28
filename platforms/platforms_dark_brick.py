# name file : platforms_dark_brick.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# asset for tileset level 02
brick_dark_wall = (0, 0, 140, 630)
brick_dark_big_wall = (374, 230, 280, 630)
brick_medium_short_land = (148, 0, 280, 70)
brick_medium_large_land = (146, 80, 210, 140)
brick_medium_long_land = (440, 0, 420, 70)
brick_medium_large_long_land = (368, 80, 280, 140)
brick_small_short_land = (224, 528, 140, 70)
brick_half_short_land = (662, 80, 140, 43)
brick_half_small_land = (815, 80, 70, 43)
brick_dark_grass_rounded = (146, 528, 70, 70)
brick_dark_small_stairs1 = (146, 374, 70, 140)
brick_dark_small_stairs2 = (218, 302, 70, 210)
brick_dark_small_stairs3 = (290, 230, 70, 280)
brick_large_high_land = (0, 687, 350, 210)


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


class MovingPlatform_dark_brick(Platform_dark_brick):
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
