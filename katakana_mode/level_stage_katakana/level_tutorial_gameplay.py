# name file: level_tutorial_gameplay.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_snow, platforms_item,
    platforms_special_enemy, platforms_enemy
    )

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


class Level_Tutorial_Gameplay(Level):
    """ This class for introduce the player
        for how to play the game"""

    def __init__(self, player):
        """ Create intro how to play """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms_snow.snow_dirt_wall, -140, 0],
                 [platforms_snow.snow_dirt_intro, 0, 460],
                 [platforms_snow.snow_dirt_big_wall, 769, 0]]

        special_enemy_pic = [[platforms_special_enemy.big_ogre_a, 67, 50]]
        enemy_pic = [[platforms_enemy.fat_frog, 70, 180]]
        health_pic = [[platforms_item.restore_health, 70, 260]]

        portal = [[platforms_item.portal_snow, 700, 380]]

        for platform in intro:
            block = platforms_snow.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms_snow.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # for tutorial purpose
        # for special enemy
        for platform in special_enemy_pic:
            special_eaten_A = platforms_special_enemy.Platform_special_enemy(platform[0])
            special_eaten_A.rect.x = platform[1]
            special_eaten_A.rect.y = platform[2]
            special_eaten_A.player = self.player
            self.special_enemy_icon_list.add(special_eaten_A)

        # for enemy
        for platform in enemy_pic:
            eaten = platforms_enemy.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.general_enemy_icon_list.add(eaten)

        # for health point
        for platform in health_pic:
            love_restore = platforms_item.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.health_icon_list.add(love_restore)
