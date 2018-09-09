# name file: level_11.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_lava_rock, platforms_bad_sprite,
    platforms_item, platforms_katakana,
    platforms_enemy, platforms_special_enemy
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_11(Level):
    def __init__(self, player):
        """ Definition for Level 11"""

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/lava_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1656

        # Array with type of platform, and x, y location of the platform.
        # for level 11
        level11 = [
            [platforms_lava_rock.lava_rock_wall, -140, 0],
            [platforms_lava_rock.lava_rock_medium_large_land, 0, 530],
            [platforms_lava_rock.lava_rock_medium_large_land, 280, 530],
            [platforms_lava_rock.lava_rock_small_tall, 770, 390],
            [platforms_lava_rock.lava_rock_medium_tall, 840, 320],
            [platforms_lava_rock.lava_rock_long_tall, 910, 250],
            [platforms_lava_rock.lava_rock_basic, 1050, 98],
            [platforms_lava_rock.lava_rock_basic_medium, 560, 105],
            [platforms_lava_rock.lava_rock_short_small_land, 0, 98],
            [platforms_lava_rock.lava_rock_medium_large_land, 1540, 410],
            [platforms_lava_rock.lava_rock_long_tall, 2100, 110],
            [platforms_lava_rock.lava_rock_medium_large_land, 2380, 410],
            [platforms_lava_rock.lava_rock_big_wall, 2590, 0],
            [platforms_lava_rock.lava_rock_wall, 2870, 0]
        ]

        lava_water_level11 = [
            [platforms_bad_sprite.lava_water_long, 560, 531],
            [platforms_bad_sprite.lava_water_long, 980, 531],
            [platforms_bad_sprite.lava_water_long, 1190, 531],
            [platforms_bad_sprite.lava_water, 1400, 531],
            [platforms_bad_sprite.lava_water, 1470, 531],
            [platforms_bad_sprite.lava_water_long, 1820, 531],
            [platforms_bad_sprite.lava_water, 2030, 531],
            [platforms_bad_sprite.lava_water_long, 2170, 531]
        ]

        portal = [[platforms_item.portal_snow, 2520, 340]]

        love_health = [[platforms_item.restore_health, 70, 20]]

        # katakana Point
        katakana_wa = [[platforms_katakana.katakana_wa, 1050, 20]]
        katakana_wo = [[platforms_katakana.katakana_wo, 350, 100]]
        katakana_n = [[platforms_katakana.katakana_n, 0, 20]]

        # enemys
        slime_lava = [
            [platforms_enemy.orange_slime, 770, 357],
            [platforms_enemy.orange_slime, 805, 357],
            [platforms_enemy.orange_slime, 840, 286],
            [platforms_enemy.orange_slime, 875, 286],
            [platforms_enemy.orange_slime, 910, 216],
            [platforms_enemy.orange_slime, 945, 216]
        ]

        for platform in level11:
            block = platforms_lava_rock.Platform_lava_rock(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in lava_water_level11:
            lava_water_suicide_lv11 = platforms_bad_sprite.Platform_lava_rock(
                platform[0])
            lava_water_suicide_lv11.rect.x = platform[1]
            lava_water_suicide_lv11.rect.y = platform[2]
            lava_water_suicide_lv11.player = self.player
            self.death_place_list_lv11.add(lava_water_suicide_lv11)

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
        for platform in slime_lava:
            eaten_lv11 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv11.rect.x = platform[1]
            eaten_lv11.rect.y = platform[2]
            eaten_lv11.player = self.player
            self.enemy_list_lv11.add(eaten_lv11)

        # Point
        # katakana Wa
        for platform in katakana_wa:
            true_point_lv11 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv11.rect.x = platform[1]
            true_point_lv11.rect.y = platform[2]
            true_point_lv11.player = self.player
            self.katakana_WA.add(true_point_lv11)

        # katakana Wo
        for platform in katakana_wo:
            true_point_lv11 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv11.rect.x = platform[1]
            true_point_lv11.rect.y = platform[2]
            true_point_lv11.player = self.player
            self.katakana_WO.add(true_point_lv11)

        # katakana N
        for platform in katakana_n:
            true_point_lv11 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv11.rect.x = platform[1]
            true_point_lv11.rect.y = platform[2]
            true_point_lv11.player = self.player
            self.katakana_N.add(true_point_lv11)

        # add moving sprites
        block = platforms_lava_rock.MovingPlatform_lava_rock(
            platforms_lava_rock.lava_rock_half)
        block.rect.x = 1960
        block.rect.y = 110
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten_lv11 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv11.rect.x = 1540
        eaten_lv11.rect.y = 350
        eaten_lv11.boundary_left = 1540
        eaten_lv11.boundary_right = 1780
        eaten_lv11.change_x = 5
        eaten_lv11.player = self.player
        eaten_lv11.level = self
        self.enemy_list_lv11.add(eaten_lv11)

        eaten_lv11 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv11.rect.x = 1540
        eaten_lv11.rect.y = 350
        eaten_lv11.boundary_left = 1540
        eaten_lv11.boundary_right = 1780
        eaten_lv11.change_x = 3
        eaten_lv11.player = self.player
        eaten_lv11.level = self
        self.enemy_list_lv11.add(eaten_lv11)

        eaten_lv11 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv11.rect.x = 1540
        eaten_lv11.rect.y = 350
        eaten_lv11.boundary_left = 1540
        eaten_lv11.boundary_right = 1780
        eaten_lv11.change_x = 2
        eaten_lv11.player = self.player
        eaten_lv11.level = self
        self.enemy_list_lv11.add(eaten_lv11)

        eaten_lv11 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv11.rect.x = 1960
        eaten_lv11.rect.y = 110
        eaten_lv11.boundary_top = 100
        eaten_lv11.boundary_bottom = 450
        eaten_lv11.change_y = 3
        eaten_lv11.player = self.player
        eaten_lv11.level = self
        self.enemy_list_lv11.add(eaten_lv11)

        # add moving special enemys
        # katakana Wa
        special_eaten_WA = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_wa)
        special_eaten_WA.rect.x = 560
        special_eaten_WA.rect.y = 10
        special_eaten_WA.boundary_left = 560
        special_eaten_WA.boundary_right = 630
        special_eaten_WA.change_x = 3
        special_eaten_WA.player = self.player
        special_eaten_WA.level = self
        self.special_enemy_list_WA.add(special_eaten_WA)

        # katakana Wo
        special_eaten_WO = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_wo)
        special_eaten_WO.rect.x = 50
        special_eaten_WO.rect.y = 10
        special_eaten_WO.boundary_left = 50
        special_eaten_WO.boundary_right = 150
        special_eaten_WO.change_x = 3
        special_eaten_WO.player = self.player
        special_eaten_WO.level = self
        self.special_enemy_list_WO.add(special_eaten_WO)

        # katakana N
        special_eaten_N = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_n)
        special_eaten_N.rect.x = 1540
        special_eaten_N.rect.y = 320
        special_eaten_N.boundary_left = 1540
        special_eaten_N.boundary_right = 1780
        special_eaten_N.change_x = 4
        special_eaten_N.player = self.player
        special_eaten_N.level = self
        self.special_enemy_list_N.add(special_eaten_N)
