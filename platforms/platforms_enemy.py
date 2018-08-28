# name file : platforms_enemy.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# for enemys
skull_ghost = (10, 5, 42, 51)
fat_frog = (62, 7, 49, 49)
old_skull = (122, 7, 31, 49)
dark_bat = (158, 8, 57, 48)
orange_slime = (14, 60, 33, 33)
bad_mushroom = (65, 60, 42, 42)
bad_octo = (122, 60, 31, 33)
bad_ogre = (167, 60, 39, 42)


class Platform_enemy(pygame.sprite.Sprite):
    """ Platform for enemy """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # enemy tileset
        sprite_sheet_enemys = SpriteSheet("spritesheet/enemy.png")

        # Grab the image for this platform
        self.image = sprite_sheet_enemys.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()

# for prototype


class MovingEnemy(Platform_enemy):
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

        # Move up/down
        self.rect.y += self.change_y

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or \
                self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
