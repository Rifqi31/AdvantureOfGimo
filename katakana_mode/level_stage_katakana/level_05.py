# name file: level_05.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_red_brick, platforms_bad_sprite,
    platforms_item, platforms_special_enemy,
    platforms_katakana, platforms_enemy
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_05(Level):
    def __init__(self, player):
        """ Definition for Level 05 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/snow_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1583

        # Array with type of platform, and x, y location of the platform.
        # for level 05
        level05 = [
            [platforms_red_brick.brick_red_wall, -220, 0],
            [platforms_red_brick.brick_basic, -80, 530],
            [platforms_red_brick.brick_red_snow_medium_short_land, -20, 530],
            [platforms_red_brick.brick_red_medium_bottom, 500, 300],
            [platforms_red_brick.brick_red_snow_high_small_left_right, 499, 160],
            [platforms_red_brick.brick_red_snow_medium_short_land, 500, 90],
            [platforms_red_brick.brick_red_snow_medium_short_land, 640, 90],
            [platforms_red_brick.brick_basic, 980, 529],
            [platforms_red_brick.brick_red_snow_medium_short_land, 1050, 530],
            [platforms_red_brick.brick_red_snow_high_small_left_right, 978, 387],
            [platforms_red_brick.brick_red_snow_medium_short_land, 978, 317],
            [platforms_red_brick.brick_red_snow_high_small_left_right, 1188, 177],
            [platforms_red_brick.brick_red_snow_medium_short_land, 1188, 177],
            [platforms_red_brick.brick_red_snow_high_small_left_right, 1677, 177],
            [platforms_red_brick.brick_basic, 1680, 317],
            [platforms_red_brick.brick_red_snow_medium_short_land, 1750, 317],
            [platforms_red_brick.brick_basic, 2030, 317],
            [platforms_red_brick.brick_red_snow_high_small_left_right, 2027, 177],
            [platforms_red_brick.brick_red_snow_high_small_left_right, 2027, 37],
            [platforms_red_brick.brick_red_snow_medium_short_land, 2237, 530],
            [platforms_red_brick.brick_red_big_wall,  2517, 0],
            [platforms_red_brick.brick_red_wall, 2790, 0]
        ]

        water_level05 = [
            [platforms_bad_sprite.medium_short_water, 260, 531],
            [platforms_bad_sprite.medium_long_water, 280, 531],
            [platforms_bad_sprite.medium_long_water, 490, 531],
            [platforms_bad_sprite.medium_long_water, 700, 531],
            [platforms_bad_sprite.medium_short_water, 770, 531],
            [platforms_bad_sprite.medium_short_water, 840, 531],
            [platforms_bad_sprite.medium_long_water, 1330, 531],
            [platforms_bad_sprite.medium_long_water, 1540, 531],
            [platforms_bad_sprite.medium_long_water, 1750, 531],
            [platforms_bad_sprite.medium_long_water, 1960, 531],
            [platforms_bad_sprite.medium_short_water, 2100, 531]
        ]

        portal = [[platforms_item.portal_snow, 2447, 440]]

        love_health = [[platforms_item.restore_health, 1130, 421]]

        # for special enemys
        special_enemy_ta = [[platforms_special_enemy.big_ogre_ta, 700, 190]]
        special_enemy_tu = [[platforms_special_enemy.big_ogre_tu, 1200, 421]]
        special_enemy_te = [[platforms_special_enemy.big_ogre_te, 1680, 70]]
        special_enemy_to = [[platforms_special_enemy.big_ogre_to, 2230, 421]]

        # for point katakana
        katakana_ta = [[platforms_katakana.katakana_ta, 1000, 190]]
        katakana_ti = [[platforms_katakana.katakana_ti, 600, 190]]
        katakana_tu = [[platforms_katakana.katakana_tu, 1538, 200]]
        katakana_te = [[platforms_katakana.katakana_te, 1050, 421]]
        katakana_to = [[platforms_katakana.katakana_to, 1950, 190]]

        for platform in level05:
            block = platforms_red_brick.Platform_grass_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level05:
            water_suicide_lv5 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv5.rect.x = platform[1]
            water_suicide_lv5.rect.y = platform[2]
            water_suicide_lv5.player = self.player
            self.death_place_list_lv5.add(water_suicide_lv5)

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

        # Special enemys
        # katakana Ta
        for platform in special_enemy_ta:
            special_eaten_TA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_TA.rect.x = platform[1]
            special_eaten_TA.rect.y = platform[2]
            special_eaten_TA.player = self.player
            self.special_enemy_list_TA.add(special_eaten_TA)

        # katakana Tu
        for platform in special_enemy_tu:
            special_eaten_TU = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_TU.rect.x = platform[1]
            special_eaten_TU.rect.y = platform[2]
            special_eaten_TU.player = self.player
            self.special_enemy_list_TU.add(special_eaten_TU)

        # katakana Te
        for platform in special_enemy_te:
            special_eaten_TE = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_TE.rect.x = platform[1]
            special_eaten_TE.rect.y = platform[2]
            special_eaten_TE.player = self.player
            self.special_enemy_list_TE.add(special_eaten_TE)

        # katakana To
        for platform in special_enemy_to:
            special_eaten_TO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_TO.rect.x = platform[1]
            special_eaten_TO.rect.y = platform[2]
            special_eaten_TO.player = self.player
            self.special_enemy_list_TO.add(special_eaten_TO)

        # Point
        # katakana Ta
        for platform in katakana_ta:
            true_point_lv5 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.katakana_TA.add(true_point_lv5)

        # katakana Ti
        for platform in katakana_ti:
            true_point_lv5 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.katakana_TI.add(true_point_lv5)

        # katakana Ti
        for platform in katakana_tu:
            true_point_lv5 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.katakana_TU.add(true_point_lv5)

        # katakana Te
        for platform in katakana_te:
            true_point_lv5 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.katakana_TE.add(true_point_lv5)

        # katakana To
        for platform in katakana_to:
            true_point_lv5 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.katakana_TO.add(true_point_lv5)

        # add moving sprites
        block = platforms_red_brick.MovingPlatform_brick_red(
            platforms_red_brick.brick_red_snow_small_half)
        block.rect.x = 350
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_red_brick.MovingPlatform_brick_red(
            platforms_red_brick.brick_red_snow_small_half)
        block.rect.x = 850
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_red_brick.MovingPlatform_brick_red(
            platforms_red_brick.brick_red_snow_small_half)
        block.rect.x = 1538
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_red_brick.MovingPlatform_brick_red(
            platforms_red_brick.brick_red_snow_small_half)
        block.rect.x = 1302
        block.rect.y = 483
        block.boundary_left = 1302
        block.boundary_right = 2167
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # mov_lv5ing enemys
        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv5.rect.x = 500
        eaten_lv5.rect.y = 30
        eaten_lv5.boundary_left = 500
        eaten_lv5.boundary_right = 700
        eaten_lv5.change_x = 5
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv5.rect.x = 600
        eaten_lv5.rect.y = 30
        eaten_lv5.boundary_left = 600
        eaten_lv5.boundary_right = 900
        eaten_lv5.change_x = 4
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv5.rect.x = 750
        eaten_lv5.rect.y = 190
        eaten_lv5.boundary_top = 120
        eaten_lv5.boundary_bottom = 300
        eaten_lv5.change_y = 6
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv5.rect.x = 950
        eaten_lv5.rect.y = 190
        eaten_lv5.boundary_top = 30
        eaten_lv5.boundary_bottom = 300
        eaten_lv5.change_y = 4
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv5.rect.x = 1185
        eaten_lv5.rect.y = 100
        eaten_lv5.boundary_left = 1185
        eaten_lv5.boundary_right = 1400
        eaten_lv5.change_x = 6
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv5.rect.x = 1250
        eaten_lv5.rect.y = 300
        eaten_lv5.boundary_top = 300
        eaten_lv5.boundary_bottom = 500
        eaten_lv5.change_y = 5
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv5.rect.x = 1538
        eaten_lv5.rect.y = 190
        eaten_lv5.boundary_top = 30
        eaten_lv5.boundary_bottom = 300
        eaten_lv5.change_y = 4
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv5.rect.x = 1800
        eaten_lv5.rect.y = 190
        eaten_lv5.boundary_top = 30
        eaten_lv5.boundary_bottom = 300
        eaten_lv5.change_y = 4
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv5.rect.x = 1830
        eaten_lv5.rect.y = 250
        eaten_lv5.boundary_left = 1830
        eaten_lv5.boundary_right = 1900
        eaten_lv5.change_x = 4
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        eaten_lv5 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv5.rect.x = 1850
        eaten_lv5.rect.y = 250
        eaten_lv5.boundary_left = 1850
        eaten_lv5.boundary_right = 1930
        eaten_lv5.change_x = 3
        eaten_lv5.player = self.player
        eaten_lv5.level = self
        self.enemy_list_lv5.add(eaten_lv5)

        special_eaten_TI = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.big_ogre_ti)
        special_eaten_TI.rect.x = 1185
        special_eaten_TI.rect.y = 70
        special_eaten_TI.boundary_left = 1185
        special_eaten_TI.boundary_right = 1400
        special_eaten_TI.change_x = 5
        special_eaten_TI.player = self.player
        special_eaten_TI.level = self
        self.special_enemy_list_TI.add(special_eaten_TI)
