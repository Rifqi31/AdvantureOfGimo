# name file : player_level_9.py
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
from katakana_mode.overscreen_katakana import (
    dead_katakana_level_9, dead_katakana_level_10,
    dead_katakana_level_11
)
# import sounds module
from game_settings import configsounds
# import moving platform modules
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
            
            if isinstance(block, MovingPlatform_ancient_brick):
                self.rect.x += block.change_x
            
            elif isinstance(block, MovingPlatform_lava_rock):
                self.rect.x += block.change_x

        # For general enemy list
        # If player touched by enemys
        hit_by_enemy_list_lv9 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv9, True)
        
        hit_by_enemy_list_lv10 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv10, True)
        
        hit_by_enemy_list_lv11 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv11, True)
        
        for eaten_lv9 in hit_by_enemy_list_lv9:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_9.show_game_over_katakana()
        
        for eaten_lv10 in hit_by_enemy_list_lv10:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_10.show_game_over_katakana()
        
        for eaten_lv11 in hit_by_enemy_list_lv11:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_11.show_game_over_katakana()


        # for special enemy list
        # If player touched by special enemys

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
                dead_katakana_level_9.show_game_over_katakana()

        # Symbol YU
        special_hit_enemy_list_YU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_YU, True)
        for special_eaten_YU in special_hit_enemy_list_YU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_YU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_9.show_game_over_katakana()

        # Symbol YO
        special_hit_enemy_list_YO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_YO, True)
        for special_eaten_YO in special_hit_enemy_list_YO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_YO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_9.show_game_over_katakana()
        

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
                dead_katakana_level_10.show_game_over_katakana()

        # Symbol RI
        special_hit_enemy_list_RI = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RI, True)
        for special_eaten_RI in special_hit_enemy_list_RI:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RI == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_10.show_game_over_katakana()

        # Symbol RU
        special_hit_enemy_list_RU = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RU, True)
        for special_eaten_RU in special_hit_enemy_list_RU:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RU == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_10.show_game_over_katakana()

        # Symbol RE
        special_hit_enemy_list_RE = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RE, True)
        for special_eaten_RE in special_hit_enemy_list_RE:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RE == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_10.show_game_over_katakana()

        # Symbol RO
        special_hit_enemy_list_RO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_RO, True)
        for special_eaten_RO in special_hit_enemy_list_RO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_RO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_10.show_game_over_katakana()
        

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
                dead_katakana_level_11.show_game_over_katakana()

        # Symbol WO
        special_hit_enemy_list_WO = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_WO, True)
        for special_eaten_WO in special_hit_enemy_list_WO:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_WO == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_11.show_game_over_katakana()

        # Vocal Single N
        special_hit_enemy_list_N = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_N, True)
        for special_eaten_N in special_hit_enemy_list_N:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_N == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_11.show_game_over_katakana()


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
        you_die_in_hell_lv9 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv9, False)
        
        you_die_in_hell_lv10 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv10, False)
        
        you_die_in_hell_lv11 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv11, False)

        # effect from death sprite list
        for water_suicide_lv9 in you_die_in_hell_lv9:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_katakana_level_9.show_game_over_katakana()
        
        for lava_water_suicide_10 in you_die_in_hell_lv10:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_katakana_level_10.show_game_over_katakana()
        
        for lava_water_suicide_11 in you_die_in_hell_lv11:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_katakana_level_11.show_game_over_katakana()
        

        # for NPC purpose
        meet_himesama = pygame.sprite.spritecollide(
            self, self.level.himesama_list, False)
        for kiss_himesama in meet_himesama:
            endscreen.show_end_screen_hiragana()

        # FOR LEVEL 9 katakana Mode
        point1_katakana_lv9 = pygame.sprite.spritecollide(
            self, self.level.katakana_YA, True)
        point2_katakana_lv9 = pygame.sprite.spritecollide(
            self, self.level.katakana_YU, True)
        point3_katakana_lv9 = pygame.sprite.spritecollide(
            self, self.level.katakana_YO, True)

        # If user get point katakana YA
        for true_point_lv9 in point1_katakana_lv9:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_YA = True

        # If user get point katakana YU
        for true_point_lv9 in point2_katakana_lv9:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_YU = True

        # If user get point katakana YO
        for true_point_lv9 in point3_katakana_lv9:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_YO = True
        

        # For level 10 katakana Mode
        point1_katakana_lv10 = pygame.sprite.spritecollide(
            self, self.level.katakana_RA, True)
        point2_katakana_lv10 = pygame.sprite.spritecollide(
            self, self.level.katakana_RI, True)
        point3_katakana_lv10 = pygame.sprite.spritecollide(
            self, self.level.katakana_RU, True)
        point4_katakana_lv10 = pygame.sprite.spritecollide(
            self, self.level.katakana_RE, True)
        point5_katakana_lv10 = pygame.sprite.spritecollide(
            self, self.level.katakana_RO, True)

        # If user get point katakana RA
        for true_point_lv10 in point1_katakana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RA = True

        # If user get point katakana RI
        for true_point_lv10 in point2_katakana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RI = True

        # If user get point katakana RU
        for true_point_lv10 in point3_katakana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RU = True

        # If user get point katakana Re
        for true_point_lv10 in point4_katakana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RE = True

        # If user get point katakana RO
        for true_point_lv10 in point5_katakana_lv10:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_RO = True


        # For level 11 katakana Mode
        point1_katakana_lv11 = pygame.sprite.spritecollide(
            self, self.level.katakana_WA, True)
        point2_katakana_lv11 = pygame.sprite.spritecollide(
            self, self.level.katakana_WO, True)
        point3_katakana_lv11 = pygame.sprite.spritecollide(
            self, self.level.katakana_N, True)

        # If user get point katakana WA
        for true_point_lv11 in point1_katakana_lv11:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_WA = True

        # If user get point katakana WO
        for true_point_lv11 in point2_katakana_lv11:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_WO = True

        # If user get point katakana N
        for true_point_lv11 in point3_katakana_lv11:
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
        self.confirm_katakana = None

        # for special enemy
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
        hitting_enemy_lv9 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv9, True)
        hitting_enemy_lv10 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv10, True)
        hitting_enemy_lv11 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv11, True)
        
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
        # FOR LEVEL 9
        # Vocal Y
        for special_eaten_YA in hitting_special_enemy_YA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ya.play()

                if self.special_remove_YA == True:
                    self.confirm_katakana = True
                elif self.special_remove_YU \
                        or self.special_remove_YO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ya.play()

                if self.special_remove_YA == True:
                    self.confirm_katakana = True
                elif self.special_remove_YU \
                        or self.special_remove_YO == True:
                    self.confirm_katakana = False

        for special_eaten_YU in hitting_special_enemy_YU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yu.play()
                
                if self.special_remove_YU == True:
                    self.confirm_katakana = True
                elif self.special_remove_YA \
                        or self.special_remove_YO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yu.play()

                if self.special_remove_YU == True:
                    self.confirm_katakana = True
                elif self.special_remove_YA \
                        or self.special_remove_YO == True:
                    self.confirm_katakana = False

        for special_eaten_YO in hitting_special_enemy_YO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yo.play()

                if self.special_remove_YO == True:
                    self.confirm_katakana = True
                elif self.special_remove_YA \
                        or self.special_remove_YU == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_yo.play()

                if self.special_remove_YO == True:
                    self.confirm_katakana = True
                elif self.special_remove_YA \
                        or self.special_remove_YU == True:
                    self.confirm_katakana = False

        # FOR LEVEL 10
        # Vocal R
        for special_eaten_RA in hitting_special_enemy_RA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ra.play()

                if self.special_remove_RA == True:
                    self.confirm_katakana = True
                elif self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ra.play()

                if self.special_remove_RA == True:
                    self.confirm_katakana = True
                elif self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

        for special_eaten_RI in hitting_special_enemy_RI:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ri.play()

                if self.special_remove_RI == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ri.play()

                if self.special_remove_RI == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RU \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

        for special_eaten_RU in hitting_special_enemy_RU:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ru.play()

                if self.special_remove_RU == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ru.play()

                if self.special_remove_RU == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RE \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

        for special_eaten_RE in hitting_special_enemy_RE:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_re.play()

                if self.special_remove_RE == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_re.play()

                if self.special_remove_RE == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RO == True:
                    self.confirm_katakana = False

        for special_eaten_RO in hitting_special_enemy_RO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ro.play()

                if self.special_remove_RO == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_ro.play()

                if self.special_remove_RO == True:
                    self.confirm_katakana = True
                elif self.special_remove_RA \
                        or self.special_remove_RI \
                        or self.special_remove_RU \
                        or self.special_remove_RE == True:
                    self.confirm_katakana = False

        # FOR LEVEL 11
        # Vocal W
        for special_eaten_WA in hitting_special_enemy_WA:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wa.play()

                if self.special_remove_WA == True:
                    self.confirm_katakana = True
                elif self.special_remove_WO \
                        or self.special_remove_N == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wa.play()

                if self.special_remove_WA == True:
                    self.confirm_katakana = True
                elif self.special_remove_WO \
                        or self.special_remove_N == True:
                    self.confirm_katakana = False

        for special_eaten_WO in hitting_special_enemy_WO:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wo.play()

                if self.special_remove_WO == True:
                    self.confirm_katakana = True
                elif self.special_remove_WA \
                        or self.special_remove_N == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_wo.play()

                if self.special_remove_WO == True:
                    self.confirm_katakana = True
                elif self.special_remove_WA \
                        or self.special_remove_N == True:
                    self.confirm_katakana = False

        # Vocal N
        for special_eaten_N in hitting_special_enemy_N:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_n.play()

                if self.special_remove_N == True:
                    self.confirm_katakana = True
                elif self.special_remove_WA \
                        or self.special_remove_WO == True:
                    self.confirm_katakana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_n.play()

                if self.special_remove_N == True:
                    self.confirm_katakana = True
                elif self.special_remove_WA \
                        or self.special_remove_WO == True:
                    self.confirm_katakana = False

        # when hit platform the bullet is gone
        hitting_platform = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)

        for block in hitting_platform:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
