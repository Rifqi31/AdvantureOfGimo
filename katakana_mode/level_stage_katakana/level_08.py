# name file: level_08.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_sand_dirt, platforms_bad_sprite,
    platforms_item, platforms_katakana,
    platforms_enemy, platforms_special_enemy
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_08(Level):
    def __init__(self, player):
        """ Definition for Level 08 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1586

        # Array with type of platform, and x, y location of the platform.
        # for level 08
        level08 = [
            [platforms_sand_dirt.sand_dirt_wall, -140, 0],
            [platforms_sand_dirt.sand_dirt_medium_long_land, 0, 530],
            [platforms_sand_dirt.sand_dirt_tall_small, 560, 390],
            [platforms_sand_dirt.sand_dirt_tall_medium, 630, 320],
            [platforms_sand_dirt.sand_dirt_tall_long, 700, 250],
            [platforms_sand_dirt.sand_dirt_half, 560, 120],
            [platforms_sand_dirt.sand_dirt_wall, 920, -250],
            [platforms_sand_dirt.sand_dirt_basic_medium, 280, 120],
            [platforms_sand_dirt.sand_dirt_basic_medium, 0, 120],
            [platforms_sand_dirt.sand_dirt_tall_large_medium, 1190, 390],
            [platforms_sand_dirt.sand_dirt_medium_long_land, 1330, 460],
            [platforms_sand_dirt.sand_dirt_tall_large_medium, 1680, 390],
            [platforms_sand_dirt.sand_dirt_long_soft_up_down, 1200, 190],
            [platforms_sand_dirt.sand_dirt_medium_long_land, 2240, 460],
            [platforms_sand_dirt.sand_dirt_big_wall, 2660, 0],
            [platforms_sand_dirt.sand_dirt_wall, 2520, 0]
        ]

        water_level08 = [
            [platforms_bad_sprite.medium_long_water, 350, 531],
            [platforms_bad_sprite.medium_long_water, 770, 531],
            [platforms_bad_sprite.medium_long_water, 980, 531],
            [platforms_bad_sprite.medium_long_water, 1820, 531],
            [platforms_bad_sprite.medium_long_water, 2030, 531]
        ]

        portal = [[platforms_item.portal_snow, 2450, 389]]

        # katakana point
        katakana_ma = [[platforms_katakana.katakana_ma, 420, 210]]
        katakana_mi = [[platforms_katakana.katakana_mi, 820, 10]]
        katakana_mu = [[platforms_katakana.katakana_mu, 180, 130]]
        katakana_me = [[platforms_katakana.katakana_me, 0, 20]]
        katakana_mo = [[platforms_katakana.katakana_mo, 1520, 380]]

        # Enemys
        skull_zombie = [[platforms_enemy.old_skull, 570, 340],
                        [platforms_enemy.old_skull, 650, 270],
                        [platforms_enemy.old_skull, 710, 199]]

        # Special Enemys
        special_enemy_ma = [[platforms_special_enemy.zombie_skull_ma, 555, 20]]
        special_enemy_mi = [[platforms_special_enemy.zombie_skull_mi, 280, 20]]
        special_enemy_mu = [[platforms_special_enemy.zombie_skull_mu, 60, 20]]
        special_enemy_me = [
            [platforms_special_enemy.zombie_skull_me, 1200, 290]]
        special_enemy_mo = [
            [platforms_special_enemy.zombie_skull_mo, 1680, 290]]

        for platform in level08:
            block = platforms_sand_dirt.Platform_dirt_sand(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level08:
            water_suicide_lv8 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv8.rect.x = platform[1]
            water_suicide_lv8.rect.y = platform[2]
            water_suicide_lv8.player = self.player
            self.death_place_list_lv8.add(water_suicide_lv8)

        for platform in portal:
            gate = platforms_item.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # Enemys
        for platform in skull_zombie:
            eaten_lv8 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv8.rect.x = platform[1]
            eaten_lv8.rect.y = platform[2]
            eaten_lv8.player = self.player
            self.enemy_list_lv8.add(eaten_lv8)

        # Special enemys
        # katakana Ma
        for platform in special_enemy_ma:
            special_eaten_MA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_MA.rect.x = platform[1]
            special_eaten_MA.rect.y = platform[2]
            special_eaten_MA.player = self.player
            self.special_enemy_list_MA.add(special_eaten_MA)

        # katakana Mi
        for platform in special_enemy_mi:
            special_eaten_MI = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_MI.rect.x = platform[1]
            special_eaten_MI.rect.y = platform[2]
            special_eaten_MI.player = self.player
            self.special_enemy_list_MI.add(special_eaten_MI)

        # katakana Mu
        for platform in special_enemy_mu:
            special_eaten_MU = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_MU.rect.x = platform[1]
            special_eaten_MU.rect.y = platform[2]
            special_eaten_MU.player = self.player
            self.special_enemy_list_MU.add(special_eaten_MU)

        # katakana Me
        for platform in special_enemy_me:
            special_eaten_ME = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_ME.rect.x = platform[1]
            special_eaten_ME.rect.y = platform[2]
            special_eaten_ME.player = self.player
            self.special_enemy_list_ME.add(special_eaten_ME)

        # katakana Mo
        for platform in special_enemy_mo:
            special_eaten_MO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_MO.rect.x = platform[1]
            special_eaten_MO.rect.y = platform[2]
            special_eaten_MO.player = self.player
            self.special_enemy_list_MO.add(special_eaten_MO)

        # Point
        # katakana Ma
        for platform in katakana_ma:
            true_point_lv8 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.katakana_MA.add(true_point_lv8)

        # katakana Mi
        for platform in katakana_mi:
            true_point_lv8 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.katakana_MI.add(true_point_lv8)

        # katakana Mu
        for platform in katakana_mu:
            true_point_lv8 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.katakana_MU.add(true_point_lv8)

        # katakana Me
        for platform in katakana_me:
            true_point_lv8 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.katakana_ME.add(true_point_lv8)

        # katakana Mo
        for platform in katakana_mo:
            true_point_lv8 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.katakana_MO.add(true_point_lv8)

        # Moving Platforms
        block = platforms_sand_dirt.MovingPlatform_dirt_sand(
            platforms_sand_dirt.sand_dirt_half)
        block.rect.x = 820
        block.rect.y = 483
        block.boundary_top = 70
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms_sand_dirt.MovingPlatform_dirt_sand(
            platforms_sand_dirt.sand_dirt_half)
        block.rect.x = 820
        block.rect.y = 483
        block.boundary_left = 820
        block.boundary_right = 1100
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemys
        eaten_lv8 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv8.rect.x = 820
        eaten_lv8.rect.y = 120
        eaten_lv8.boundary_top = 70
        eaten_lv8.boundary_bottom = 500
        eaten_lv8.change_y = 4
        eaten_lv8.player = self.player
        eaten_lv8.level = self
        self.enemy_list_lv8.add(eaten_lv8)

        eaten_lv8 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv8.rect.x = 1380
        eaten_lv8.rect.y = 400
        eaten_lv8.boundary_left = 1380
        eaten_lv8.boundary_right = 1700
        eaten_lv8.change_x = 6
        eaten_lv8.player = self.player
        eaten_lv8.level = self
        self.enemy_list_lv8.add(eaten_lv8)

        eaten_lv8 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv8.rect.x = 1380
        eaten_lv8.rect.y = 400
        eaten_lv8.boundary_left = 1380
        eaten_lv8.boundary_right = 1700
        eaten_lv8.change_x = 5
        eaten_lv8.player = self.player
        eaten_lv8.level = self
        self.enemy_list_lv8.add(eaten_lv8)

        eaten_lv8 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv8.rect.x = 1380
        eaten_lv8.rect.y = 400
        eaten_lv8.boundary_left = 1380
        eaten_lv8.boundary_right = 1700
        eaten_lv8.change_x = 4
        eaten_lv8.player = self.player
        eaten_lv8.level = self
        self.enemy_list_lv8.add(eaten_lv8)
