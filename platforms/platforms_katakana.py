# name file : platforms_katakana.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet


# for Katakana
# Katakana Symbol
katakana_a = (0, 438, 70, 70)
katakana_i = (0, 511, 70, 70)
katakana_u = (0, 584, 70, 70)
katakana_e = (0, 657, 70, 70)
katakana_o = (0, 730, 70, 70)

# vocal K
katakana_ka = (73, 438, 70, 70)
katakana_ki = (73, 511, 70, 70)
katakana_ku = (73, 584, 70, 70)
katakana_ke = (73, 657, 70, 70)
katakana_ko = (73, 730, 70, 70)

# vocal S
katakana_sa = (146, 438, 70, 70)
katakana_si = (146, 511, 70, 70)
katakana_su = (146, 584, 70, 70)
katakana_se = (146, 657, 70, 70)
katakana_so = (146, 730, 70, 70)

# vocal T
katakana_ta = (219, 438, 70, 70)
katakana_ti = (219, 511, 70, 70)
katakana_tu = (219, 584, 70, 70)
katakana_te = (219, 657, 70, 70)
katakana_to = (219, 730, 70, 70)

# vocal N
katakana_na = (292, 438, 70, 70)
katakana_ni = (292, 511, 70, 70)
katakana_nu = (292, 584, 70, 70)
katakana_ne = (292, 657, 70, 70)
katakana_no = (292, 730, 70, 70)

# vocal H
katakana_ha = (365, 438, 70, 70)
katakana_hi = (365, 511, 70, 70)
katakana_hu = (365, 584, 70, 70)
katakana_he = (365, 657, 70, 70)
katakana_ho = (365, 730, 70, 70)

# vocal M
katakana_ma = (438, 438, 70, 70)
katakana_mi = (438, 511, 70, 70)
katakana_mu = (438, 584, 70, 70)
katakana_me = (438, 657, 70, 70)
katakana_mo = (438, 730, 70, 70)

# vocal Y
katakana_ya = (584, 438, 70, 70)
katakana_yu = (584, 511, 70, 70)
katakana_yo = (584, 484, 70, 70)

# vocal R
katakana_ra = (511, 438, 70, 70)
katakana_ri = (511, 511, 70, 70)
katakana_ru = (511, 484, 70, 70)
katakana_re = (511, 657, 70, 70)
katakana_ro = (511, 730, 70, 70)

# vocal W
katakana_wa = (657, 438, 70, 70)
katakana_wo = (657, 511, 70, 70)

# vocal N
katakana_n = (730, 438, 70, 70)


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
