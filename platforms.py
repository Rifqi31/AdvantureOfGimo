# name file : platforms.py
# python version 3

"""
Module for managing platforms.
"""

# import pygame module
import pygame
# import spritesheet_functions file
from spritesheet_functions import SpriteSheet 

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

# for grass tileset
GRASS_RIGHT 							= (0 , 0, 70, 70)
GRASS_LEFT 								= (146, 0, 70, 70)
GRASS_MIDDLE							= (73, 0, 70, 70)
GRASS_TOP_DOWN							= (219, 0, 70, 70)
GRASS_LEFT_RIGHT						= (292, 0, 70, 70)
GRASS_ROUNDED							= (365, 0, 70, 70)

# for mountain tileset
SNOW_MIDDLE 							= (0, 73, 70, 70)
SNOW_LEFT 								= (73, 73, 70, 70)
SNOW_RIGHT 								= (146, 73, 70, 70)
SNOW_TOP_DOWN 							= (219, 73, 70, 70)
SNOW_LEFT_RIGHT 						= (292, 73, 70, 70)
SNOW_ROUNDED 							= (365, 73, 70, 70)

# for lava tileset
LAVA 									= (0, 146, 70, 70)
LAVA_LITTLE_ROCK 						= (73, 146, 70, 70)
LAVA_BLACK_GRASS_LITTLE_ROCK 			= (146, 146, 70, 70)
LAVA_BLACK_GRASS_LARGE_ROCK 			= (219, 146, 70, 70)
LAVA_LIQUIED 							= (292, 146, 70, 70)
LAVA_GREY_GRASS_LARGE_ROCK 				= (365, 146, 70, 70)


# for sand tileset
SAND_GRASS_MIDDLE 						= (0, 219, 70, 70)
SAND_GRASS_LEFT 						= (73, 219, 70, 70)
SAND_GRASS_RIGHT 						= (146, 219, 70, 70)
SAND_GRASS_TOP_DOWN 					= (219, 219, 70, 70)


# for bricks grass snowed
BRICKS_SNOW_LEFT 						= (292, 292, 70, 70)
BRICKS_SNOW_RIGHT 						= (365, 292, 70, 70)
BRICKS_SNOW_MIDDLE 						= (0, 292, 70, 70)
BRICKS_SNOW_TOP_DOWN 					= (73, 292, 70, 70)
BRICKS_SNOW_LEFT_RIGHT 					= (219, 292, 70, 70)
BRICKS_ROUNDED 							= (146, 292, 70, 70)

# for bricks grass
BRICKS_GRASS_LEFT 						= (73, 365, 70, 70)
BRICKS_GRASS_RIGHT 						= (146, 365, 70, 70)
BRICKS_GRASS_MIDDLE 					= (0, 365, 70, 70)
BRICKS_GRASS_TOP_DOWN 					= (219, 365, 70, 70)
BRICKS_GRASS_LEFT_RIGHT 				= (292, 365, 70, 70)
BRICKS_GRASS_ROUNDED 					= (365, 365, 70, 70)

# for ancient tomb tileset
ANCIENT_SAND_GRASS_LEFT 				= (73, 438, 70, 70)
ANCIENT_SAND_GRASS_RIGHT 				= (146, 438, 70, 70)
ANCIENT_SAND_GRASS_MIDDLE 				= (0, 438, 70, 70)
ANCIENT_SAND_GRASS_TOP_DOWN 			= (219, 438, 70, 70)
ANCIENT_SAND_GRASS_LEFT_RIGHT 			= (292, 438, 70, 70)
ANCIENT_SAND_GRASS_ROUNDED 				= (365, 438, 70, 70)

# for tileset darkland
DARKLAND_GRASS_LEFT 					= (73, 511, 70, 70)
DARKLAND_GRASS_RIGHT 					= (146, 511, 70, 70)
DARKLAND_GRASS_MIDDLE 					= (0, 511, 70, 70)
DARKLAND_BRIKCS_GRASS_LEFT 				= (292, 511, 70, 70)
DARKLAND_BRICKS_GRASS_RIGHT 			= (365, 511, 70, 70)
DARKLADN_BRICKS_GRASS_MIDDLE 			= (219, 511, 70, 70)
DARKLAND_BRICKS_GRASS_TOP_DOWN 			= (0, 657, 70, 70)
DARKLAND_BRICKS_GRASS_LEFT_RIGHT 		= (0, 584, 70, 70)
DARKLAND_BRICKS_GRASS_ROUNDED 			= (73, 584, 70, 70)

# for general un grassed tileset
DIRT 									= (219, 584, 70, 70)
ROCK 									= (292, 584, 70, 70) 
SAND 									= (292, 219, 70, 70)
BRICKS 									= (365, 219, 70, 70)
DARKLAND_BRICKS 						= (146, 584, 70, 70)
ANCIENT 								= (365, 584, 70, 70)
BLOCK 									= (73, 657, 70, 70)




class Platform(pygame.sprite.Sprite):
	""" Platform the user can jump on """

	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """

        super().__init__()

        sprite_sheet = SpriteSheet("tiles_asset.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[1],
        									sprite_sheet_data[2],
        									sprite_sheet_data[3],
        									sprite_sheet_data[4])

        self.rect = self.image.get_rect()
