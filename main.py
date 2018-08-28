# file name : main.py
# python version 3

# import pygame module
import pygame
# import main menu screen
from game_screens import mainmenu

pygame.init()

# set icon game
icon = pygame.image.load("spritesheet/gimo.png")
pygame.display.set_icon(icon)

mainmenu.main_menu()
