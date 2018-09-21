# name file: level_tutorial_kill_special.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_snow, 
    platforms_item, 
    platforms_bad_sprite,
    platforms_enemy,
    platforms_special_enemy,
    platforms_hiragana,
)

# import levels module
from hiragana_mode.level_stage_hiragana.levels import Level


# for NPC section
class Level_Tutorial_Kill_Special(Level):
    """This class for introduce for player how to play this game"""

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [
            [platforms_snow.snow_dirt_wall, -140, 0],
            [platforms_snow.snow_dirt_grass_medium_large, 0, 530],
            [platforms_snow.snow_dirt_grass_medium_large, 280, 530],
            [platforms_snow.snow_dirt_grass_medium_large, 490, 460],
            [platforms_snow.snow_dirt_big_wall, 769, 0]
        ]
        
        hiragana_a = [[platforms_hiragana.hiragana_a, 360, 320]]
        hiragana_u = [[platforms_hiragana.hiragana_u, 250, 320]]


        portal = [[platforms_item.portal_snow, 700, 380]]

        for platform in intro:
            block = platforms_snow.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms_item.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # True Point increease scores player
        # Hiragana A Point
        for platform in hiragana_a:
            true_point_lv1 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv1.rect.x = platform[1]
            true_point_lv1.rect.y = platform[2]
            true_point_lv1.player = self.player
            self.hiragana_A.add(true_point_lv1)
        
        # False point decrease health player
        # Hiragana U Point
        for platform in hiragana_u:
            false_point_lv1 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            false_point_lv1.rect.x = platform[1]
            false_point_lv1.rect.y = platform[2]
            false_point_lv1.player = self.player
            self.hiragana_U.add(false_point_lv1)

        # add moving special enemys
        special_eaten_A = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.big_ogre_a)
        special_eaten_A.rect.x = 490
        special_eaten_A.rect.y = 350
        special_eaten_A.boundary_left = 490
        special_eaten_A.boundary_right = 630
        special_eaten_A.change_x = 2
        special_eaten_A.player = self.player
        special_eaten_A.level = self
        self.special_enemy_list_A.add(special_eaten_A)