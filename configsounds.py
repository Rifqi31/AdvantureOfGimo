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
coin_sfx = pygame.mixer.Sound("sounds/mattix_8bit-coin.wav")
magic_sfx = pygame.mixer.Sound("sounds/8bit-laser-shot.wav")
ouch_sfx = pygame.mixer.Sound("sounds/ouch_sfx.wav")
portal_sfx = pygame.mixer.Sound("sounds/retro-accomplished-sfx.wav")


# ----- For Sounds Settings -----
def turn_off_sounds():
	""" This function for turn off all sounds """
	pygame.mixer.stop()

def turn_on_sounds():
	""" This function for turn on all sounds """
	background_music.play(-1)
	background_music.set_volume(0.5)
