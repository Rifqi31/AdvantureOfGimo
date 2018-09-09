# name file: level_02.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_dirt, platforms_bad_sprite,
    platforms_item, platforms_katakana,
    platforms_enemy, platforms_special_enemy
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create Level 2 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1096

        # Array with type of platform, and x, y location of the platform.
        # for level 02
        level02 = [
            [platforms_dirt.dirt_wall, -140, 0],
            [platforms_dirt.dirt_medium_long_land, 0, 460],
            [platforms_dirt.dirt_medium_short_land, 0, 92],
            [platforms_dirt.dirt_wall, 700, 100],
            [platforms_dirt.dirt_medium_short_land, 1050, 460],
            [platforms_dirt.dirt_medium_short_land, 1050, 180],
            [platforms_dirt.dirt_short_land, 1540, 460],
            [platforms_dirt.dirt_short_land, 1540, 180],
            [platforms_dirt.dirt_medium_short_land, 1890, 460],
            [platforms_dirt.dirt_big_wall, 2030, 0]
        ]

        water_level02 = [
            [platforms_bad_sprite.medium_long_water, 490, 531],
            [platforms_bad_sprite.medium_long_water, 840, 531],
            [platforms_bad_sprite.medium_long_water, 1330, 531],
            [platforms_bad_sprite.medium_long_water, 1680, 531]
        ]

        portal = [[platforms_item.portal_snow, 1960, 380]]

        love_health = [[platforms_item.restore_health, 1860, 380]]

        # true point
        katakana_u = [[platforms_katakana.katakana_u, 20, 10]]
        katakana_i = [[platforms_katakana.katakana_i, 850, 258]]
        katakana_o = [[platforms_katakana.katakana_o, 1280, 350]]
        katakana_a = [[platforms_katakana.katakana_a, 1400, 280]]
        katakana_e = [[platforms_katakana.katakana_e, 1400, 100]]

        # for special enemy
        special_enemy_u = [[platforms_special_enemy.big_ogre_u, 730, 2]]
        special_enemy_o = [[platforms_special_enemy.big_ogre_o, 1050, 75]]
        special_enemy_i = [[platforms_special_enemy.big_ogre_i, 1050, 350]]
        special_enemy_a = [[platforms_special_enemy.big_ogre_a, 1565, 75]]
        special_enemy_e = [[platforms_special_enemy.big_ogre_e, 1565, 350]]

        for platform in level02:
            block = platforms_dirt.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level02:
            water_suicide_lv2 = platforms_dirt.Platform_dirt(platform[0])
            water_suicide_lv2.rect.x = platform[1]
            water_suicide_lv2.rect.y = platform[2]
            water_suicide_lv2.player = self.player
            self.death_place_list_lv2.add(water_suicide_lv2)

        for platform in portal:
            gate = platforms_item.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms_item.Platform_hiragana_katakana(
                platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # True Point increease scores player
        # katakana U Point
        for platform in katakana_u:
            true_point_lv2 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.katakana_U_lv2.add(true_point_lv2)

        # katakana I
        for platform in katakana_i:
            true_point_lv2 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.katakana_I_lv2.add(true_point_lv2)

        # katakana O
        for platform in katakana_o:
            true_point_lv2 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.katakana_O.add(true_point_lv2)

        # katakana a
        for platform in katakana_a:
            true_point_lv2 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.katakana_A_lv2.add(true_point_lv2)

        # katakana e
        for platform in katakana_e:
            true_point_lv2 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.katakana_E.add(true_point_lv2)

        # for special enemy
        # katakana U
        for platform in special_enemy_u:
            special_eaten_U_lv2 = \
                platforms_special_enemy.Platform_special_enemy(platform[0])
            special_eaten_U_lv2.rect.x = platform[1]
            special_eaten_U_lv2.rect.y = platform[2]
            special_eaten_U_lv2.player = self.player
            self.special_enemy_list_U_lv2.add(special_eaten_U_lv2)

        # katakana O
        for platform in special_enemy_o:
            special_eaten_O = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_O.rect.x = platform[1]
            special_eaten_O.rect.y = platform[2]
            special_eaten_O.player = self.player
            self.special_enemy_list_O.add(special_eaten_O)

        # katakana I
        for platform in special_enemy_i:
            special_eaten_I_lv2 = \
                platforms_special_enemy.Platform_special_enemy(platform[0])
            special_eaten_I_lv2.rect.x = platform[1]
            special_eaten_I_lv2.rect.y = platform[2]
            special_eaten_I_lv2.player = self.player
            self.special_enemy_list_I_lv2.add(special_eaten_I_lv2)

        # katakana A
        for platform in special_enemy_a:
            special_eaten_A_lv2 = \
                platforms_special_enemy.Platform_special_enemy(platform[0])
            special_eaten_A_lv2.rect.x = platform[1]
            special_eaten_A_lv2.rect.y = platform[2]
            special_eaten_A_lv2.player = self.player
            self.special_enemy_list_A_lv2.add(special_eaten_A_lv2)

        # katakana E
        for platform in special_enemy_e:
            special_eaten_E = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_E.rect.x = platform[1]
            special_eaten_E.rect.y = platform[2]
            special_eaten_E.player = self.player
            self.special_enemy_list_E.add(special_eaten_E)

        # add moving sprites
        block = platforms_dirt.MovingPlatform_dirt(
            platforms_dirt.dirt_grass_rounded)
        block.rect.x = 560
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms_dirt.MovingPlatform_dirt(
            platforms_dirt.dirt_grass_rounded)
        block.rect.x = 910
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemy
        eaten_lv2 = platforms_enemy.MovingEnemy(platforms_enemy.bad_ogre)
        eaten_lv2.rect.x = 200
        eaten_lv2.rect.y = 400
        eaten_lv2.boundary_left = 200
        eaten_lv2.boundary_right = 450
        eaten_lv2.change_x = 5
        eaten_lv2.player = self.player
        eaten_lv2.level = self
        self.enemy_list_lv2.add(eaten_lv2)

        eaten_lv2 = platforms_enemy.MovingEnemy(platforms_enemy.bad_ogre)
        eaten_lv2.rect.x = 70
        eaten_lv2.rect.y = 30
        eaten_lv2.boundary_left = 70
        eaten_lv2.boundary_right = 230
        eaten_lv2.change_x = 3
        eaten_lv2.player = self.player
        eaten_lv2.level = self
        self.enemy_list_lv2.add(eaten_lv2)

        eaten_lv2 = platforms_enemy.MovingEnemy(platforms_enemy.bad_ogre)
        eaten_lv2.rect.x = 1160
        eaten_lv2.rect.y = 120
        eaten_lv2.boundary_left = 1160
        eaten_lv2.boundary_right = 1300
        eaten_lv2.change_x = 3
        eaten_lv2.player = self.player
        eaten_lv2.level = self
        self.enemy_list_lv2.add(eaten_lv2)

        eaten_lv2 = platforms_enemy.MovingEnemy(platforms_enemy.bad_ogre)
        eaten_lv2.rect.x = 1160
        eaten_lv2.rect.y = 400
        eaten_lv2.boundary_left = 1160
        eaten_lv2.boundary_right = 1300
        eaten_lv2.change_x = 3
        eaten_lv2.player = self.player
        eaten_lv2.level = self
        self.enemy_list_lv2.add(eaten_lv2)
