# filename : configsounds.py
# python version 3

# import pygame module
import pygame

# intialize
pygame.init()

# load from file
# for music
main_menu_background_music = pygame.mixer.music.load("sounds/01_Invitation.ogg")

# for SFX
jump_sfx = pygame.mixer.Sound("sounds/jump_sfx.wav")
