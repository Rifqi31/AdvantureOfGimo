# name file: level_ending.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import (
    platforms_dirt, platforms_item,
    platforms_npc,
)

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# Create platforms for the level
class Level_Ending(Level):
    """ This class for introduce the player """

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/snow_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms_dirt.dirt_wall, -140, 0],
                 [platforms_dirt.dirt_medium_long_land, 0, 460],
                 [platforms_dirt.dirt_medium_long_land, 480, 460],
                 [platforms_dirt.dirt_big_wall, 769, 0]]

        portal = [[platforms_item.portal_snow, 700, 380]]

        himesama = [[platforms_npc.himesama_blonde, 450, 385]]

        text_himesama = [[platforms_npc.text_himesama, 450, 340]]

        for platform in intro:
            block = platforms_dirt.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # for NPC
        for platform in himesama:
            kiss_himesama = platforms_npc.Platform_NPC(platform[0])
            kiss_himesama.rect.x = platform[1]
            kiss_himesama.rect.y = platform[2]
            kiss_himesama.player = self.player
            self.himesama_list.add(kiss_himesama)

        for platform in text_himesama:
            gate = platforms_npc.Platform_NPC(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.himesama_list.add(gate)
