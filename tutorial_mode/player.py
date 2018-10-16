# name file : player.py
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
from game_screens import endscreen_tutorial
from hiragana_mode.overscreen_hiragana import dead_tutorial
# import sounds module
from game_settings import configsounds
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
        self.special_remove_A = None
        self.special_remove_U = None

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

        
        # For general enemy list
        # If player touched by enemys
        hit_by_enemy_list_tutorial = pygame.sprite.spritecollide(
            self, self.level.enemy_list_tutorial, True)

        for eaten_tutorial in hit_by_enemy_list_tutorial:
            self.health_number -= self.general_enemy_dmg
            configsounds.ouch_sfx.play()

            if self.health_number == 0 or self.health_number < 0:
                dead_tutorial.show_game_over_tutorial()

        # for special enemy list
        # If player touched by special enemys
        
        # FOR LEVEL TUTORIAL
        # Basic Vocal
        # Symbol A
        special_hit_enemy_list_A = pygame.sprite.spritecollide(
            self, self.level.special_enemy_list_A, True)
        for special_eaten_A in special_hit_enemy_list_A:

            self.health_number -= self.special_enemy_dmg
            configsounds.ouch_sfx.play()

            # if self.special_remove_A == False:
            if self.health_number == 0 or self.health_number < 0:
                dead_tutorial.show_game_over_tutorial()

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
        # for tutorial
        you_die_in_hell_tutorial = pygame.sprite.spritecollide(
            self, self.level.death_place_list_tutorial, False)

        # effect from death sprite list
        for water_suicide_intro in you_die_in_hell_tutorial:
            self.rect.y += 20
            if self.rect.bottom >= constants.SCREEN_HEIGHT \
                    or self.rect.bottom < 0:
                dead_tutorial.show_game_over_tutorial()
        
        # for NPC purpose
        meet_grandpa = pygame.sprite.spritecollide(
            self, self.level.grandpa_list, False)
        for talk_grandpa in meet_grandpa:
            endscreen_tutorial.show_end_screen_tutorial()



        # FOR LEVEL TUTORIAL
        point1_hiragana_lv1 = pygame.sprite.spritecollide(
            self, self.level.hiragana_A, True)
        point3_hiragana_lv1 = pygame.sprite.spritecollide(
            self, self.level.hiragana_U, True)

        # If user get point hiragana A
        for true_point_lv1 in point1_hiragana_lv1:
            configsounds.coin_sfx.play()
            configsounds.coin_sfx.set_volume(0.5)
            self.scores += 100
            self.special_remove_A = True

        # If user get point hiragana U
        for false_point_lv1 in point3_hiragana_lv1:
            configsounds.denied_sfx.play()
            self.scores -= 100
            self.health_number -= self.false_point_dmg
            self.special_remove_U = False

            if self.health_number == 0 or self.health_number < 0:
                dead_tutorial.show_game_over_tutorial()

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
        
        self.confirm_hiragana = None

        # for special enemy
        # Basic Vocal
        # FOR LEVEL 1
        self.special_remove_A = player.special_remove_A
        self.special_remove_U = player.special_remove_U

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
        hitting_enemy_tutorial = pygame.sprite.spritecollide(
            self, self.level.enemy_list_tutorial, True)

        for eaten_tutorial in hitting_enemy_tutorial:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.ouch_sfx.play()
        
        # just for special enemy list they are immune
        # if the player not get point mission enemy are immnune
        # if the player get point mission enemy are not immnune

        # FOR LEVEL TUTORIAL
        # for point mission symbol A
        if self.special_remove_A:
            hitting_special_enemy_A = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_A, True)
        elif not self.special_remove_A:
            hitting_special_enemy_A = pygame.sprite.spritecollide(
                self, self.level.special_enemy_list_A, False)

        # attack a special enemy
        # Basic Vocal

        # FOR LEVEL TUTORIAL
        for special_eaten_A in hitting_special_enemy_A:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_a.play()

                if self.special_remove_A == True:
                    self.confirm_hiragana = True
                elif self.special_remove_U == False:
                    self.confirm_hiragana = False

            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
                configsounds.effect_a.play()

                if self.special_remove_A == True:
                    self.confirm_hiragana = True
                elif self.special_remove_U == False:
                    self.confirm_hiragana = False

        # when hit platform the bullet is gone
        hitting_platform = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)

        for block in hitting_platform:
            if self.direction == "R":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
            elif self.direction == "L":
                pygame.sprite.spritecollide(self, self.bullet_list, True)
