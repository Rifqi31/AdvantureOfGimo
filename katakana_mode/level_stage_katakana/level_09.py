# name file: level_08.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_ancient_brick, platforms_bad_sprite,
    platforms_item, platforms_katakana,
    platforms_enemy, platforms_special_enemy
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_09(Level):
    def __init__(self, player):
        """ Definition for Level 09 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1686

        # Array with type of platform, and x, y location of the platform.
        # for level 09
        level09 = [
            [platforms_ancient_brick.ancient_brick_wall, -140, 0],
            [platforms_ancient_brick.ancient_brick_tall_large_long, 0, 530],
            [platforms_ancient_brick.ancient_brick_tall_large_long, 0, 74],
            [platforms_ancient_brick.ancient_brick_tall_sand_left_right, 420, 180],
            [platforms_ancient_brick.ancient_brick_basic, 420, 130],
            [platforms_ancient_brick.ancient_brick_medium_sand_top_down, 490, 130],
            [platforms_ancient_brick.ancient_brick_medium_sand_top_down, 490, 340],
            [platforms_ancient_brick.ancient_brick_tall_large_small, 910, 410],
            [platforms_ancient_brick.ancient_brick_tall_large_medium, 980, 480],
            [platforms_ancient_brick.ancient_brick_short_land, 1570, 100],
            [platforms_ancient_brick.ancient_brick_tall_large_long, 2200, 530],
            [platforms_ancient_brick.ancient_brick_tall_large_long, 2410, 530],
            [platforms_ancient_brick.ancient_brick_big_wall, 2620, 0],
            [platforms_ancient_brick.ancient_brick_wall, 2900, 0]
        ]

        water_level09 = [
            [platforms_bad_sprite.medium_long_water, 210, 531],
            [platforms_bad_sprite.medium_long_water, 490, 531],
            [platforms_bad_sprite.medium_long_water, 700, 531],
            [platforms_bad_sprite.medium_long_water, 1120, 531],
            [platforms_bad_sprite.medium_long_water, 1330, 531],
            [platforms_bad_sprite.medium_long_water, 1540, 531],
            [platforms_bad_sprite.medium_short_water, 1660, 531],
            [platforms_bad_sprite.medium_long_water, 1730, 531],
            [platforms_bad_sprite.medium_long_water, 1940, 531],
            [platforms_bad_sprite.medium_short_water, 2060, 531]
        ]

        portal = [[platforms_item.portal_snow, 2550, 459]]

        love_health = [[platforms_item.restore_health, 600, 250]]

        # katakana
        katakana_ya = [[platforms_katakana.katakana_ya, 20, 10]]
        katakana_yu = [[platforms_katakana.katakana_yu, 500, 250]]
        katakana_yo = [[platforms_katakana.katakana_yo, 1150, 20]]

        # Special enemy
        special_enemy_ya = [[platforms_special_enemy.zombie_skull_ya, 420, 35]]

        for platform in level09:
            block = platforms_ancient_brick.Platform_ancient_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level09:
            water_suicide_lv9 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv9.rect.x = platform[1]
            water_suicide_lv9.rect.y = platform[2]
            water_suicide_lv9.player = self.player
            self.death_place_list_lv9.add(water_suicide_lv9)

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
        # katakana Ya
        for platform in special_enemy_ya:
            special_eaten_YA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_YA.rect.x = platform[1]
            special_eaten_YA.rect.y = platform[2]
            special_eaten_YA.player = self.player
            self.special_enemy_list_YA.add(special_eaten_YA)

        # Point
        # katakana Ya
        for platform in katakana_ya:
            true_point_lv9 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv9.rect.x = platform[1]
            true_point_lv9.rect.y = platform[2]
            true_point_lv9.player = self.player
            self.katakana_YA.add(true_point_lv9)

        # katakana Yu
        for platform in katakana_yu:
            true_point_lv9 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv9.rect.x = platform[1]
            true_point_lv9.rect.y = platform[2]
            true_point_lv9.player = self.player
            self.katakana_YU.add(true_point_lv9)

        # katakana Yo
        for platform in katakana_yo:
            true_point_lv9 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv9.rect.x = platform[1]
            true_point_lv9.rect.y = platform[2]
            true_point_lv9.player = self.player
            self.katakana_YO.add(true_point_lv9)

        # add moving sprites
        block = platforms_ancient_brick.MovingPlatform_ancient_brick(
            platforms_ancient_brick.ancient_brick_half)
        block.rect.x = 280
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_ancient_brick.MovingPlatform_ancient_brick(
            platforms_ancient_brick.ancient_brick_half)
        block.rect.x = 700
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_ancient_brick.MovingPlatform_ancient_brick(
            platforms_ancient_brick.ancient_brick_half)
        block.rect.x = 1120
        block.rect.y = 343
        block.boundary_left = 1120
        block.boundary_right = 1500
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_ancient_brick.MovingPlatform_ancient_brick(
            platforms_ancient_brick.ancient_brick_half)
        block.rect.x = 1120
        block.rect.y = 203
        block.boundary_left = 1120
        block.boundary_right = 1500
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten_lv9 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv9.rect.x = 70
        eaten_lv9.rect.y = 25
        eaten_lv9.boundary_left = 70
        eaten_lv9.boundary_right = 180
        eaten_lv9.change_x = 3
        eaten_lv9.player = self.player
        eaten_lv9.level = self
        self.enemy_list_lv9.add(eaten_lv9)

        eaten_lv9 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv9.rect.x = 280
        eaten_lv9.rect.y = 100
        eaten_lv9.boundary_top = 100
        eaten_lv9.boundary_bottom = 450
        eaten_lv9.change_y = 4
        eaten_lv9.player = self.player
        eaten_lv9.level = self
        self.enemy_list_lv9.add(eaten_lv9)

        eaten_lv9 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv9.rect.x = 700
        eaten_lv9.rect.y = 100
        eaten_lv9.boundary_top = 100
        eaten_lv9.boundary_bottom = 450
        eaten_lv9.change_y = 2
        eaten_lv9.player = self.player
        eaten_lv9.level = self
        self.enemy_list_lv9.add(eaten_lv9)

        # add moving special enemy
        # katakana Yu
        special_eaten_YU = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.zombie_skull_yu)
        special_eaten_YU.rect.x = 1120
        special_eaten_YU.rect.y = 110
        special_eaten_YU.boundary_left = 1120
        special_eaten_YU.boundary_right = 1500
        special_eaten_YU.change_x = 3
        special_eaten_YU.player = self.player
        special_eaten_YU.level = self
        self.special_enemy_list_YU.add(special_eaten_YU)

        # katakana Yo
        special_eaten_YO = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.zombie_skull_yo)
        special_eaten_YO.rect.x = 1570
        special_eaten_YO.rect.y = 10
        special_eaten_YO.boundary_left = 1570
        special_eaten_YO.boundary_right = 1670
        special_eaten_YO.change_x = 3
        special_eaten_YO.player = self.player
        special_eaten_YO.level = self
        self.special_enemy_list_YO.add(special_eaten_YO)
