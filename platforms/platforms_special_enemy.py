# name file : platforms.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# special enemys
# basic vokal
big_ogre_a = (5, 5, 65, 109)
big_ogre_i = (79, 5, 65, 109)
big_ogre_u = (152, 5, 65, 109)
big_ogre_e = (225, 5, 65, 109)
big_ogre_o = (301, 5, 65, 109)

# Vocal K
dark_rabbit_ka = (5, 117, 71, 108)
dark_rabbit_ki = (79, 117, 71, 108)
dark_rabbit_ku = (152, 117, 71, 108)
dark_rabbit_ke = (225, 117, 71, 108)
dark_rabbit_ko = (301, 117, 71, 108)

# Vocal S
orange_slime_sa = (5, 234, 80, 99)
orange_slime_si = (88, 234, 80, 99)
orange_slime_su = (170, 234, 80, 99)
orange_slime_se = (254, 234, 80, 99)
orange_slime_so = (336, 234, 80, 99)

# vocal T
big_ogre_ta = (380, 5, 65, 109)
big_ogre_ti = (452, 5, 65, 109)
big_ogre_tu = (523, 5, 65, 109)
big_ogre_te = (596, 5, 65, 109)
big_ogre_to = (670, 5, 65, 109)

# Vocal N
dark_rabbit_na = (380, 117, 71, 108)
dark_rabbit_ni = (452, 117, 71, 108)
dark_rabbit_nu = (523, 117, 71, 108)
dark_rabbit_ne = (596, 117, 71, 108)
dark_rabbit_no = (670, 117, 71, 108)

# Vocal H
orange_slime_ha = (420, 234, 80, 99)
orange_slime_hi = (504, 234, 80, 99)
orange_slime_hu = (588, 234, 80, 99)
orange_slime_he = (674, 234, 80, 99)
orange_slime_ho = (758, 234, 80, 99)

# Vocal M
zombie_skull_ma = (5, 348, 65, 96)
zombie_skull_mi = (79, 348, 65, 96)
zombie_skull_mu = (152, 348, 65, 96)
zombie_skull_me = (223, 348, 65, 96)
zombie_skull_mo = (297, 348, 65, 96)

# Vocal Yo
zombie_skull_ya = (372, 348, 65, 96)
zombie_skull_yu = (445, 348, 65, 96)
zombie_skull_yo = (517, 348, 65, 96)

# Vocal R
slime_lava_ra = (5, 456, 80, 99)
slime_lava_ri = (91, 456, 80, 99)
slime_lava_ru = (176, 456, 80, 99)
slime_lava_re = (260, 456, 80, 99)
slime_lava_ro = (344, 456, 80, 99)

# Vocal W
slime_lava_wa = (430, 456, 80, 99)
slime_lava_wo = (517, 456, 80, 99)

# Vocal N
slime_lava_n = (603, 456, 80, 99)


class Platform_special_enemy(pygame.sprite.Sprite):
    """ Platform for enemy """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # enemy tileset
        sprite_sheet_enemys = SpriteSheet(
            "spritesheet/special_enemy_characters.png")

        # Grab the image for this platform
        self.image = sprite_sheet_enemys.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()

# for special enemy


class MovingEnemySpecial(Platform_special_enemy):
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
