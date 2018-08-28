# name file : platforms_hiragana.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# for hiragana
# hiragana symbol
# vocal
hiragana_a = (0, 0, 70, 70)
hiragana_i = (0, 72, 70, 70)
hiragana_u = (0, 146, 70, 70)
hiragana_e = (0, 219, 70, 70)
hiragana_o = (0, 292, 70, 70)

# vocal K
hiragana_ka = (73, 0, 70, 70)
hiragana_ki = (73, 73, 70, 70)
hiragana_ku = (73, 146, 70, 70)
hiragana_ke = (73, 219, 70, 70)
hiragana_ko = (73, 292, 70, 70)

# vocal S
hiragana_sa = (146, 0, 70, 70)
hiragana_si = (146, 73, 70, 70)
hiragana_su = (146, 146, 70, 70)
hiragana_se = (146, 219, 70, 70)
hiragana_so = (146, 292, 70, 70)

# vocal T
hiragana_ta = (219, 0, 70, 70)
hiragana_ti = (219, 73, 70, 70)
hiragana_tu = (219, 146, 70, 70)
hiragana_te = (219, 219, 70, 70)
hiragana_to = (219, 292, 70, 70)

# vocal N
hiragana_na = (292, 0, 70, 70)
hiragana_ni = (292, 73, 70, 70)
hiragana_nu = (292, 146, 70, 70)
hiragana_ne = (292, 219, 70, 70)
hiragana_no = (292, 292, 70, 70)

# vocal H
hiragana_ha = (365, 0, 70, 70)
hiragana_hi = (365, 73, 70, 70)
hiragana_hu = (365, 146, 70, 70)
hiragana_he = (365, 219, 70, 70)
hiragana_ho = (365, 292, 70, 70)

# vocal M
hiragana_ma = (438, 0, 70, 70)
hiragana_mi = (438, 73, 70, 70)
hiragana_mu = (438, 146, 70, 70)
hiragana_me = (438, 219, 70, 70)
hiragana_mo = (438, 292, 70, 70)

# vocal Y
hiragana_ya = (511, 0, 70, 70)
hiragana_yu = (511, 73, 70, 70)
hiragana_yo = (511, 146, 70, 70)

# vocal R
hiragana_ra = (584, 0, 70, 70)
hiragana_ri = (584, 73, 70, 70)
hiragana_ru = (584, 146, 70, 70)
hiragana_re = (584, 219, 70, 70)
hiragana_ro = (584, 292, 70, 70)

# vocal W
hiragana_wa = (657, 0, 70, 70)
hiragana_wo = (657, 73, 70, 70)

# vocal N
hiragana_n = (730, 0, 70, 70)


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
