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
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()



class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
 
    def __init__(self, sprite_sheet_data):
 
        super().__init__(sprite_sheet_data)
 
        self.change_x = 0
        self.change_y = 0
 
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
 
        self.level = None
        self.player = None
 
    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """
 
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
