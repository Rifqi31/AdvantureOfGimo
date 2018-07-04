# filename : configsounds.py
# python version 3

# import pygame module
import pygame

# intialize
pygame.init()

# for music
background_music = pygame.mixer.Sound("sounds/01_Invitation.ogg")

# for SFX
menu_sfx = pygame.mixer.Sound("sounds/menu_sfx.wav")
push_button_sfx = pygame.mixer.Sound("sounds/push_button_sfx.wav")
jump_sfx = pygame.mixer.Sound("sounds/jump_sfx.wav")
game_over_sfx = pygame.mixer.Sound("sounds/game_over_sfx.wav")
