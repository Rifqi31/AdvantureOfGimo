# name file: level_10.py
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
class Level_10(Level):
    def __init__(self, player):
        """ Definition for Level 10"""

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/lava_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1656

        # Array with type of platform, and x, y location of the platform.
        # for level 10
        level10 = [
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

        lava_water_level10 = [
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
        katakana_ra = [[platforms_katakana.katakana_ra, 1050, 20]]
        katakana_ri = [[platforms_katakana.katakana_ri, 350, 100]]
        katakana_ru = [[platforms_katakana.katakana_ru, 0, 20]]
        katakana_re = [[platforms_katakana.katakana_re, 1650, 100]]
        katakana_ro = [[platforms_katakana.katakana_ro, 1800, 100]]

        # enemys
        slime_lava = [
            [platforms_enemy.orange_slime, 770, 357],
            [platforms_enemy.orange_slime, 805, 357],
            [platforms_enemy.orange_slime, 840, 286],
            [platforms_enemy.orange_slime, 875, 286],
            [platforms_enemy.orange_slime, 910, 216],
            [platforms_enemy.orange_slime, 945, 216]
        ]

        # special enemys
        special_enemy_ro = [[platforms_special_enemy.slime_lava_ro, 2100, 10]]

        for platform in level10:
            block = platforms_lava_rock.Platform_lava_rock(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in lava_water_level10:
            lava_water_suicide_lv10 = platforms_lava_rock.Platform_lava_rock(
                platform[0])
            lava_water_suicide_lv10.rect.x = platform[1]
            lava_water_suicide_lv10.rect.y = platform[2]
            lava_water_suicide_lv10.player = self.player
            self.death_place_list_lv10.add(lava_water_suicide_lv10)

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
            eaten_lv10 = platforms_enemy.Platform_enemy(platform[0])
            eaten_lv10.rect.x = platform[1]
            eaten_lv10.rect.y = platform[2]
            eaten_lv10.player = self.player
            self.enemy_list_lv10.add(eaten_lv10)

        # Special enemys
        # katakana Ro
        for platform in special_enemy_ro:
            special_eaten_RO = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_RO.rect.x = platform[1]
            special_eaten_RO.rect.y = platform[2]
            special_eaten_RO.player = self.player
            self.special_enemy_list_RO.add(special_eaten_RO)

        # Point
        # katakana Ra
        for platform in katakana_ra:
            true_point_lv10 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.katakana_RA.add(true_point_lv10)

        # katakana RI
        for platform in katakana_ri:
            true_point_lv10 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.katakana_RI.add(true_point_lv10)

        # katakana Ru
        for platform in katakana_ru:
            true_point_lv10 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.katakana_RU.add(true_point_lv10)

        # katakana Re
        for platform in katakana_re:
            true_point_lv10 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.katakana_RE.add(true_point_lv10)

        # katakana Ro
        for platform in katakana_ro:
            true_point_lv10 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.katakana_RO.add(true_point_lv10)

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
        eaten_lv10 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv10.rect.x = 1540
        eaten_lv10.rect.y = 350
        eaten_lv10.boundary_left = 1540
        eaten_lv10.boundary_right = 1780
        eaten_lv10.change_x = 5
        eaten_lv10.player = self.player
        eaten_lv10.level = self
        self.enemy_list_lv10.add(eaten_lv10)

        eaten_lv10 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv10.rect.x = 1540
        eaten_lv10.rect.y = 350
        eaten_lv10.boundary_left = 1540
        eaten_lv10.boundary_right = 1780
        eaten_lv10.change_x = 3
        eaten_lv10.player = self.player
        eaten_lv10.level = self
        self.enemy_list_lv10.add(eaten_lv10)

        eaten_lv10 = platforms_enemy.MovingEnemy(platforms_enemy.old_skull)
        eaten_lv10.rect.x = 1540
        eaten_lv10.rect.y = 350
        eaten_lv10.boundary_left = 1540
        eaten_lv10.boundary_right = 1780
        eaten_lv10.change_x = 2
        eaten_lv10.player = self.player
        eaten_lv10.level = self
        self.enemy_list_lv10.add(eaten_lv10)

        eaten_lv10 = platforms_enemy.MovingEnemy(platforms_enemy.dark_bat)
        eaten_lv10.rect.x = 1960
        eaten_lv10.rect.y = 110
        eaten_lv10.boundary_top = 100
        eaten_lv10.boundary_bottom = 450
        eaten_lv10.change_y = 3
        eaten_lv10.player = self.player
        eaten_lv10.level = self
        self.enemy_list_lv10.add(eaten_lv10)

        # add moving special enemys
        # katakana Ra
        special_eaten_RA = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_ra)
        special_eaten_RA.rect.x = 560
        special_eaten_RA.rect.y = 10
        special_eaten_RA.boundary_left = 560
        special_eaten_RA.boundary_right = 630
        special_eaten_RA.change_x = 3
        special_eaten_RA.player = self.player
        special_eaten_RA.level = self
        self.special_enemy_list_RA.add(special_eaten_RA)

        # katakana Ri
        special_eaten_RI = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_ri)
        special_eaten_RI.rect.x = 50
        special_eaten_RI.rect.y = 10
        special_eaten_RI.boundary_left = 50
        special_eaten_RI.boundary_right = 150
        special_eaten_RI.change_x = 3
        special_eaten_RI.player = self.player
        special_eaten_RI.level = self
        self.special_enemy_list_RI.add(special_eaten_RI)

        # katakana Ru
        special_eaten_RU = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_ru)
        special_eaten_RU.rect.x = 1540
        special_eaten_RU.rect.y = 320
        special_eaten_RU.boundary_left = 1540
        special_eaten_RU.boundary_right = 1780
        special_eaten_RU.change_x = 4
        special_eaten_RU.player = self.player
        special_eaten_RU.level = self
        self.special_enemy_list_RU.add(special_eaten_RU)

        # katakana Re
        special_eaten_RE = platforms_special_enemy.MovingEnemySpecial(
            platforms_special_enemy.slime_lava_re)
        special_eaten_RE.rect.x = 1960
        special_eaten_RE.rect.y = 110
        special_eaten_RE.boundary_top = 100
        special_eaten_RE.boundary_bottom = 450
        special_eaten_RE.change_y = 3
        special_eaten_RE.player = self.player
        special_eaten_RE.level = self
        self.special_enemy_list_RE.add(special_eaten_RE)
