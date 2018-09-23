# name file: level_04.py
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
class Level_04(Level):
    def __init__(self, player):
        """ Definition for Level 04 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1095

        # Array with type of platform, and x, y location of the platform.
        # for level 04
        level04 = [
            [platforms_red_brick.brick_red_wall, -140, 0],
            [platforms_red_brick.brick_red_medium_long_land, 0, 529],
            [platforms_red_brick.brick_red_medium_long_land, 210, 529],
            [platforms_red_brick.brick_red_grass_rounded, 300, 150],
            [platforms_red_brick.brick_red_medium_short_land, 0, 150],
            [platforms_red_brick.brick_red_grass_left_right_long, 700, 180],
            [platforms_red_brick.brick_red_medium_long_land, 979, 80],
            [platforms_red_brick.brick_red_medium_long_land, 979, 280],
            [platforms_red_brick.brick_red_medium_high_land, 979, 470],
            [platforms_red_brick.brick_red_medium_short_land, 1049, 529],
            [platforms_red_brick.brick_red_medium_high_land, 1189, 470],
            [platforms_red_brick.brick_red_grass_left_right_long, 1400, 250],
            [platforms_red_brick.brick_red_grass_left_right_long, 1400, -300],
            [platforms_red_brick.brick_red_medium_high_large_land, 1609, 470],
            [platforms_red_brick.brick_red_medium_short_land, 1819, 540],
            [platforms_red_brick.brick_red_medium_short_land, 1959, 540],
            [platforms_red_brick.brick_red_big_wall, 2029, 0]
        ]

        water_level04 = [
            [platforms_bad_sprite.medium_long_water, 490, 532],
            [platforms_bad_sprite.medium_long_water, 770, 532],
            [platforms_bad_sprite.medium_long_water, 1260, 532],
            [platforms_bad_sprite.medium_short_water, 1470, 532]
        ]

        portal = [[platforms_item.portal_snow, 1930, 440]]

        love_health = [
            [platforms_item.restore_health, 80, 50],
            [platforms_item.restore_health, 1100, 480],
            [platforms_item.restore_health, 1300, 340]
        ]

        # special enemys
        special_enemy_sa = [[platforms_special_enemy.orange_slime_sa, 695, 80]]
        special_enemy_si = [[platforms_special_enemy.orange_slime_si, 295, 50]]
        special_enemy_su = [
            [platforms_special_enemy.orange_slime_su, 1180, 183]]
        special_enemy_se = [
            [platforms_special_enemy.orange_slime_se, 1395, 150]]
        special_enemy_so = [
            [platforms_special_enemy.orange_slime_so, 1609, 370]]

        # katakana Point
        katakana_sa = [[platforms_katakana.katakana_sa, 150, 50]]
        katakana_si = [[platforms_katakana.katakana_si, 560, 100]]
        katakana_su = [[platforms_katakana.katakana_su, 1189, 370]]
        katakana_se = [[platforms_katakana.katakana_se, 1189, 10]]
        katakana_so = [[platforms_katakana.katakana_so, 1500, 340]]

        for platform in level04:
            block = platforms_red_brick.Platform_grass_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level04:
            water_suicide_lv4 = platforms_bad_sprite.Platform_dirt(platform[0])
            water_suicide_lv4.rect.x = platform[1]
            water_suicide_lv4.rect.y = platform[2]
            water_suicide_lv4.player = self.player
            self.death_place_list_lv4.add(water_suicide_lv4)

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
        # katakana Sa
        for platform in special_enemy_sa:
            special_eaten_SA = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_SA.rect.x = platform[1]
            special_eaten_SA.rect.y = platform[2]
            special_eaten_SA.player = self.player
            self.special_enemy_list_SA.add(special_eaten_SA)

        # katakana Si
        for platform in special_enemy_si:
            special_eaten_SI = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_SI.rect.x = platform[1]
            special_eaten_SI.rect.y = platform[2]
            special_eaten_SI.player = self.player
            self.special_enemy_list_SI.add(special_eaten_SI)

        # katakana Su
        for platform in special_enemy_su:
            special_eaten_SU = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_SU.rect.x = platform[1]
            special_eaten_SU.rect.y = platform[2]
            special_eaten_SU.player = self.player
            self.special_enemy_list_SU.add(special_eaten_SU)

        # katakana Se
        for platform in special_enemy_se:
            special_eaten_SE = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_SE.rect.x = platform[1]
            special_eaten_SE.rect.y = platform[2]
            special_eaten_SE.player = self.player
            self.special_enemy_list_SE.add(special_eaten_SE)

        # katakana So
        for platform in special_enemy_so:
            special_eaten_SO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_SO.rect.x = platform[1]
            special_eaten_SO.rect.y = platform[2]
            special_eaten_SO.player = self.player
            self.special_enemy_list_SO.add(special_eaten_SO)

        # Point
        # katakana Sa
        for platform in katakana_sa:
            true_point_lv4 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.katakana_SA.add(true_point_lv4)

        # katakana Si
        for platform in katakana_si:
            true_point_lv4 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.katakana_SI.add(true_point_lv4)

        # katakana Si
        for platform in katakana_su:
            true_point_lv4 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.katakana_SU.add(true_point_lv4)

        # katakana Se
        for platform in katakana_se:
            true_point_lv4 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.katakana_SE.add(true_point_lv4)

        # katakana So
        for platform in katakana_so:
            true_point_lv4 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.katakana_SO.add(true_point_lv4)

        # add moving sprites
        block = platforms_red_brick.MovingPlatform_brick_red(
            platforms_red_brick.brick_red_small_half)
        block.rect.x = 560
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms_red_brick.MovingPlatform_brick_red(
            platforms_red_brick.brick_red_small_half)
        block.rect.x = 800
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Enemys
        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv4.rect.x = 0
        eaten_lv4.rect.y = 80
        eaten_lv4.boundary_left = 0
        eaten_lv4.boundary_right = 100
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv4.rect.x = 300
        eaten_lv4.rect.y = 470
        eaten_lv4.boundary_left = 300
        eaten_lv4.boundary_right = 400
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv4.rect.x = 350
        eaten_lv4.rect.y = 470
        eaten_lv4.boundary_left = 350
        eaten_lv4.boundary_right = 450
        eaten_lv4.change_x = 4
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv4.rect.x = 1000
        eaten_lv4.rect.y = 230
        eaten_lv4.boundary_left = 1000
        eaten_lv4.boundary_right = 1150
        eaten_lv4.change_x = 4
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 560
        eaten_lv4.rect.y = 200
        eaten_lv4.boundary_top = 100
        eaten_lv4.boundary_bottom = 400
        eaten_lv4.change_y = 4
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 600
        eaten_lv4.rect.y = 20
        eaten_lv4.boundary_left = 600
        eaten_lv4.boundary_right = 800
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 800
        eaten_lv4.rect.y = 200
        eaten_lv4.boundary_top = 100
        eaten_lv4.boundary_bottom = 400
        eaten_lv4.change_y = 4
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 979
        eaten_lv4.rect.y = 370
        eaten_lv4.boundary_left = 979
        eaten_lv4.boundary_right = 1200
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 1300
        eaten_lv4.rect.y = 200
        eaten_lv4.boundary_top = 100
        eaten_lv4.boundary_bottom = 400
        eaten_lv4.change_y = 4
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 1500
        eaten_lv4.rect.y = 200
        eaten_lv4.boundary_top = 100
        eaten_lv4.boundary_bottom = 400
        eaten_lv4.change_y = 4
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv4.rect.x = 1600
        eaten_lv4.rect.y = 280
        eaten_lv4.boundary_left = 1600
        eaten_lv4.boundary_right = 1800
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten_lv4.rect.x = 979
        eaten_lv4.rect.y = 30
        eaten_lv4.boundary_left = 979
        eaten_lv4.boundary_right = 1100
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)

        eaten_lv4 = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten_lv4.rect.x = 1045
        eaten_lv4.rect.y = 480
        eaten_lv4.boundary_left = 1045
        eaten_lv4.boundary_right = 1150
        eaten_lv4.change_x = 3
        eaten_lv4.player = self.player
        eaten_lv4.level = self
        self.enemy_list_lv4.add(eaten_lv4)
