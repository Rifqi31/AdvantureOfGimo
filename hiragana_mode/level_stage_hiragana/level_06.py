# name file: level_06.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_snow, platforms_bad_sprite,
    platforms_item, platforms_hiragana,
    platforms_enemy, platforms_special_enemy,
)

from hiragana_mode.level_stage_hiragana.levels import Level


# Create platforms for the level
class Level_06(Level):
    def __init__(self, player):
        """ Definition for Level 06 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/snow_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1146

        # Array with type of platform, and x, y location of the platform.
        # for level 06
        level06 = [
            [platforms_snow.snow_dirt_wall, -140, 0],
            [platforms_snow.snow_dirt_grass_medium_large, 0, 530],
            [platforms_snow.snow_dirt_grass_short_tall, 490, 390],
            [platforms_snow.snow_dirt_grass_medium_tall, 560, 320],
            [platforms_snow.snow_dirt_grass_rounded, 320, 190],
            [platforms_snow.snow_dirt_tall_grass_left_right, 740, 0],
            [platforms_snow.snow_dirt_grass_small_large, 0, 120],
            [platforms_snow.snow_dirt_tall_grass_left_right, 1240, 260],
            [platforms_snow.snow_dirt_grass_up_down, 1310, 260],
            [platforms_snow.snow_dirt_grass_medium_large, 1380, 460],
            [platforms_snow.snow_dirt_grass_medium_large, 1870, 460],
            [platforms_snow.snow_dirt_big_wall, 2080, 0]
        ]

        water_level06 = [
            [platforms_bad_sprite.medium_long_water, 280, 531],
            [platforms_bad_sprite.medium_long_water, 630, 531],
            [platforms_bad_sprite.medium_long_water, 840, 531],
            [platforms_bad_sprite.medium_long_water, 1030, 531],
            [platforms_bad_sprite.medium_short_water, 1310, 531],
            [platforms_bad_sprite.medium_long_water, 1660, 531]
        ]

        portal = [[platforms_item.portal_snow, 2010, 390]]

        love_health = [[platforms_item.restore_health, 0, 40],
                       [platforms_item.restore_health, 1450, 350]]

        # hiragana point
        hiragana_na = [[platforms_hiragana.hiragana_na, 560, 100]]
        hiragana_ni = [[platforms_hiragana.hiragana_ni, 200, 175]]
        hiragana_nu = [[platforms_hiragana.hiragana_nu, 640, 0]]
        hiragana_ne = [[platforms_hiragana.hiragana_ne, 830, 35]]
        hiragana_no = [[platforms_hiragana.hiragana_no, 1380, 350]]

        # enemys
        ghost = [[platforms_enemy.skull_ghost, 490, 330],
                 [platforms_enemy.skull_ghost, 580, 260]]

        # special enemys
        special_enemy_na = [[platforms_special_enemy.dark_rabbit_na, 320, 80]]
        special_enemy_ni = [[platforms_special_enemy.dark_rabbit_ni, 50, 15]]
        special_enemy_no = [
            [platforms_special_enemy.dark_rabbit_no, 1870, 350]]

        for platform in level06:
            block = platforms_snow.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level06:
            water_suicide_lv6 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv6.rect.x = platform[1]
            water_suicide_lv6.rect.y = platform[2]
            water_suicide_lv6.player = self.player
            self.death_place_list_lv6.add(water_suicide_lv6)

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

        # Enemys
        for platform in ghost:
            eaten_lv6 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv6.rect.x = platform[1]
            eaten_lv6.rect.y = platform[2]
            eaten_lv6.player = self.player
            self.enemy_list_lv6.add(eaten_lv6)

        # Special enemys
        # Hiragana Na
        for platform in special_enemy_na:
            special_eaten_NA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_NA.rect.x = platform[1]
            special_eaten_NA.rect.y = platform[2]
            special_eaten_NA.player = self.player
            self.special_enemy_list_NA.add(special_eaten_NA)

        # Hiragana Ni
        for platform in special_enemy_ni:
            special_eaten_NI = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_NI.rect.x = platform[1]
            special_eaten_NI.rect.y = platform[2]
            special_eaten_NI.player = self.player
            self.special_enemy_list_NI.add(special_eaten_NI)

        # Hiragana No
        for platform in special_enemy_no:
            special_eaten_NO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_NO.rect.x = platform[1]
            special_eaten_NO.rect.y = platform[2]
            special_eaten_NO.player = self.player
            self.special_enemy_list_NO.add(special_eaten_NO)

        # Point
        # Hiragana Na
        for platform in hiragana_na:
            true_point_lv6 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NA.add(true_point_lv6)

        # Hiragana Ni
        for platform in hiragana_ni:
            true_point_lv6 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NI.add(true_point_lv6)

        # Hiragana Nu
        for platform in hiragana_nu:
            true_point_lv6 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NU.add(true_point_lv6)

        # Hiragana Ne
        for platform in hiragana_ne:
            true_point_lv6 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NE.add(true_point_lv6)

        # Hiragana No
        for platform in hiragana_no:
            true_point_lv6 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NO.add(true_point_lv6)

        # add moving sprites
        block = platforms_snow.MovingPlatform_snow(
            platforms_snow.snow_dirt_half)
        block.rect.x = 690
        block.rect.y = 483
        block.boundary_left = 690
        block.boundary_right = 1100
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms_snow.MovingPlatform_snow(
            platforms_snow.snow_dirt_half)
        block.rect.x = 820
        block.rect.y = 343
        block.boundary_left = 820
        block.boundary_right = 1100
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten_lv6 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv6.rect.x = 690
        eaten_lv6.rect.y = 430
        eaten_lv6.boundary_left = 690
        eaten_lv6.boundary_right = 1100
        eaten_lv6.change_x = 2
        eaten_lv6.player = self.player
        eaten_lv6.level = self
        self.enemy_list_lv6.add(eaten_lv6)

        eaten_lv6 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv6.rect.x = 690
        eaten_lv6.rect.y = 380
        eaten_lv6.boundary_left = 690
        eaten_lv6.boundary_right = 1100
        eaten_lv6.change_x = 4
        eaten_lv6.player = self.player
        eaten_lv6.level = self
        self.enemy_list_lv6.add(eaten_lv6)

        eaten_lv6 = platforms_enemy.MovingEnemy(platforms_enemy.skull_ghost)
        eaten_lv6.rect.x = 1350
        eaten_lv6.rect.y = 200
        eaten_lv6.boundary_left = 1350
        eaten_lv6.boundary_right = 1450
        eaten_lv6.change_x = 4
        eaten_lv6.player = self.player
        eaten_lv6.level = self
        self.enemy_list_lv6.add(eaten_lv6)

        # add moving special enemys
        special_eaten_NU = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.dark_rabbit_nu)
        special_eaten_NU.rect.x = 820
        special_eaten_NU.rect.y = 235
        special_eaten_NU.boundary_left = 820
        special_eaten_NU.boundary_right = 1100
        special_eaten_NU.change_x = 4
        special_eaten_NU.player = self.player
        special_eaten_NU.level = self
        self.special_enemy_list_NU.add(special_eaten_NU)

        special_eaten_NE = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.dark_rabbit_ne)
        special_eaten_NE.rect.x = 1310
        special_eaten_NE.rect.y = 150
        special_eaten_NE.boundary_left = 1310
        special_eaten_NE.boundary_right = 1450
        special_eaten_NE.change_x = 4
        special_eaten_NE.player = self.player
        special_eaten_NE.level = self
        self.special_enemy_list_NE.add(special_eaten_NE)
