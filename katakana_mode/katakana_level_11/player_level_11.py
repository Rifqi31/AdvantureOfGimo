# name file : player_level_11.py
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
    dead_katakana_level_11
)
# import sounds module
from game_settings import configsounds
# import moving platform modules
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
            
            if isinstance(block, MovingPlatform_lava_rock):
                self.rect.x += block.change_x

        # For general enemy list
        # If player touched by enemys
        hit_by_enemy_list_lv11 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv11, True)

        for eaten_lv11 in hit_by_enemy_list_lv11:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_katakana_level_11.show_game_over_katakana()


        # for special enemy list
        # If player touched by special enemys

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
        you_die_in_hell_lv11 = pygame.sprite.spritecollide(
            self, self.level.death_place_list_lv11, False)

        # effect from death sprite list
        for lava_water_suicide_11 in you_die_in_hell_lv11:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_katakana_level_11.show_game_over_katakana()
        

        # for NPC purpose
        meet_himesama = pygame.sprite.spritecollide(
            self, self.level.himesama_list, False)
        for kiss_himesama in meet_himesama:
            endscreen.show_end_screen_katakana()

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
        hitting_enemy_lv11 = pygame.sprite.spritecollide(
            self, self.level.enemy_list_lv11, True)

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
