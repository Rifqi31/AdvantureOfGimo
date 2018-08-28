# name file : platforms_lava_rock.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# asset for tileset level 08
lava_rock_wall = (0, 0, 140, 630)
lava_rock_small_tall = (145, 362, 70, 210)
lava_rock_medium_tall = (145, 0, 70, 350)
lava_rock_long_tall = (218, 0, 70, 490)
lava_rock_medium_large_land = (292, 0, 280, 210)
lava_rock_short_small_land = (292, 219, 210, 140)
lava_rock_tall_small_land = (292, 366, 210, 210)
lava_rock_basic = (145, 583, 70, 70)
lava_rock_basic_medium = (292, 586, 140, 70)
lava_rock_half = (439, 586, 72, 38)
lava_rock_big_wall = (626, 0, 280, 630)


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


class MovingPlatform_lava_rock(Platform_lava_rock):
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
