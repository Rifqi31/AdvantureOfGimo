# name file: level_03.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_dark_brick, platforms_bad_sprite,
    platforms_item, platforms_enemy,
    platforms_special_enemy, platforms_hiragana
)

# import levels module
from hiragana_mode.level_stage_hiragana.levels import Level


# Create platforms for the level
class Level_03(Level):

    def __init__(self, player):
        """ Definition for Level 03 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/night_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1166

        # Array with type of platform, and x, y location of the platform.
        # for level 03
        level02 = [
            [platforms_dark_brick.brick_dark_wall, -140, 0],
            [platforms_dark_brick.brick_medium_short_land, 0, 529],
            [platforms_dark_brick.brick_medium_large_land, 0, 141],
            [platforms_dark_brick.brick_dark_small_stairs1, 281, 459],
            [platforms_dark_brick.brick_dark_small_stairs2, 351, 389],
            [platforms_dark_brick.brick_dark_small_stairs3, 421, 319],
            [platforms_dark_brick.brick_dark_grass_rounded, 281, 214],
            [platforms_dark_brick.brick_small_short_land, 642, 102],
            [platforms_dark_brick.brick_dark_grass_rounded, 713, 384],
            [platforms_dark_brick.brick_medium_long_land, 840, 528],
            [platforms_dark_brick.brick_medium_large_long_land, 869, 272],
            [platforms_dark_brick.brick_half_short_land, 943, 131],
            [platforms_dark_brick.brick_dark_small_stairs1, 1680, 480],
            [platforms_dark_brick.brick_large_high_land, 1750, 410],
            [platforms_dark_brick.brick_dark_big_wall, 2100, 0]
        ]

        sharp_rock_level03 = [
            [platforms_bad_sprite.medium_sharp_rock, 490, 540],
            [platforms_bad_sprite.small_sharp_rock, 700, 540],
            [platforms_bad_sprite.medium_sharp_rock, 1260, 540],
            [platforms_bad_sprite.medium_sharp_rock, 1470, 540]
        ]

        portal = [[platforms_item.portal_snow, 2030, 335]]

        love_health = [[platforms_item.restore_health, 980, 80]]

        # enemys
        bad_bat = [
            [platforms_enemy.dark_bat, 280, 400],
            [platforms_enemy.dark_bat, 350, 330],
            [platforms_enemy.dark_bat, 420, 260],
            [platforms_enemy.dark_bat, 280, 150],
            [platforms_enemy.dark_bat, 1680, 400]
        ]

        # special enemys
        special_enemy_ka = [[platforms_special_enemy.dark_rabbit_ka, 700, 2]]
        special_enemy_ki = [[platforms_special_enemy.dark_rabbit_ki, 710, 275]]
        special_enemy_ku = [[platforms_special_enemy.dark_rabbit_ku, 130, 30]]
        special_enemy_ke = [
            [platforms_special_enemy.dark_rabbit_ke, 1050, 170]]
        special_enemy_ko = [
            [platforms_special_enemy.dark_rabbit_ko, 1750, 300]]

        # hiragana point
        hiragana_ka = [[platforms_hiragana.hiragana_ka, 30, 30]]
        hiragana_ki = [[platforms_hiragana.hiragana_ki, 500, 180]]
        hiragana_ku = [[platforms_hiragana.hiragana_ku, 280, 50]]
        hiragana_ke = [[platforms_hiragana.hiragana_ke, 800, 150]]
        hiragana_ko = [[platforms_hiragana.hiragana_ko, 1200, 400]]

        for platform in level02:
            block = platforms_dark_brick.Platform_dark_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in sharp_rock_level03:
            sharp_rock_lv3 = platforms_bad_sprite.Platform_dark_brick(platform[0])
            sharp_rock_lv3.rect.x = platform[1]
            sharp_rock_lv3.rect.y = platform[2]
            sharp_rock_lv3.player = self.player
            self.death_place_list_lv3.add(sharp_rock_lv3)

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

        for platform in bad_bat:
            eaten_lv3 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv3.rect.x = platform[1]
            eaten_lv3.rect.y = platform[2]
            eaten_lv3.player = self.player
            self.enemy_list_lv3.add(eaten_lv3)

        # Special enemys
        # Hiragana Ka
        for platform in special_enemy_ka:
            special_eaten_KA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_KA.rect.x = platform[1]
            special_eaten_KA.rect.y = platform[2]
            special_eaten_KA.player = self.player
            self.special_enemy_list_KA.add(special_eaten_KA)

        # Hiragana Ki
        for platform in special_enemy_ki:
            special_eaten_KI = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_KI.rect.x = platform[1]
            special_eaten_KI.rect.y = platform[2]
            special_eaten_KI.player = self.player
            self.special_enemy_list_KI.add(special_eaten_KI)

        # Hiragana Ku
        for platform in special_enemy_ku:
            special_eaten_KU = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_KU.rect.x = platform[1]
            special_eaten_KU.rect.y = platform[2]
            special_eaten_KU.player = self.player
            self.special_enemy_list_KU.add(special_eaten_KU)

        # Hiragana Ke
        for platform in special_enemy_ke:
            special_eaten_KE = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_KE.rect.x = platform[1]
            special_eaten_KE.rect.y = platform[2]
            special_eaten_KE.player = self.player
            self.special_enemy_list_KE.add(special_eaten_KE)

        # Hiragana Ko
        for platform in special_enemy_ko:
            special_eaten_KO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_KO.rect.x = platform[1]
            special_eaten_KO.rect.y = platform[2]
            special_eaten_KO.player = self.player
            self.special_enemy_list_KO.add(special_eaten_KO)

        # Point
        # Hiragana Ka
        for platform in hiragana_ka:
            true_point_lv3 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KA_lv3.add(true_point_lv3)

        # Hiragana Ki
        for platform in hiragana_ki:
            true_point_lv3 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KI_lv3.add(true_point_lv3)

        # Hiragana Ku
        for platform in hiragana_ku:
            true_point_lv3 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KU.add(true_point_lv3)

        # Hiragana Ke
        for platform in hiragana_ke:
            true_point_lv3 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KE.add(true_point_lv3)

        # Hiragana Ko
        for platform in hiragana_ko:
            true_point_lv3 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KO.add(true_point_lv3)

        # add moving sprites
        block = platforms_dark_brick.MovingPlatform_dark_brick(
            platforms_dark_brick.brick_half_small_land)
        block.rect.x = 1302
        block.rect.y = 483
        block.boundary_left = 1302
        block.boundary_right = 1600
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemys
        eaten_lv3 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv3.rect.x = 900
        eaten_lv3.rect.y = 200
        eaten_lv3.boundary_left = 900
        eaten_lv3.boundary_right = 1000
        eaten_lv3.change_x = 4
        eaten_lv3.player = self.player
        eaten_lv3.level = self
        self.enemy_list_lv3.add(eaten_lv3)

        eaten_lv3 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv3.rect.x = 800
        eaten_lv3.rect.y = 450
        eaten_lv3.boundary_left = 800
        eaten_lv3.boundary_right = 1000
        eaten_lv3.change_x = 4
        eaten_lv3.player = self.player
        eaten_lv3.level = self
        self.enemy_list_lv3.add(eaten_lv3)
