# name file: level_01.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_dirt, platforms_bad_sprite,
    platforms_item, platforms_hiragana,
    platforms_enemy, platforms_special_enemy
)

# import levels module
from hiragana_mode.level_stage_hiragana.levels import Level


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create Level 1 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1166

        # Array with type of platform, and x, y location of the platform.
        # for level 01
        level01 = [
            [platforms_dirt.dirt_wall, -140, 0],
            [platforms_dirt.dirt_medium_long_land, 0, 460],
            [platforms_dirt.dirt_medium_long_land, 700, 460],
            [platforms_dirt.dirt_medium_short_land, 770, 196],
            [platforms_dirt.dirt_short_land, 1330, 460],
            [platforms_dirt.dirt_grass_rounded, 1146, 319],
            [platforms_dirt.dirt_medium_short_land, 1218, 125],
            [platforms_dirt.dirt_medium_long_land, 1680, 460],
            [platforms_dirt.dirt_big_wall, 2100, 0]
        ]

        water_level01 = [
            [platforms_bad_sprite.medium_long_water, 490, 531],
            [platforms_bad_sprite.medium_short_water, 1190, 531],
            [platforms_bad_sprite.medium_long_water, 1470, 531]
        ]

        portal = [[platforms_item.portal_snow, 2030, 380]]

        love_health = [[platforms_item.restore_health, 1380, 400]]

        hiragana_a = [[platforms_hiragana.hiragana_a, 400, 200]]
        hiragana_i = [[platforms_hiragana.hiragana_i, 600, 48]]
        hiragana_u = [[platforms_hiragana.hiragana_u, 200, 200]]

        toxic_frog = [
            [platforms_enemy.fat_frog, 300, 405],
            [platforms_enemy.fat_frog, 400, 405],
            [platforms_enemy.fat_frog, 1680, 405]
        ]

        # for special enemy
        special_enemy_a = [[platforms_special_enemy.big_ogre_a, 700, 360]]
        special_enemy_i = [[platforms_special_enemy.big_ogre_i, 1250, 20]]

        for platform in level01:
            block = platforms_dirt.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level01:
            water_suicide_lv1 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv1.rect.x = platform[1]
            water_suicide_lv1.rect.y = platform[2]
            water_suicide_lv1.player = self.player
            self.death_place_list_lv1.add(water_suicide_lv1)

        for platform in love_health:
            love_restore = platforms_item.Platform_hiragana_katakana(
                platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

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

        # Hiragana I Point
        for platform in hiragana_i:
            true_point_lv1 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv1.rect.x = platform[1]
            true_point_lv1.rect.y = platform[2]
            true_point_lv1.player = self.player
            self.hiragana_I.add(true_point_lv1)

        # False point decrease health player
        # Hiragana U Point
        for platform in hiragana_u:
            false_point_lv1 = platforms_hiragana.Platform_hiragana_katakana(
                platform[0])
            false_point_lv1.rect.x = platform[1]
            false_point_lv1.rect.y = platform[2]
            false_point_lv1.player = self.player
            self.hiragana_U.add(false_point_lv1)

        for platform in toxic_frog:
            eaten_lv1 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv1.rect.x = platform[1]
            eaten_lv1.rect.y = platform[2]
            eaten_lv1.player = self.player
            self.enemy_list_lv1.add(eaten_lv1)

        # for special enemy/immune enemys
        for platform in special_enemy_a:
            special_eaten_A = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_A.rect.x = platform[1]
            special_eaten_A.rect.y = platform[2]
            special_eaten_A.player = self.player
            self.special_enemy_list_A.add(special_eaten_A)

        for platform in special_enemy_i:
            special_eaten_I = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_I.rect.x = platform[1]
            special_eaten_I.rect.y = platform[2]
            special_eaten_I.player = self.player
            self.special_enemy_list_I.add(special_eaten_I)

        # Moving Enemy
        eaten_lv1 = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten_lv1.rect.x = 780
        eaten_lv1.rect.y = 405
        eaten_lv1.boundary_left = 700
        eaten_lv1.boundary_right = 1100
        eaten_lv1.change_x = 3
        eaten_lv1.player = self.player
        eaten_lv1.level = self
        self.enemy_list_lv1.add(eaten_lv1)

        eaten_lv1 = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten_lv1.rect.x = 790
        eaten_lv1.rect.y = 140
        eaten_lv1.boundary_left = 790
        eaten_lv1.boundary_right = 1000
        eaten_lv1.change_x = 6
        eaten_lv1.player = self.player
        eaten_lv1.level = self
        self.enemy_list_lv1.add(eaten_lv1)

        eaten_lv1 = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten_lv1.rect.x = 1300
        eaten_lv1.rect.y = 70
        eaten_lv1.boundary_left = 1300
        eaten_lv1.boundary_right = 1450
        eaten_lv1.change_x = 3
        eaten_lv1.player = self.player
        eaten_lv1.level = self
        self.enemy_list_lv1.add(eaten_lv1)
