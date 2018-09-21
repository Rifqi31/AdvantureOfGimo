# name file: level_ending_tutorial.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import platforms_snow, platforms_item, platforms_npc

# import levels module
from hiragana_mode.level_stage_hiragana.levels import Level


# for intro how to play the game
class Level_Ending_Tutorial(Level):
    """ This class for introduce the player """

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
            [platforms_snow.snow_dirt_intro, 0, 460],
            [platforms_snow.snow_dirt_big_wall, 769, 0]
        ]

        grandpa = [[platforms_npc.grandpa_magus, 450, 370]]

        text_grandpa = [[platforms_npc.text_grandpa, 450, 320]]

        for platform in intro:
            block = platforms_snow.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        
        # for NPC purpose
        for platform in grandpa:
            talk_grandpa = platforms_npc.Platform_NPC(platform[0])
            talk_grandpa.rect.x = platform[1]
            talk_grandpa.rect.y = platform[2]
            talk_grandpa.player = self.player
            self.grandpa_list.add(talk_grandpa)

        for platform in text_grandpa:
            gate = platforms_npc.Platform_NPC(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.grandpa_list.add(gate)
