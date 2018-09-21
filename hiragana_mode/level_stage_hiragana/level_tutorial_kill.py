# name file: level_tutorial_kill.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_snow,
    platforms_item,
    platforms_bad_sprite,
    platforms_enemy
)

# import levels module
from hiragana_mode.level_stage_hiragana.levels import Level


# for NPC section
class Level_Tutorial_Kill(Level):
    """This class for introduce for player how to play this game"""

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [
            [platforms_snow.snow_dirt_wall, -140, 0],
            [platforms_snow.snow_dirt_grass_medium_large, 0, 530],
            [platforms_snow.snow_dirt_grass_medium_large, 490, 460],
            [platforms_snow.snow_dirt_big_wall, 769, 0]
        ]

        water_intro = [
            [platforms_bad_sprite.medium_long_water, 280, 531],
        ]

        portal = [[platforms_item.portal_snow, 700, 380]]

        for platform in intro:
            block = platforms_snow.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms_item.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in water_intro:
            water_suicide_intro = platforms_bad_sprite.Platform_dirt(
                platform[0])
            water_suicide_intro.rect.x = platform[1]
            water_suicide_intro.rect.y = platform[2]
            water_suicide_intro.player = self.player
            self.death_place_list_tutorial.add(water_suicide_intro)

        # add moving enemys
        eaten_tutorial = platforms_enemy.MovingEnemy(
            platforms_enemy.skull_ghost)
        eaten_tutorial.rect.x = 490
        eaten_tutorial.rect.y = 340
        eaten_tutorial.boundary_left = 490
        eaten_tutorial.boundary_right = 630
        eaten_tutorial.change_x = 4
        eaten_tutorial.player = self.player
        eaten_tutorial.level = self
        self.enemy_list_tutorial.add(eaten_tutorial)

        eaten_tutorial = platforms_enemy.MovingEnemy(
            platforms_enemy.skull_ghost)
        eaten_tutorial.rect.x = 490
        eaten_tutorial.rect.y = 410
        eaten_tutorial.boundary_left = 490
        eaten_tutorial.boundary_right = 630
        eaten_tutorial.change_x = 5
        eaten_tutorial.player = self.player
        eaten_tutorial.level = self
        self.enemy_list_tutorial.add(eaten_tutorial)
