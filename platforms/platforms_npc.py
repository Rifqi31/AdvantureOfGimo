# name file : platforms_npc.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet

# for NPC
grandpa_magus = (5, 4, 63, 90)
himesama_blonde = (157, 20, 51, 74)
text_grandpa = (28, 121, 169, 10)
text_himesama = (31, 108, 77, 11)


class Platform_NPC(pygame.sprite.Sprite):
    """ Platform for enemy """

    def __init__(self, sprite_sheet_data):

        super().__init__()

        # enemy tileset
        sprite_sheet_enemys = SpriteSheet("spritesheet/npc_asset.png")

        # Grab the image for this platform
        self.image = sprite_sheet_enemys.get_image(
            sprite_sheet_data[0],
            sprite_sheet_data[1],
            sprite_sheet_data[2],
            sprite_sheet_data[3]
        )

        self.rect = self.image.get_rect()
