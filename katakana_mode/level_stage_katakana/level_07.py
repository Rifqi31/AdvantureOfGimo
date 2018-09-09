# name file: level_07.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_sand_dirt, platforms_bad_sprite,
    platforms_katakana, platforms_enemy,
    platforms_special_enemy, platforms_item
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_07(Level):
    def __init__(self, player):
        """ Definition for Level 07 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1586

        # Array with type of platform, and x, y location of the platform.
        # for level 07
        level07 = [
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

        water_level07 = [
            [platforms_bad_sprite.medium_long_water, 350, 531],
            [platforms_bad_sprite.medium_long_water, 770, 531],
            [platforms_bad_sprite.medium_long_water, 980, 531],
            [platforms_bad_sprite.medium_long_water, 1820, 531],
            [platforms_bad_sprite.medium_long_water, 2030, 531]
        ]

        portal = [[platforms_item.portal_snow, 2450, 389]]

        # katakana point
        katakana_ha = [[platforms_katakana.katakana_ha, 420, 210]]
        katakana_hi = [[platforms_katakana.katakana_hi, 820, 10]]
        katakana_hu = [[platforms_katakana.katakana_hu, 180, 130]]
        katakana_he = [[platforms_katakana.katakana_he, 0, 20]]
        katakana_ho = [[platforms_katakana.katakana_ho, 1520, 380]]

        # Enemys
        skull_zombie = [[platforms_enemy.old_skull, 570, 340],
                        [platforms_enemy.old_skull, 650, 270],
                        [platforms_enemy.old_skull, 710, 199]]

        # Special Enemys
        special_enemy_ha = [[platforms_special_enemy.orange_slime_ha, 555, 20]]
        special_enemy_hi = [[platforms_special_enemy.orange_slime_hi, 280, 20]]
        special_enemy_hu = [[platforms_special_enemy.orange_slime_hu, 60, 20]]
        special_enemy_he = [
            [platforms_special_enemy.orange_slime_he, 1200, 290]]
        special_enemy_ho = [
            [platforms_special_enemy.orange_slime_ho, 1680, 290]]

        for platform in level07:
            block = platforms_sand_dirt.Platform_dirt_sand(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level07:
            water_suicide_lv7 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv7.rect.x = platform[1]
            water_suicide_lv7.rect.y = platform[2]
            water_suicide_lv7.player = self.player
            self.death_place_list_lv7.add(water_suicide_lv7)

        for platform in portal:
            gate = platforms_item.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # Enemys
        for platform in skull_zombie:
            eaten_lv7 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv7.rect.x = platform[1]
            eaten_lv7.rect.y = platform[2]
            eaten_lv7.player = self.player
            self.enemy_list_lv7.add(eaten_lv7)

        # Special enemys
        # katakana Ha
        for platform in special_enemy_ha:
            special_eaten_HA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_HA.rect.x = platform[1]
            special_eaten_HA.rect.y = platform[2]
            special_eaten_HA.player = self.player
            self.special_enemy_list_HA.add(special_eaten_HA)

        # katakana Hi
        for platform in special_enemy_hi:
            special_eaten_HI = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_HI.rect.x = platform[1]
            special_eaten_HI.rect.y = platform[2]
            special_eaten_HI.player = self.player
            self.special_enemy_list_HI.add(special_eaten_HI)

        # katakana Hu
        for platform in special_enemy_hu:
            special_eaten_HU = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_HU.rect.x = platform[1]
            special_eaten_HU.rect.y = platform[2]
            special_eaten_HU.player = self.player
            self.special_enemy_list_HU.add(special_eaten_HU)

        # katakana He
        for platform in special_enemy_he:
            special_eaten_HE = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_HE.rect.x = platform[1]
            special_eaten_HE.rect.y = platform[2]
            special_eaten_HE.player = self.player
            self.special_enemy_list_HE.add(special_eaten_HE)

        # katakana Ho
        for platform in special_enemy_ho:
            special_eaten_HO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_HO.rect.x = platform[1]
            special_eaten_HO.rect.y = platform[2]
            special_eaten_HO.player = self.player
            self.special_enemy_list_HO.add(special_eaten_HO)

        # Point
        # katakana Ha
        for platform in katakana_ha:
            true_point_lv7 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.katakana_HA.add(true_point_lv7)

        # katakana Hi
        for platform in katakana_hi:
            true_point_lv7 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.katakana_HI.add(true_point_lv7)

        # katakana Hu
        for platform in katakana_hu:
            true_point_lv7 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.katakana_HU.add(true_point_lv7)

        # katakana He
        for platform in katakana_he:
            true_point_lv7 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.katakana_HE.add(true_point_lv7)

        # katakana Ho
        for platform in katakana_ho:
            true_point_lv7 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.katakana_HO.add(true_point_lv7)

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
        eaten_lv7 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv7.rect.x = 820
        eaten_lv7.rect.y = 120
        eaten_lv7.boundary_top = 70
        eaten_lv7.boundary_bottom = 500
        eaten_lv7.change_y = 4
        eaten_lv7.player = self.player
        eaten_lv7.level = self
        self.enemy_list_lv7.add(eaten_lv7)

        eaten_lv7 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv7.rect.x = 1380
        eaten_lv7.rect.y = 400
        eaten_lv7.boundary_left = 1380
        eaten_lv7.boundary_right = 1700
        eaten_lv7.change_x = 6
        eaten_lv7.player = self.player
        eaten_lv7.level = self
        self.enemy_list_lv7.add(eaten_lv7)

        eaten_lv7 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv7.rect.x = 1380
        eaten_lv7.rect.y = 400
        eaten_lv7.boundary_left = 1380
        eaten_lv7.boundary_right = 1700
        eaten_lv7.change_x = 5
        eaten_lv7.player = self.player
        eaten_lv7.level = self
        self.enemy_list_lv7.add(eaten_lv7)

        eaten_lv7 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv7.rect.x = 1380
        eaten_lv7.rect.y = 400
        eaten_lv7.boundary_left = 1380
        eaten_lv7.boundary_right = 1700
        eaten_lv7.change_x = 4
        eaten_lv7.player = self.player
        eaten_lv7.level = self
        self.enemy_list_lv7.add(eaten_lv7)
