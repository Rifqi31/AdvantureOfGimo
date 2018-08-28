# file name : fontsettings.py
# python version 3

import pygame

from game_settings import configfont, configscreen


class BasicSettings(object):
    """this is basic settings"""

    def text_objects(self, text, color, size):
        """Function for store variable size font"""

        # config text size small
        if size == "small":
            textSurface = configfont.smallfont.render(text, True, color)
        # config text size medium
        elif size == "medium":
            textSurface = configfont.medfont.render(text, True, color)
        # config text size large
        elif size == "large":
            textSurface = configfont.largefont.render(text, True, color)

        return textSurface, textSurface.get_rect()

    # function for render text in the intro level
    def msg_to_screen(self, msg, color, x_pos, y_pos, size="small"):
        """Function for render text to the screen """

        # for calling it self
        settings = BasicSettings()
        textSurf, textRect = settings.text_objects(msg, color, size)
        configscreen.screen.blit(textSurf, [x_pos, y_pos])

