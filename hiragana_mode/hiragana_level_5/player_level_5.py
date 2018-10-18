# name file : player_level_5.py
# python version 3
"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""

# import pygame module
import os
import pygame
from pygame.locals import *
# import constans variable
import constants
# import game screen modules
from game_screens import endscreen
from hiragana_mode.overscreen_hiragana import (
    dead_hiragana_level_5, dead_hiragana_level_6,
    dead_hiragana_level_7, dead_hiragana_level_8,
    dead_hiragana_level_9, dead_hiragana_level_10,
    dead_hiragana_level_11
)
# import sounds module
from game_settings import configsounds
# import moving platform modules
from platforms.platforms_red_brick import MovingPlatform_brick_red
from platforms.platforms_snow import MovingPlatform_snow
from platforms.platforms_sand_dirt import MovingPlatform_dirt_sand
from platforms.platforms_ancient_brick import MovingPlatform_ancient_brick
from platforms.platforms_lava_rock import MovingPlatform_lava_rock
# import spritesheet module
from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
    # This class represents the player controls.

    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # set scores for player
        self.scores = 0
        # set kills for player
        self.kills = 0
        # set health number for player
        self.health_number = 100
        # set restore health percentage
        self.give_health = 20
        # set damage for enemy
        self.general_enemy_dmg = 20
        self.special_enemy_dmg = 40
        self.false_point_dmg = 40
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # removing special enemy
        # Level 5
        # Vocal T
        self.special_remove_TA = None
        self.special_remove_TI = None
        self.special_remove_TU = None
        self.special_remove_TE = None
        self.special_remove_TO = None

        # Level 6
        # Vocal N
        self.special_remove_NA = None
        self.special_remove_NI = None
        self.special_remove_NU = None
        self.special_remove_NE = None
        self.special_remove_NO = None

        # Level 7
        # Vocal H
        self.special_remove_HA = None
        self.special_remove_HI = None
        self.special_remove_HU = None
        self.special_remove_HE = None
        self.special_remove_HO = None

        # Level 8
        # Vocal M
        self.special_remove_MA = None
        self.special_remove_MI = None
        self.special_remove_MU = None
        self.special_remove_ME = None
        self.special_remove_MO = None

        # Level 9
        # Vocal Y
        self.special_remove_YA = None
        self.special_remove_YU = None
        self.special_remove_YO = None

        # Level 10
        # Vocal R
        self.special_remove_RA = None
        self.special_remove_RI = None
        self.special_remove_RU = None
        self.special_remove_RE = None
        self.special_remove_RO = None

        # FOR LEVEL 11
        # Vocal W
        self.special_remove_WA = None
        self.special_remove_WO = None

        # Vocal N
        self.special_remove_N = None




        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("spritesheet/player.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(10, 7, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(85, 7, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(160, 7, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(10, 106, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(85, 106, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(160, 106, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(10, 208, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(85, 208, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(160, 208, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(10, 305, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(85, 305, 66, 90)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(10, 7, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(85, 7, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(160, 7, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(10, 106, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(85, 106, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(160, 106, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(10, 208, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(85, 208, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(160, 208, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(10, 305, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(85, 305, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # for platform_list
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform_brick_red):
                self.rect.x += block.change_x
            
            elif isinstance(block, MovingPlatform_snow):
                self.rect.x += block.change_x
            
            elif isinstance(block, MovingPlatform_dirt_sand):
                self.rect.x += block.change_x
            
            elif isinstance(block, MovingPlatform_ancient_brick):
                self.rect.x += block.change_x
            
            elif isinstance(block, MovingPlatform_lava_rock):
                self.rect.x += block.change_x

        # For general enemy list
        # If player touched by enemys
        hit_by_enemy_list_lv5 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv5, True)
        
        hit_by_enemy_list_lv6 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv6, True)
        
        hit_by_enemy_list_lv7 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv7, True)
        
        hit_by_enemy_list_lv8 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv8, True)
        
        hit_by_enemy_list_lv9 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv9, True)
        
        hit_by_enemy_list_lv10 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv10, True)
        
        hit_by_enemy_list_lv11 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv11, True)
        

        for eaten_lv5 in hit_by_enemy_list_lv5:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_5.show_game_over_hiragana()
        
        for eaten_lv6 in hit_by_enemy_list_lv6:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_6.show_game_over_hiragana()
        
        for eaten_lv7 in hit_by_enemy_list_lv7:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_7.show_game_over_hiragana()
        
        for eaten_lv8 in hit_by_enemy_list_lv8:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_8.show_game_over_hiragana()
        
        for eaten_lv9 in hit_by_enemy_list_lv9:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_9.show_game_over_hiragana()
        
        for eaten_lv10 in hit_by_enemy_list_lv10:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_10.show_game_over_hiragana()
        
        for eaten_lv11 in hit_by_enemy_list_lv11:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_11.show_game_over_hiragana()


        # for special enemy list
        # If player touched by special enemys

        # FOR LEVEL 5
        # Vocal T
        # Symbol TA
        special_hit_enemy_list_TA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_TA, True)
        for special_eaten_TA in special_hit_enemy_list_TA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_TA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_5.show_game_over_hiragana()

        # Symbol TI
        special_hit_enemy_list_TI = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_TI, True)
        for special_eaten_TI in special_hit_enemy_list_TI:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_TI == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_5.show_game_over_hiragana()

        # Symbol TU
        special_hit_enemy_list_TU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_TU, True)
        for special_eaten_TU in special_hit_enemy_list_TU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_TU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_5.show_game_over_hiragana()

        # Symbol TE
        special_hit_enemy_list_TE = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_TE, True)
        for special_eaten_TE in special_hit_enemy_list_TE:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_TE == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_5.show_game_over_hiragana()

        # Symbol TO
        special_hit_enemy_list_TO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_TO, True)
        for special_eaten_TO in special_hit_enemy_list_TO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_TO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_5.show_game_over_hiragana()


        # FOR LEVEL 6
        # Vocal N
        # Symbol NA
        special_hit_enemy_list_NA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_NA, True)
        for special_eaten_NA in special_hit_enemy_list_NA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_NA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_6.show_game_over_hiragana()

        # Symbol NI
        special_hit_enemy_list_NI = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_NI, True)
        for special_eaten_NI in special_hit_enemy_list_NI:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_NI == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_6.show_game_over_hiragana()

        # Symbol NU
        special_hit_enemy_list_NU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_NU, True)
        for special_eaten_NU in special_hit_enemy_list_NU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_NU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_6.show_game_over_hiragana()

        # Symbol NE
        special_hit_enemy_list_NE = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_NE, True)
        for special_eaten_NE in special_hit_enemy_list_NE:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_NE == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_6.show_game_over_hiragana()

        # Symbol NO
        special_hit_enemy_list_NO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_NO, True)
        for special_eaten_NO in special_hit_enemy_list_NO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_NO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_6.show_game_over_hiragana()


        # FOR LEVEL 7
        # Vocal H
        # Symbol HA
        special_hit_enemy_list_HA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_HA, True)
        for special_eaten_HA in special_hit_enemy_list_HA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_HA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_7.show_game_over_hiragana()

        # Symbol HI
        special_hit_enemy_list_HI = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_HI, True)
        for special_eaten_HI in special_hit_enemy_list_HI:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_HI == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_7.show_game_over_hiragana()

        # Symbol HU
        special_hit_enemy_list_HU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_HU, True)
        for special_eaten_HU in special_hit_enemy_list_HU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_HU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_7.show_game_over_hiragana()

        # Symbol HE
        special_hit_enemy_list_HE = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_HE, True)
        for special_eaten_HE in special_hit_enemy_list_HE:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_HE == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_7.show_game_over_hiragana()

        # Symbol HO
        special_hit_enemy_list_HO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_HO, True)
        for special_eaten_HO in special_hit_enemy_list_HO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_HO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_7.show_game_over_hiragana()
        

        # FOR LEVEL 8
        # Vocal M
        # Symbol MA
        special_hit_enemy_list_MA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_MA, True)
        for special_eaten_MA in special_hit_enemy_list_MA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_MA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_8.show_game_over_hiragana()

        # Symbol MI
        special_hit_enemy_list_MI = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_MI, True)
        for special_eaten_MI in special_hit_enemy_list_MI:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_MI == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_8.show_game_over_hiragana()

        # Symbol MU
        special_hit_enemy_list_MU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_MU, True)
        for special_eaten_MU in special_hit_enemy_list_MU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_MU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_8.show_game_over_hiragana()

        # Symbol ME
        special_hit_enemy_list_ME = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_ME, True)
        for special_eaten_ME in special_hit_enemy_list_ME:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_ME == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_8.show_game_over_hiragana()

        # Symbol MO
        special_hit_enemy_list_MO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_MO, True)
        for special_eaten_MO in special_hit_enemy_list_MO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_MO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_8.show_game_over_hiragana()
        

        # FOR LEVEL 9
        # Vocal Y
        # Symbol YA
        special_hit_enemy_list_YA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_YA, True)
        for special_eaten_YA in special_hit_enemy_list_YA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_YA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_9.show_game_over_hiragana()

        # Symbol YU
        special_hit_enemy_list_YU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_YU, True)
        for special_eaten_YU in special_hit_enemy_list_YU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_YU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_9.show_game_over_hiragana()

        # Symbol YO
        special_hit_enemy_list_YO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_YO, True)
        for special_eaten_YO in special_hit_enemy_list_YO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_YO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_9.show_game_over_hiragana()
        

        # FOR LEVEL 10
        # Vocal R
        # Symbol RA
        special_hit_enemy_list_RA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RA, True)
        for special_eaten_RA in special_hit_enemy_list_RA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_10.show_game_over_hiragana()

        # Symbol RI
        special_hit_enemy_list_RI = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RI, True)
        for special_eaten_RI in special_hit_enemy_list_RI:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RI == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_10.show_game_over_hiragana()

        # Symbol RU
        special_hit_enemy_list_RU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RU, True)
        for special_eaten_RU in special_hit_enemy_list_RU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_10.show_game_over_hiragana()

        # Symbol RE
        special_hit_enemy_list_RE = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RE, True)
        for special_eaten_RE in special_hit_enemy_list_RE:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RE == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_10.show_game_over_hiragana()

        # Symbol RO
        special_hit_enemy_list_RO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RO, True)
        for special_eaten_RO in special_hit_enemy_list_RO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_10.show_game_over_hiragana()
        

        # FOR LEVEL 11
        # Vocal W
        # Symbol WA
        special_hit_enemy_list_WA = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_WA, True)
        for special_eaten_WA in special_hit_enemy_list_WA:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_WA == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_11.show_game_over_hiragana()

        # Symbol WO
        special_hit_enemy_list_WO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_WO, True)
        for special_eaten_WO in special_hit_enemy_list_WO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_WO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_11.show_game_over_hiragana()

        # Vocal Single N
        special_hit_enemy_list_N = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_N, True)
        for special_eaten_N in special_hit_enemy_list_N:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_N == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_hiragana_level_11.show_game_over_hiragana()


        # for portal list
        go_to_portal_list = pygame.sprite.spritecollide(
            self, self.level.portal_list, True)
        for gate in go_to_portal_list:
            configsounds.portal_sfx.play()

        # for restore health
        restore_health_player = pygame.sprite.spritecollide(
            self, self.level.love_restore_health, True)
        for love_restore in restore_health_player:

            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.health_number += self.give_health

            total_health = self.health_number + self.give_health

            if total_health > 100:
                self.health_number = self.health_number - self.give_health

        # debugging purpose
        # print(self.health_number)

        # for death sprite 
        you_die_in_hell_lv5 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv5, False)
        
        you_die_in_hell_lv6 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv6, False)
        
        you_die_in_hell_lv7 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv7, False)
        
        you_die_in_hell_lv8 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv8, False)
        
        you_die_in_hell_lv9 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv9, False)
        
        you_die_in_hell_lv10 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv10, False)
        
        you_die_in_hell_lv11 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv11, False)

        # effect from death sprite list
        for water_suicide_lv5 in you_die_in_hell_lv5:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_5.show_game_over_hiragana()
        
        for water_suicide_lv6 in you_die_in_hell_lv6:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_6.show_game_over_hiragana()
        
        for water_suicide_lv7 in you_die_in_hell_lv7:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_7.show_game_over_hiragana()
        
        for water_suicide_lv8 in you_die_in_hell_lv8:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_8.show_game_over_hiragana()
        
        for water_suicide_lv9 in you_die_in_hell_lv9:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_9.show_game_over_hiragana()
        
        for lava_water_suicide_10 in you_die_in_hell_lv10:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_10.show_game_over_hiragana()
        
        for lava_water_suicide_11 in you_die_in_hell_lv11:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_hiragana_level_11.show_game_over_hiragana()
        

        # for NPC purpose
        meet_himesama = pygame.sprite.spritecollide(
            self, self.level.himesama_list, False)
        for kiss_himesama in meet_himesama:
            endscreen.show_end_screen_hiragana()

        # For level 5 Hiragana Mode
        point1_hiragana_lv5 = pygame.sprite.spritecollide(
            self, self.level.hiragana_TA, True)
        point2_hiragana_lv5 = pygame.sprite.spritecollide(
            self, self.level.hiragana_TI, True)
        point3_hiragana_lv5 = pygame.sprite.spritecollide(
            self, self.level.hiragana_TU, True)
        point4_hiragana_lv5 = pygame.sprite.spritecollide(
            self, self.level.hiragana_TE, True)
        point5_hiragana_lv5 = pygame.sprite.spritecollide(
            self, self.level.hiragana_TO, True)

        # If user get point hiragana TA
        for true_point_lv5 in point1_hiragana_lv5:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_TA = True

        # If user get point hiragana TI
        for true_point_lv5 in point2_hiragana_lv5:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_TI = True

        # If user get point hiragana TU
        for true_point_lv5 in point3_hiragana_lv5:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_TU = True

        # If user get point hiragana Te
        for true_point_lv5 in point4_hiragana_lv5:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_TE = True

        # If user get point hiragana TO
        for true_point_lv5 in point5_hiragana_lv5:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_TO = True
        

        # For level 6 Hiragana Mode
        point1_hiragana_lv6 = pygame.sprite.spritecollide(
            self, self.level.hiragana_NA, True)
        point2_hiragana_lv6 = pygame.sprite.spritecollide(
            self, self.level.hiragana_NI, True)
        point3_hiragana_lv6 = pygame.sprite.spritecollide(
            self, self.level.hiragana_NU, True)
        point4_hiragana_lv6 = pygame.sprite.spritecollide(
            self, self.level.hiragana_NE, True)
        point5_hiragana_lv6 = pygame.sprite.spritecollide(
            self, self.level.hiragana_NO, True)

        # If user get point hiragana NA
        for true_point_lv6 in point1_hiragana_lv6:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_NA = True

        # If user get point hiragana NI
        for true_point_lv6 in point2_hiragana_lv6:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_NI = True

        # If user get point hiragana NU
        for true_point_lv6 in point3_hiragana_lv6:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_NU = True

        # If user get point hiragana NE
        for true_point_lv6 in point4_hiragana_lv6:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_NE = True

        # If user get point hiragana NO
        for true_point_lv6 in point5_hiragana_lv6:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_NO = True
        

        # For level 7 Hiragana Mode
        point1_hiragana_lv7 = pygame.sprite.spritecollide(
            self, self.level.hiragana_HA, True)
        point2_hiragana_lv7 = pygame.sprite.spritecollide(
            self, self.level.hiragana_HI, True)
        point3_hiragana_lv7 = pygame.sprite.spritecollide(
            self, self.level.hiragana_HU, True)
        point4_hiragana_lv7 = pygame.sprite.spritecollide(
            self, self.level.hiragana_HE, True)
        point5_hiragana_lv7 = pygame.sprite.spritecollide(
            self, self.level.hiragana_HO, True)

        # If user get point hiragana HA
        for true_point_lv7 in point1_hiragana_lv7:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_HA = True

        # If user get point hiragana HI
        for true_point_lv7 in point2_hiragana_lv7:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_HI = True

        # If user get point hiragana HU
        for true_point_lv7 in point3_hiragana_lv7:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_HU = True

        # If user get point hiragana HE
        for true_point_lv7 in point4_hiragana_lv7:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_HE = True

        # If user get point hiragana HO
        for true_point_lv7 in point5_hiragana_lv7:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_HO = True
        

        # For level 8 Hiragana Mode
        point1_hiragana_lv8 = pygame.sprite.spritecollide(
            self, self.level.hiragana_MA, True)
        point2_hiragana_lv8 = pygame.sprite.spritecollide(
            self, self.level.hiragana_MI, True)
        point3_hiragana_lv8 = pygame.sprite.spritecollide(
            self, self.level.hiragana_MU, True)
        point4_hiragana_lv8 = pygame.sprite.spritecollide(
            self, self.level.hiragana_ME, True)
        point5_hiragana_lv8 = pygame.sprite.spritecollide(
            self, self.level.hiragana_MO, True)

        # If user get point hiragana MA
        for true_point_lv8 in point1_hiragana_lv8:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_MA = True

        # If user get point hiragana MI
        for true_point_lv8 in point2_hiragana_lv8:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_MI = True

        # If user get point hiragana MU
        for true_point_lv8 in point3_hiragana_lv8:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_MU = True

        # If user get point hiragana Me
        for true_point_lv8 in point4_hiragana_lv8:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_ME = True

        # If user get point hiragana MO
        for true_point_lv8 in point5_hiragana_lv8:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_MO = True
        

        # FOR LEVEL 9 Hiragana Mode
        point1_hiragana_lv9 = pygame.sprite.spritecollide(
            self, self.level.hiragana_YA, True)
        point2_hiragana_lv9 = pygame.sprite.spritecollide(
            self, self.level.hiragana_YU, True)
        point3_hiragana_lv9 = pygame.sprite.spritecollide(
            self, self.level.hiragana_YO, True)

        # If user get point hiragana YA
        for true_point_lv9 in point1_hiragana_lv9:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_YA = True

        # If user get point hiragana YU
        for true_point_lv9 in point2_hiragana_lv9:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_YU = True

        # If user get point hiragana YO
        for true_point_lv9 in point3_hiragana_lv9:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_YO = True
        

        # For level 10 Hiragana Mode
        point1_hiragana_lv10 = pygame.sprite.spritecollide(
            self, self.level.hiragana_RA, True)
        point2_hiragana_lv10 = pygame.sprite.spritecollide(
            self, self.level.hiragana_RI, True)
        point3_hiragana_lv10 = pygame.sprite.spritecollide(
            self, self.level.hiragana_RU, True)
        point4_hiragana_lv10 = pygame.sprite.spritecollide(
            self, self.level.hiragana_RE, True)
        point5_hiragana_lv10 = pygame.sprite.spritecollide(
            self, self.level.hiragana_RO, True)

        # If user get point hiragana RA
        for true_point_lv10 in point1_hiragana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RA = True

        # If user get point hiragana RI
        for true_point_lv10 in point2_hiragana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RI = True

        # If user get point hiragana RU
        for true_point_lv10 in point3_hiragana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RU = True

        # If user get point hiragana Re
        for true_point_lv10 in point4_hiragana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RE = True

        # If user get point hiragana RO
        for true_point_lv10 in point5_hiragana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RO = True


        # For level 11 Hiragana Mode
        point1_hiragana_lv11 = pygame.sprite.spritecollide(
            self, self.level.hiragana_WA, True)
        point2_hiragana_lv11 = pygame.sprite.spritecollide(
            self, self.level.hiragana_WO, True)
        point3_hiragana_lv11 = pygame.sprite.spritecollide(
            self, self.level.hiragana_N, True)

        # If user get point hiragana WA
        for true_point_lv11 in point1_hiragana_lv11:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_WA = True

        # If user get point hiragana WO
        for true_point_lv11 in point2_hiragana_lv11:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_WO = True

        # If user get point hiragana N
        for true_point_lv11 in point3_hiragana_lv11:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_N = True


    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height \
                and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        """
        Move down a bit and see if there is a platform below us.
        Move down 2 pixels because it doesn't work well if we only move down 1
        when working with a platform moving down.
        """

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or \
                self.rect.bottom >= constants.SCREEN_HEIGHT:
            # play the sound
            configsounds.jump_sfx.play()
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


# class for bullet
class Bullet(Player):
    """ This Class represent the bullet from player"""

    def __init__(self, player):
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(constants.MAGIC_BULLET)

        self.rect = self.image.get_rect()

        self.bullet_list = pygame.sprite.Group()

        # access variable from player class
        self.direction = player.direction
        self.level = player.level

        # confirmation value
        self.confirm_hiragana = None

        # for special enemy
        # FOR LEVEL 5
        # Vocal T
        self.special_remove_TA = player.special_remove_TA
        self.special_remove_TI = player.special_remove_TI
        self.special_remove_TU = player.special_remove_TU
        self.special_remove_TE = player.special_remove_TE
        self.special_remove_TO = player.special_remove_TO

        # FOR LEVEL 6
        # Vocal N
        self.special_remove_NA = player.special_remove_NA
        self.special_remove_NI = player.special_remove_NI
        self.special_remove_NU = player.special_remove_NU
        self.special_remove_NE = player.special_remove_NE
        self.special_remove_NO = player.special_remove_NO

        # FOR LEVEL 7
        # Vocal H
        self.special_remove_HA = player.special_remove_HA
        self.special_remove_HI = player.special_remove_HI
        self.special_remove_HU = player.special_remove_HU
        self.special_remove_HE = player.special_remove_HE
        self.special_remove_HO = player.special_remove_HO

        # FOR LEVEL 8
        # Vocal M
        self.special_remove_MA = player.special_remove_MA
        self.special_remove_MI = player.special_remove_MI
        self.special_remove_MU = player.special_remove_MU
        self.special_remove_ME = player.special_remove_ME
        self.special_remove_MO = player.special_remove_MO

        # FOR LEVEL 9
        # Vocal Y
        self.special_remove_YA = player.special_remove_YA
        self.special_remove_YU = player.special_remove_YU
        self.special_remove_YO = player.special_remove_YO

        # FOR LEVEL 10
        # Vocal R
        self.special_remove_RA = player.special_remove_RA
        self.special_remove_RI = player.special_remove_RI
        self.special_remove_RU = player.special_remove_RU
        self.special_remove_RE = player.special_remove_RE
        self.special_remove_RO = player.special_remove_RO

        # FOR LEVEL 11
        # Vocal W
        self.special_remove_WA = player.special_remove_WA
        self.special_remove_WO = player.special_remove_WO

        # Vocal N
        self.special_remove_N = player.special_remove_N


        self.kills = player.kills

    def update(self):
        """ move the bullet """
        if self.direction == "R":
            self.rect.x += 5
        # print(self.special_remove_A)
        # print(self.special_remove_I)
        elif self.direction == "L":
            self.rect.x -= 5

        # when hit enemy the bullet is gone
        hitting_enemy_lv5 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv5, True)
        hitting_enemy_lv6 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv6, True)
        hitting_enemy_lv7 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv7, True)
        hitting_enemy_lv8 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv8, True)
        hitting_enemy_lv9 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv9, True)
        hitting_enemy_lv10 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv10, True)
        hitting_enemy_lv11 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv11, True)

        for eaten_lv5 in hitting_enemy_lv5:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        for eaten_lv6 in hitting_enemy_lv6:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        for eaten_lv7 in hitting_enemy_lv7:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        for eaten_lv8 in hitting_enemy_lv8:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        for eaten_lv9 in hitting_enemy_lv9:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        for eaten_lv10 in hitting_enemy_lv10:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        for eaten_lv11 in hitting_enemy_lv11:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()

        # just for special enemy list they are immune
        # if the player not get point mission enemy are immnune
        # if the player get point mission enemy are not immnune

        # FOR LEVEL 5
        # for point mission symbol TA
        if self.special_remove_TA:
            hitting_special_enemy_TA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TA, True)
        elif not self.special_remove_TA:
            hitting_special_enemy_TA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TA, False)

        # for point mission symbol TI
        if self.special_remove_TI:
            hitting_special_enemy_TI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TI, True)
        elif not self.special_remove_TI:
            hitting_special_enemy_TI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TI, False)

        # for point mission symbol TI
        if self.special_remove_TU:
            hitting_special_enemy_TU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TU, True)
        elif not self.special_remove_TU:
            hitting_special_enemy_TU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TU, False)

        # for point mission symbol TE
        if self.special_remove_TE:
            hitting_special_enemy_TE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TE, True)
        elif not self.special_remove_TE:
            hitting_special_enemy_TE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TE, False)

        # for point mission symbol TO
        if self.special_remove_TO:
            hitting_special_enemy_TO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TO, True)
        elif not self.special_remove_TO:
            hitting_special_enemy_TO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_TO, False)
        

        # FOR LEVEL 6
        # for point mission symbol NA
        if self.special_remove_NA:
            hitting_special_enemy_NA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NA, True)
        elif not self.special_remove_NA:
            hitting_special_enemy_NA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NA, False)

        # for point mission symbol NI
        if self.special_remove_NI:
            hitting_special_enemy_NI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NI, True)
        elif not self.special_remove_NI:
            hitting_special_enemy_NI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NI, False)

        # for point mission symbol NU
        if self.special_remove_NU:
            hitting_special_enemy_NU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NU, True)
        elif not self.special_remove_NU:
            hitting_special_enemy_NU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NU, False)

        # for point mission symbol NE
        if self.special_remove_NE:
            hitting_special_enemy_NE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NE, True)
        elif not self.special_remove_NE:
            hitting_special_enemy_NE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NE, False)

        # for point mission symbol NO
        if self.special_remove_NO:
            hitting_special_enemy_NO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NO, True)
        elif not self.special_remove_NO:
            hitting_special_enemy_NO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_NO, False)
        

        # FOR LEVEL 7
        # for point mission symbol HA
        if self.special_remove_HA:
            hitting_special_enemy_HA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HA, True)
        elif not self.special_remove_HA:
            hitting_special_enemy_HA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HA, False)

        # for point mission symbol HI
        if self.special_remove_HI:
            hitting_special_enemy_HI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HI, True)
        elif not self.special_remove_HI:
            hitting_special_enemy_HI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HI, False)

        # for point mission symbol HU
        if self.special_remove_HU:
            hitting_special_enemy_HU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HU, True)
        elif not self.special_remove_HU:
            hitting_special_enemy_HU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HU, False)

        # for point mission symbol HE
        if self.special_remove_HE:
            hitting_special_enemy_HE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HE, True)
        elif not self.special_remove_HE:
            hitting_special_enemy_HE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HE, False)

        # for point mission symbol HO
        if self.special_remove_HO:
            hitting_special_enemy_HO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HO, True)
        elif not self.special_remove_HO:
            hitting_special_enemy_HO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_HO, False)
        

        # FOR LEVEL 8
        # for point mission symbol MA
        if self.special_remove_MA:
            hitting_special_enemy_MA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MA, True)
        elif not self.special_remove_MA:
            hitting_special_enemy_MA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MA, False)

        # for point mission symbol MI
        if self.special_remove_MI:
            hitting_special_enemy_MI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MI, True)
        elif not self.special_remove_MI:
            hitting_special_enemy_MI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MI, False)

        # for point mission symbol MI
        if self.special_remove_MU:
            hitting_special_enemy_MU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MU, True)
        elif not self.special_remove_MU:
            hitting_special_enemy_MU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MU, False)

        # for point mission symbol ME
        if self.special_remove_ME:
            hitting_special_enemy_ME = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_ME, True)
        elif not self.special_remove_ME:
            hitting_special_enemy_ME = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_ME, False)

        # for point mission symbol MO
        if self.special_remove_MO:
            hitting_special_enemy_MO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MO, True)
        elif not self.special_remove_MO:
            hitting_special_enemy_MO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_MO, False)
        

        # FOR LEVEL 9
        # for point mission symbol YA
        if self.special_remove_YA:
            hitting_special_enemy_YA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_YA, True)
        elif not self.special_remove_YA:
            hitting_special_enemy_YA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_YA, False)

        # for point mission symbol YU
        if self.special_remove_YU:
            hitting_special_enemy_YU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_YU, True)
        elif not self.special_remove_YU:
            hitting_special_enemy_YU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_YU, False)

        # for point mission symbol YO
        if self.special_remove_YO:
            hitting_special_enemy_YO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_YO, True)
        elif not self.special_remove_YO:
            hitting_special_enemy_YO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_YO, False)


        # FOR LEVEL 10
        # for point mission symbol RA
        if self.special_remove_RA:
            hitting_special_enemy_RA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RA, True)
        elif not self.special_remove_RA:
            hitting_special_enemy_RA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RA, False)

        # for point mission symbol RI
        if self.special_remove_RI:
            hitting_special_enemy_RI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RI, True)
        elif not self.special_remove_RI:
            hitting_special_enemy_RI = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RI, False)

        # for point mission symbol RU
        if self.special_remove_RU:
            hitting_special_enemy_RU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RU, True)
        elif not self.special_remove_RU:
            hitting_special_enemy_RU = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RU, False)

        # for point mission symbol RE
        if self.special_remove_RE:
            hitting_special_enemy_RE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RE, True)
        elif not self.special_remove_RE:
            hitting_special_enemy_RE = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RE, False)

        # for point mission symbol RO
        if self.special_remove_RO:
            hitting_special_enemy_RO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RO, True)
        elif not self.special_remove_RO:
            hitting_special_enemy_RO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_RO, False)
        

        # FOR LEVEL 11
        # for point mision symbol WA
        if self.special_remove_WA:
            hitting_special_enemy_WA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_WA, True)
        elif not self.special_remove_WA:
            hitting_special_enemy_WA = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_WA, False)

        # for point mission symbol WO
        if self.special_remove_WO:
            hitting_special_enemy_WO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_WO, True)
        elif not self.special_remove_WO:
            hitting_special_enemy_WO = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_WO, False)

        # for point mission symbol N
        if self.special_remove_N:
            hitting_special_enemy_N = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_N, True)
        elif not self.special_remove_N:
            hitting_special_enemy_N = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_N, False)


        # attack a special enemy
        # Basic Vocal

        # FOR LEVEL 5
        # Vocal T
        for special_eaten_TA in hitting_special_enemy_TA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ta.play()

                if self.special_remove_TA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TI \
                        or self.special_remove_TU \
                        or self.special_remove_TE \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ta.play()

                if self.special_remove_TA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TI \
                        or self.special_remove_TU \
                        or self.special_remove_TE \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

        for special_eaten_TI in hitting_special_enemy_TI:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_chi.play()

                if self.special_remove_TI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TU \
                        or self.special_remove_TE \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_chi.play()

                if self.special_remove_TI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TU \
                        or self.special_remove_TE \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

        for special_eaten_TU in hitting_special_enemy_TU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_tsu.play()

                if self.special_remove_TU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TI \
                        or self.special_remove_TE \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_tsu.play()

                if self.special_remove_TU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TI \
                        or self.special_remove_TE \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

        for special_eaten_TE in hitting_special_enemy_TE:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_te.play()

                if self.special_remove_TE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TI \
                        or self.special_remove_TU \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_te.play()

                if self.special_remove_TE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TI \
                        or self.special_remove_TU \
                        or self.special_remove_TO == True:
                    self.confirm_hiragana = False

        for special_eaten_TO in hitting_special_enemy_TO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_to.play()

                if self.special_remove_TO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TI \
                        or self.special_remove_TU \
                        or self.special_remove_TE == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_to.play()

                if self.special_remove_TO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_TA \
                        or self.special_remove_TI \
                        or self.special_remove_TU \
                        or self.special_remove_TE == True:
                    self.confirm_hiragana = False
        

        # FOR LEVEL 6
        # Vocal N
        for special_eaten_NA in hitting_special_enemy_NA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_na.play()
                
                if self.special_remove_NA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NI \
                        or self.special_remove_NU \
                        or self.special_remove_NE \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False
            
            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_na.play()

                if self.special_remove_NA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NI \
                        or self.special_remove_NU \
                        or self.special_remove_NE \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

        for special_eaten_NI in hitting_special_enemy_NI:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ni.play()

                if self.special_remove_NI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NU \
                        or self.special_remove_NE \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ni.play()

                if self.special_remove_NI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NU \
                        or self.special_remove_NE \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

        for special_eaten_NU in hitting_special_enemy_NU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_no.play()

                if self.special_remove_NU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NI \
                        or self.special_remove_NE \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_no.play()

                if self.special_remove_NU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NI \
                        or self.special_remove_NE \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

        for special_eaten_NE in hitting_special_enemy_NE:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ne.play()

                if self.special_remove_NE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NI \
                        or self.special_remove_NU \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ne.play()

                if self.special_remove_NE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NI \
                        or self.special_remove_NU \
                        or self.special_remove_NO == True:
                    self.confirm_hiragana = False

        for special_eaten_NO in hitting_special_enemy_NO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_no.play()

                if self.special_remove_NO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NI \
                        or self.special_remove_NU \
                        or self.special_remove_NE == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_no.play()

                if self.special_remove_NO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_NA \
                        or self.special_remove_NI \
                        or self.special_remove_NU \
                        or self.special_remove_NE == True:
                    self.confirm_hiragana = False
        

        # FOR LEVEL 7
        # Vocal H
        for special_eaten_HO in hitting_special_enemy_HA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ha.play()

                if self.special_remove_HA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HI \
                        or self.special_remove_HU \
                        or self.special_remove_HE \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ha.play()

                if self.special_remove_HA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HI \
                        or self.special_remove_HU \
                        or self.special_remove_HE \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

        for special_eaten_HI in hitting_special_enemy_HI:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_hi.play()
                
                if self.special_remove_HI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HU \
                        or self.special_remove_HE \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_hi.play()

                if self.special_remove_HI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HU \
                        or self.special_remove_HE \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

        for special_eaten_HU in hitting_special_enemy_HU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_fu.play()

                if self.special_remove_HU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HI \
                        or self.special_remove_HE \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_fu.play()

                if self.special_remove_HU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HI \
                        or self.special_remove_HE \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

        for special_eaten_HE in hitting_special_enemy_HE:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_he.play()

                if self.special_remove_HE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HI \
                        or self.special_remove_HU \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_he.play()

                if self.special_remove_HE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HI \
                        or self.special_remove_HU \
                        or self.special_remove_HO == True:
                    self.confirm_hiragana = False

        for special_eaten_HO in hitting_special_enemy_HO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ho.play()
                
                if self.special_remove_HO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HI \
                        or self.special_remove_HU \
                        or self.special_remove_HE == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ho.play()

                if self.special_remove_HO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_HA \
                        or self.special_remove_HI \
                        or self.special_remove_HU \
                        or self.special_remove_HE == True:
                    self.confirm_hiragana = False
        

        # FOR LEVEL 8
        # Vocal M
        for special_eaten_MA in hitting_special_enemy_MA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ma.play()

                if self.special_remove_MA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MI \
                        or self.special_remove_MU \
                        or self.special_remove_ME \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ma.play()

                if self.special_remove_MA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MI \
                        or self.special_remove_MU \
                        or self.special_remove_ME \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

        for special_eaten_MI in hitting_special_enemy_MI:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_mi.play()

                if self.special_remove_MI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MU \
                        or self.special_remove_ME \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_mi.play()

                if self.special_remove_MI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MU \
                        or self.special_remove_ME \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

        for special_eaten_MU in hitting_special_enemy_MU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_mu.play()

                if self.special_remove_MU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MI \
                        or self.special_remove_ME \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_mu.play()

                if self.special_remove_MU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MI \
                        or self.special_remove_ME \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

        for special_eaten_ME in hitting_special_enemy_ME:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_me.play()

                if self.special_remove_ME == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MI \
                        or self.special_remove_MU \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_me.play()

                if self.special_remove_ME == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MI \
                        or self.special_remove_MU \
                        or self.special_remove_MO == True:
                    self.confirm_hiragana = False

        for special_eaten_MO in hitting_special_enemy_MO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_mo.play()

                if self.special_remove_MO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MI \
                        or self.special_remove_MU \
                        or self.special_remove_ME == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_mo.play()

                if self.special_remove_MO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_MA \
                        or self.special_remove_MI \
                        or self.special_remove_MU \
                        or self.special_remove_ME == True:
                    self.confirm_hiragana = False

        # FOR LEVEL 9
        # Vocal Y
        for special_eaten_YA in hitting_special_enemy_YA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ya.play()

                if self.special_remove_YA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_YU \
                        or self.special_remove_YO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ya.play()

                if self.special_remove_YA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_YU \
                        or self.special_remove_YO == True:
                    self.confirm_hiragana = False

        for special_eaten_YU in hitting_special_enemy_YU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yu.play()

                if self.special_remove_YU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_YA \
                        or self.special_remove_YO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yu.play()

                if self.special_remove_YU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_YA \
                        or self.special_remove_YO == True:
                    self.confirm_hiragana = False

        for special_eaten_YO in hitting_special_enemy_YO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yo.play()

                if self.special_remove_YO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_YA \
                        or self.special_remove_YU == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yo.play()

                if self.special_remove_YO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_YA \
                        or self.special_remove_YU == True:
                    self.confirm_hiragana = False

        # FOR LEVEL 10
        # Vocal R
        for special_eaten_RA in hitting_special_enemy_RA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ra.play()

                if self.special_remove_RA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ra.play()

                if self.special_remove_RA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

        for special_eaten_RI in hitting_special_enemy_RI:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ri.play()

                if self.special_remove_RI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ri.play()

                if self.special_remove_RI == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

        for special_eaten_RU in hitting_special_enemy_RU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ru.play()

                if self.special_remove_RU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ru.play()

                if self.special_remove_RU == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

        for special_eaten_RE in hitting_special_enemy_RE:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_re.play()

                if self.special_remove_RE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_re.play()

                if self.special_remove_RE == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RO == True:
                    self.confirm_hiragana = False

        for special_eaten_RO in hitting_special_enemy_RO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ro.play()

                if self.special_remove_RO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ro.play()

                if self.special_remove_RO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE == True:
                    self.confirm_hiragana = False

        # FOR LEVEL 11
        # Vocal W
        for special_eaten_WA in hitting_special_enemy_WA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wa.play()

                if self.special_remove_WA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_WO \
                        or self.special_remove_N == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wa.play()

                if self.special_remove_WA == True:
                    self.confirm_hiragana = True
                elif self.special_remove_WO \
                        or self.special_remove_N == True:
                    self.confirm_hiragana = False

        for special_eaten_WO in hitting_special_enemy_WO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wo.play()

                if self.special_remove_WO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_WA \
                        or self.special_remove_N == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wo.play()

                if self.special_remove_WO == True:
                    self.confirm_hiragana = True
                elif self.special_remove_WA \
                        or self.special_remove_N == True:
                    self.confirm_hiragana = False

        # Vocal N
        for special_eaten_N in hitting_special_enemy_N:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_n.play()

                if self.special_remove_N == True:
                    self.confirm_hiragana = True
                elif self.special_remove_WA \
                        or self.special_remove_WO == True:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_n.play()

                if self.special_remove_N == True:
                    self.confirm_hiragana = True
                elif self.special_remove_WA \
                        or self.special_remove_WO == True:
                    self.confirm_hiragana = False

        # when hit platform the bullet is gone
        hitting_platform = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)

        for block in hitting_platform:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
