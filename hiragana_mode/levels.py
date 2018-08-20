# name file: levels.py
# python version 3

# import pygame module
import pygame
# import constants variable
import constants
# import hiragana mode platforms
from hiragana_mode import platforms


class Level():

    def __init__(self, player):

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None
        self.portal_list = None
        self.death_place_list = None
        self.love_restore_health = None

        # this list for static picture in level Tutorial
        self.health_icon_list = None
        self.special_enemy_icon_list = None
        self.general_enemy_icon_list = None

        self.grandpa_list = None
        self.himesama_list = None

        # for special_enemys
        # basic vocal
        self.special_enemy_list_A = None
        self.special_enemy_list_I = None
        self.special_enemy_list_U = None
        self.special_enemy_list_E = None
        self.special_enemy_list_O = None

        # Vocal K
        self.special_enemy_list_KA = None
        self.special_enemy_list_KI = None
        self.special_enemy_list_KU = None
        self.special_enemy_list_KE = None
        self.special_enemy_list_KO = None

        # Vocal S
        self.special_enemy_list_SA = None
        self.special_enemy_list_SI = None
        self.special_enemy_list_SU = None
        self.special_enemy_list_SE = None
        self.special_enemy_list_SO = None

        # Vocal T
        self.special_enemy_list_TA = None
        self.special_enemy_list_TI = None
        self.special_enemy_list_TU = None
        self.special_enemy_list_TE = None
        self.special_enemy_list_TO = None

        # Vocal N
        self.special_enemy_list_NA = None
        self.special_enemy_list_NI = None
        self.special_enemy_list_NU = None
        self.special_enemy_list_NE = None
        self.special_enemy_list_NO = None

        # Vocal H
        self.special_enemy_list_HA = None
        self.special_enemy_list_HI = None
        self.special_enemy_list_HU = None
        self.special_enemy_list_HE = None
        self.special_enemy_list_HO = None

        # Vocal M
        self.special_enemy_list_MA = None
        self.special_enemy_list_MI = None
        self.special_enemy_list_MU = None
        self.special_enemy_list_ME = None
        self.special_enemy_list_MO = None

        # Vocal Y
        self.special_enemy_list_YA = None
        self.special_enemy_list_YU = None
        self.special_enemy_list_YO = None

        # Vocal R
        self.special_enemy_list_RA = None
        self.special_enemy_list_RI = None
        self.special_enemy_list_RU = None
        self.special_enemy_list_RE = None
        self.special_enemy_list_RO = None

        # Vocal W
        self.special_enemy_list_WA = None
        self.special_enemy_list_WO = None

        # Vocal N
        self.special_enemy_list_N = None

        # sprite content for hiragana and katakana
        # basic vocal
        self.hiragana_A = None
        self.hiragana_I = None
        self.hiragana_U = None

        self.hiragana_E = None
        self.hiragana_O = None

        # Vocal K
        self.hiragana_KA = None
        self.hiragana_KI = None
        self.hiragana_KU = None
        self.hiragana_KE = None
        self.hiragana_KO = None

        # Vocal S
        self.hiragana_SA = None
        self.hiragana_SI = None
        self.hiragana_SU = None
        self.hiragana_SE = None
        self.hiragana_SO = None

        # Vocal T
        self.hiragana_TA = None
        self.hiragana_TI = None
        self.hiragana_TU = None
        self.hiragana_TE = None
        self.hiragana_TO = None

        # Vocal N
        self.hiragana_NA = None
        self.hiragana_NI = None
        self.hiragana_NU = None
        self.hiragana_NE = None
        self.hiragana_NO = None

        # Vocal H
        self.hiragana_HA = None
        self.hiragana_HI = None
        self.hiragana_HU = None
        self.hiragana_HE = None
        self.hiragana_HO = None

        # Vocal M
        self.hiragana_MA = None
        self.hiragana_MI = None
        self.hiragana_MU = None
        self.hiragana_ME = None
        self.hiragana_MO = None

        # Vocal Y
        self.hiragana_YA = None
        self.hiragana_YU = None
        self.hiragana_YO = None

        # Vocal R
        self.hiragana_RA = None
        self.hiragana_RI = None
        self.hiragana_RU = None
        self.hiragana_RE = None
        self.hiragana_RO = None

        # Vocal W
        self.hiragana_WA = None
        self.hiragana_WO = None

        self.katakana_WA = None
        self.katakana_WO = None

        # Vocal N
        self.hiragana_N = None

        # for fix bug point
        # prototype
        self.special_enemy_list_A_lv2 = None
        self.special_enemy_list_I_lv2 = None
        self.special_enemy_list_U_lv2 = None

        self.hiragana_A_lv2 = None
        self.hiragana_I_lv2 = None
        self.hiragana_U_lv2 = None

        self.hiragana_KA_lv3 = None
        self.hiragana_KI_lv3 = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.portal_list = pygame.sprite.Group()
        self.death_place_list = pygame.sprite.Group()
        self.love_restore_health = pygame.sprite.Group()

        # for tutorial purpose
        self.health_icon_list = pygame.sprite.Group()
        self.special_enemy_icon_list = pygame.sprite.Group()
        self.general_enemy_icon_list = pygame.sprite.Group()
        self.grandpa_list = pygame.sprite.Group()
        self.himesama_list = pygame.sprite.Group()

        # for special enemys
        # Basic Vocal
        self.special_enemy_list_A = pygame.sprite.Group()
        self.special_enemy_list_I = pygame.sprite.Group()
        self.special_enemy_list_U = pygame.sprite.Group()
        self.special_enemy_list_E = pygame.sprite.Group()
        self.special_enemy_list_O = pygame.sprite.Group()

        # Vocal K
        self.special_enemy_list_KA = pygame.sprite.Group()
        self.special_enemy_list_KI = pygame.sprite.Group()
        self.special_enemy_list_KU = pygame.sprite.Group()
        self.special_enemy_list_KE = pygame.sprite.Group()
        self.special_enemy_list_KO = pygame.sprite.Group()

        # Vocal S
        self.special_enemy_list_SA = pygame.sprite.Group()
        self.special_enemy_list_SI = pygame.sprite.Group()
        self.special_enemy_list_SU = pygame.sprite.Group()
        self.special_enemy_list_SE = pygame.sprite.Group()
        self.special_enemy_list_SO = pygame.sprite.Group()

        # Vocal T
        self.special_enemy_list_TA = pygame.sprite.Group()
        self.special_enemy_list_TI = pygame.sprite.Group()
        self.special_enemy_list_TU = pygame.sprite.Group()
        self.special_enemy_list_TE = pygame.sprite.Group()
        self.special_enemy_list_TO = pygame.sprite.Group()

        # Vocal N
        self.special_enemy_list_NA = pygame.sprite.Group()
        self.special_enemy_list_NI = pygame.sprite.Group()
        self.special_enemy_list_NU = pygame.sprite.Group()
        self.special_enemy_list_NE = pygame.sprite.Group()
        self.special_enemy_list_NO = pygame.sprite.Group()

        # Vocal H
        self.special_enemy_list_HA = pygame.sprite.Group()
        self.special_enemy_list_HI = pygame.sprite.Group()
        self.special_enemy_list_HU = pygame.sprite.Group()
        self.special_enemy_list_HE = pygame.sprite.Group()
        self.special_enemy_list_HO = pygame.sprite.Group()

        # Vocal M
        self.special_enemy_list_MA = pygame.sprite.Group()
        self.special_enemy_list_MI = pygame.sprite.Group()
        self.special_enemy_list_MU = pygame.sprite.Group()
        self.special_enemy_list_ME = pygame.sprite.Group()
        self.special_enemy_list_MO = pygame.sprite.Group()

        # Vocal Y
        self.special_enemy_list_YA = pygame.sprite.Group()
        self.special_enemy_list_YU = pygame.sprite.Group()
        self.special_enemy_list_YO = pygame.sprite.Group()

        # Vocal R
        self.special_enemy_list_RA = pygame.sprite.Group()
        self.special_enemy_list_RI = pygame.sprite.Group()
        self.special_enemy_list_RU = pygame.sprite.Group()
        self.special_enemy_list_RE = pygame.sprite.Group()
        self.special_enemy_list_RO = pygame.sprite.Group()

        # Vocal W
        self.special_enemy_list_WA = pygame.sprite.Group()
        self.special_enemy_list_WO = pygame.sprite.Group()

        # Vocal N
        self.special_enemy_list_N = pygame.sprite.Group()

        # group sprite for hiragana and katakana
        # Basic Vokal
        self.hiragana_A = pygame.sprite.Group()
        self.hiragana_I = pygame.sprite.Group()
        self.hiragana_U = pygame.sprite.Group()
        self.hiragana_E = pygame.sprite.Group()
        self.hiragana_O = pygame.sprite.Group()

        # Vocal K
        self.hiragana_KA = pygame.sprite.Group()
        self.hiragana_KI = pygame.sprite.Group()
        self.hiragana_KU = pygame.sprite.Group()
        self.hiragana_KE = pygame.sprite.Group()
        self.hiragana_KO = pygame.sprite.Group()

        # Vocal S
        self.hiragana_SA = pygame.sprite.Group()
        self.hiragana_SI = pygame.sprite.Group()
        self.hiragana_SU = pygame.sprite.Group()
        self.hiragana_SE = pygame.sprite.Group()
        self.hiragana_SO = pygame.sprite.Group()

        # Vocal T
        self.hiragana_TA = pygame.sprite.Group()
        self.hiragana_TI = pygame.sprite.Group()
        self.hiragana_TU = pygame.sprite.Group()
        self.hiragana_TE = pygame.sprite.Group()
        self.hiragana_TO = pygame.sprite.Group()

        # Vocal N
        self.hiragana_NA = pygame.sprite.Group()
        self.hiragana_NI = pygame.sprite.Group()
        self.hiragana_NU = pygame.sprite.Group()
        self.hiragana_NE = pygame.sprite.Group()
        self.hiragana_NO = pygame.sprite.Group()

        # Vocal H
        self.hiragana_HA = pygame.sprite.Group()
        self.hiragana_HI = pygame.sprite.Group()
        self.hiragana_HU = pygame.sprite.Group()
        self.hiragana_HE = pygame.sprite.Group()
        self.hiragana_HO = pygame.sprite.Group()

        # Vocal M
        self.hiragana_MA = pygame.sprite.Group()
        self.hiragana_MI = pygame.sprite.Group()
        self.hiragana_MU = pygame.sprite.Group()
        self.hiragana_ME = pygame.sprite.Group()
        self.hiragana_MO = pygame.sprite.Group()

        # Vocal Y
        self.hiragana_YA = pygame.sprite.Group()
        self.hiragana_YU = pygame.sprite.Group()
        self.hiragana_YO = pygame.sprite.Group()

        # Vocal R
        self.hiragana_RA = pygame.sprite.Group()
        self.hiragana_RI = pygame.sprite.Group()
        self.hiragana_RU = pygame.sprite.Group()
        self.hiragana_RE = pygame.sprite.Group()
        self.hiragana_RO = pygame.sprite.Group()

        # Vocal W
        self.hiragana_WA = pygame.sprite.Group()
        self.hiragana_WO = pygame.sprite.Group()

        # Vocal N
        self.hiragana_N = pygame.sprite.Group()

        # for fix bug
        self.special_enemy_list_A_lv2 = pygame.sprite.Group()
        self.special_enemy_list_I_lv2 = pygame.sprite.Group()
        self.special_enemy_list_U_lv2 = pygame.sprite.Group()

        self.hiragana_A_lv2 = pygame.sprite.Group()
        self.hiragana_I_lv2 = pygame.sprite.Group()
        self.hiragana_U_lv2 = pygame.sprite.Group()

        self.hiragana_KA_lv3 = pygame.sprite.Group()
        self.hiragana_KI_lv3 = pygame.sprite.Group()

        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.portal_list.update()
        self.death_place_list.update()
        self.enemy_list.update()
        self.love_restore_health.update()

        # for tutorial level
        self.health_icon_list.update()
        self.special_enemy_icon_list.update()
        self.general_enemy_icon_list.update()
        self.grandpa_list.update()
        self.himesama_list.update()

        # for special enemys
        # Basic Vocal
        self.special_enemy_list_A.update()
        self.special_enemy_list_I.update()
        self.special_enemy_list_U.update()
        self.special_enemy_list_E.update()
        self.special_enemy_list_O.update()

        # Vocal K
        self.special_enemy_list_KA.update()
        self.special_enemy_list_KI.update()
        self.special_enemy_list_KU.update()
        self.special_enemy_list_KE.update()
        self.special_enemy_list_KO.update()

        # Vocal S
        self.special_enemy_list_SA.update()
        self.special_enemy_list_SI.update()
        self.special_enemy_list_SU.update()
        self.special_enemy_list_SE.update()
        self.special_enemy_list_SO.update()

        # Vocal T
        self.special_enemy_list_TA.update()
        self.special_enemy_list_TI.update()
        self.special_enemy_list_TU.update()
        self.special_enemy_list_TE.update()
        self.special_enemy_list_TO.update()

        # Vocal N
        self.special_enemy_list_NA.update()
        self.special_enemy_list_NI.update()
        self.special_enemy_list_NU.update()
        self.special_enemy_list_NE.update()
        self.special_enemy_list_NO.update()

        # Vocal H
        self.special_enemy_list_HA.update()
        self.special_enemy_list_HI.update()
        self.special_enemy_list_HU.update()
        self.special_enemy_list_HE.update()
        self.special_enemy_list_HO.update()

        # Vocal M
        self.special_enemy_list_MA.update()
        self.special_enemy_list_MI.update()
        self.special_enemy_list_MU.update()
        self.special_enemy_list_ME.update()
        self.special_enemy_list_MO.update()

        # Vocal Y
        self.special_enemy_list_YA.update()
        self.special_enemy_list_YU.update()
        self.special_enemy_list_YO.update()

        # Vocal R
        self.special_enemy_list_RA.update()
        self.special_enemy_list_RI.update()
        self.special_enemy_list_RU.update()
        self.special_enemy_list_RE.update()
        self.special_enemy_list_RO.update()

        # Vocal W
        self.special_enemy_list_WA.update()
        self.special_enemy_list_WO.update()

        # Vocal N
        self.special_enemy_list_N.update()

        # for update sprites hiragana and katakana
        # Basic Vocal
        self.hiragana_A.update()
        self.hiragana_I.update()
        self.hiragana_U.update()
        self.hiragana_E.update()
        self.hiragana_O.update()

        # Vocal K
        self.hiragana_KA.update()
        self.hiragana_KI.update()
        self.hiragana_KU.update()
        self.hiragana_KE.update()
        self.hiragana_KO.update()

        # Vocal S
        self.hiragana_SA.update()
        self.hiragana_SI.update()
        self.hiragana_SU.update()
        self.hiragana_SE.update()
        self.hiragana_SO.update()

        # Vocal T
        self.hiragana_TA.update()
        self.hiragana_TI.update()
        self.hiragana_TU.update()
        self.hiragana_TE.update()
        self.hiragana_TO.update()

        # Vocal N
        self.hiragana_NA.update()
        self.hiragana_NI.update()
        self.hiragana_NU.update()
        self.hiragana_NE.update()
        self.hiragana_NO.update()

        # Vocal H
        self.hiragana_HA.update()
        self.hiragana_HI.update()
        self.hiragana_HU.update()
        self.hiragana_HE.update()
        self.hiragana_HO.update()

        # Vocal M
        self.hiragana_MA.update()
        self.hiragana_MI.update()
        self.hiragana_MU.update()
        self.hiragana_ME.update()
        self.hiragana_MO.update()

        # Vocal Y
        self.hiragana_YA.update()
        self.hiragana_YU.update()
        self.hiragana_YO.update()

        # Vocal R
        self.hiragana_RA.update()
        self.hiragana_RI.update()
        self.hiragana_RU.update()
        self.hiragana_RE.update()
        self.hiragana_RO.update()

        # Vocal W
        self.hiragana_WA.update()
        self.hiragana_WO.update()

        # Vocal N
        self.hiragana_N.update()

        # for fix bug point
        self.special_enemy_list_A.update()
        self.special_enemy_list_I.update()
        self.special_enemy_list_U.update()

        self.hiragana_A_lv2.update()
        self.hiragana_I_lv2.update()
        self.hiragana_U_lv2.update()

        self.hiragana_KA_lv3.update()
        self.hiragana_KI_lv3.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.portal_list.draw(screen)
        self.death_place_list.draw(screen)
        self.enemy_list.draw(screen)
        self.love_restore_health.draw(screen)

        # for tutorial level
        self.health_icon_list.draw(screen)
        self.special_enemy_icon_list.draw(screen)
        self.general_enemy_icon_list.draw(screen)
        self.grandpa_list.draw(screen)
        self.himesama_list.draw(screen)

        # For special enemy
        # Basic Vocal
        self.special_enemy_list_A.draw(screen)
        self.special_enemy_list_I.draw(screen)
        self.special_enemy_list_U.draw(screen)
        self.special_enemy_list_E.draw(screen)
        self.special_enemy_list_O.draw(screen)

        # Vocal K
        self.special_enemy_list_KA.draw(screen)
        self.special_enemy_list_KI.draw(screen)
        self.special_enemy_list_KU.draw(screen)
        self.special_enemy_list_KE.draw(screen)
        self.special_enemy_list_KO.draw(screen)

        # Vocal S
        self.special_enemy_list_SA.draw(screen)
        self.special_enemy_list_SI.draw(screen)
        self.special_enemy_list_SU.draw(screen)
        self.special_enemy_list_SE.draw(screen)
        self.special_enemy_list_SO.draw(screen)

        # Vocal T
        self.special_enemy_list_TA.draw(screen)
        self.special_enemy_list_TI.draw(screen)
        self.special_enemy_list_TU.draw(screen)
        self.special_enemy_list_TE.draw(screen)
        self.special_enemy_list_TO.draw(screen)

        # Vocal N
        self.special_enemy_list_NA.draw(screen)
        self.special_enemy_list_NI.draw(screen)
        self.special_enemy_list_NU.draw(screen)
        self.special_enemy_list_NE.draw(screen)
        self.special_enemy_list_NO.draw(screen)

        # Vocal H
        self.special_enemy_list_HA.draw(screen)
        self.special_enemy_list_HI.draw(screen)
        self.special_enemy_list_HU.draw(screen)
        self.special_enemy_list_HE.draw(screen)
        self.special_enemy_list_HO.draw(screen)

        # Vocal M
        self.special_enemy_list_MA.draw(screen)
        self.special_enemy_list_MI.draw(screen)
        self.special_enemy_list_MU.draw(screen)
        self.special_enemy_list_ME.draw(screen)
        self.special_enemy_list_MO.draw(screen)

        # Vocal Y
        self.special_enemy_list_YA.draw(screen)
        self.special_enemy_list_YU.draw(screen)
        self.special_enemy_list_YO.draw(screen)

        # Vocal R
        self.special_enemy_list_RA.draw(screen)
        self.special_enemy_list_RI.draw(screen)
        self.special_enemy_list_RU.draw(screen)
        self.special_enemy_list_RE.draw(screen)
        self.special_enemy_list_RO.draw(screen)

        # Vocal W
        self.special_enemy_list_WA.draw(screen)
        self.special_enemy_list_WO.draw(screen)

        # Vocal N
        self.special_enemy_list_N.draw(screen)

        # for hiragana and katakana sprites
        # Basic Vocal
        self.hiragana_A.draw(screen)
        self.hiragana_I.draw(screen)
        self.hiragana_U.draw(screen)
        self.hiragana_E.draw(screen)
        self.hiragana_O.draw(screen)

        # Vocal K
        self.hiragana_KA.draw(screen)
        self.hiragana_KI.draw(screen)
        self.hiragana_KU.draw(screen)
        self.hiragana_KE.draw(screen)
        self.hiragana_KO.draw(screen)

        # Vocal S
        self.hiragana_SA.draw(screen)
        self.hiragana_SI.draw(screen)
        self.hiragana_SU.draw(screen)
        self.hiragana_SE.draw(screen)
        self.hiragana_SO.draw(screen)

        # Vocal T
        self.hiragana_TA.draw(screen)
        self.hiragana_TI.draw(screen)
        self.hiragana_TU.draw(screen)
        self.hiragana_TE.draw(screen)
        self.hiragana_TO.draw(screen)

        # Vocal N
        self.hiragana_NA.draw(screen)
        self.hiragana_NI.draw(screen)
        self.hiragana_NU.draw(screen)
        self.hiragana_NE.draw(screen)
        self.hiragana_NO.draw(screen)

        # Vocal H
        self.hiragana_HA.draw(screen)
        self.hiragana_HI.draw(screen)
        self.hiragana_HU.draw(screen)
        self.hiragana_HE.draw(screen)
        self.hiragana_HO.draw(screen)

        # Vocal M
        self.hiragana_MA.draw(screen)
        self.hiragana_MI.draw(screen)
        self.hiragana_MU.draw(screen)
        self.hiragana_ME.draw(screen)
        self.hiragana_MO.draw(screen)

        # Vocal Y
        self.hiragana_YA.draw(screen)
        self.hiragana_YU.draw(screen)
        self.hiragana_YO.draw(screen)

        # Vocal R
        self.hiragana_RA.draw(screen)
        self.hiragana_RI.draw(screen)
        self.hiragana_RU.draw(screen)
        self.hiragana_RE.draw(screen)
        self.hiragana_RO.draw(screen)

        # Vocal W
        self.hiragana_WA.draw(screen)
        self.hiragana_WO.draw(screen)

        # Vocal N
        self.hiragana_N.draw(screen)

        # for fix bug point
        self.special_enemy_list_A_lv2.draw(screen)
        self.special_enemy_list_I_lv2.draw(screen)
        self.special_enemy_list_U_lv2.draw(screen)

        self.hiragana_A_lv2.draw(screen)
        self.hiragana_I_lv2.draw(screen)
        self.hiragana_U_lv2.draw(screen)

        self.hiragana_KA_lv3.draw(screen)
        self.hiragana_KI_lv3.draw(screen)

    def shift_world(self, shift_x):
        """
        When the user moves left/right
        and we need to scroll everything:
        """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.portal_list:
            platform.rect.x += shift_x

        for platform in self.death_place_list:
            platform.rect.x += shift_x

        for platform in self.love_restore_health:
            platform.rect.x += shift_x

        # for hiragana and katakana sprites
        # Basic Vocal
        for platform in self.hiragana_A:
            platform.rect.x += shift_x

        for platform in self.hiragana_I:
            platform.rect.x += shift_x

        for platform in self.hiragana_U:
            platform.rect.x += shift_x

        for platform in self.hiragana_E:
            platform.rect.x += shift_x

        for platform in self.hiragana_O:
            platform.rect.x += shift_x

        #####################################

        # Vocal K
        for platform in self.hiragana_KA:
            platform.rect.x += shift_x

        for platform in self.hiragana_KI:
            platform.rect.x += shift_x

        for platform in self.hiragana_KU:
            platform.rect.x += shift_x

        for platform in self.hiragana_KE:
            platform.rect.x += shift_x

        for platform in self.hiragana_KO:
            platform.rect.x += shift_x

        #####################################

        # Vocal S
        for platform in self.hiragana_SA:
            platform.rect.x += shift_x

        for platform in self.hiragana_SI:
            platform.rect.x += shift_x

        for platform in self.hiragana_SU:
            platform.rect.x += shift_x

        for platform in self.hiragana_SE:
            platform.rect.x += shift_x

        for platform in self.hiragana_SO:
            platform.rect.x += shift_x

        #####################################

        # Vocal T
        for platform in self.hiragana_TA:
            platform.rect.x += shift_x

        for platform in self.hiragana_TI:
            platform.rect.x += shift_x

        for platform in self.hiragana_TU:
            platform.rect.x += shift_x

        for platform in self.hiragana_TE:
            platform.rect.x += shift_x

        for platform in self.hiragana_TO:
            platform.rect.x += shift_x

        #####################################

        # Vocal N
        for platform in self.hiragana_NA:
            platform.rect.x += shift_x

        for platform in self.hiragana_NI:
            platform.rect.x += shift_x

        for platform in self.hiragana_NU:
            platform.rect.x += shift_x

        for platform in self.hiragana_NE:
            platform.rect.x += shift_x

        for platform in self.hiragana_NO:
            platform.rect.x += shift_x

        #####################################

        # Vocal H
        for platform in self.hiragana_HA:
            platform.rect.x += shift_x

        for platform in self.hiragana_HI:
            platform.rect.x += shift_x

        for platform in self.hiragana_HU:
            platform.rect.x += shift_x

        for platform in self.hiragana_HE:
            platform.rect.x += shift_x

        for platform in self.hiragana_HO:
            platform.rect.x += shift_x

        #####################################

        # Vocal M
        for platform in self.hiragana_MA:
            platform.rect.x += shift_x

        for platform in self.hiragana_MI:
            platform.rect.x += shift_x

        for platform in self.hiragana_MU:
            platform.rect.x += shift_x

        for platform in self.hiragana_ME:
            platform.rect.x += shift_x

        for platform in self.hiragana_MO:
            platform.rect.x += shift_x

        #####################################

        # Vocal Y
        for platform in self.hiragana_YA:
            platform.rect.x += shift_x

        for platform in self.hiragana_YU:
            platform.rect.x += shift_x

        for platform in self.hiragana_YO:
            platform.rect.x += shift_x

        #####################################

        # Vocal R
        for platform in self.hiragana_RA:
            platform.rect.x += shift_x

        for platform in self.hiragana_RI:
            platform.rect.x += shift_x

        for platform in self.hiragana_RU:
            platform.rect.x += shift_x

        for platform in self.hiragana_RE:
            platform.rect.x += shift_x

        for platform in self.hiragana_RO:
            platform.rect.x += shift_x

        #####################################

        # Vocal W
        for platform in self.hiragana_WA:
            platform.rect.x += shift_x

        for platform in self.hiragana_WO:
            platform.rect.x += shift_x

        #####################################

        # Vocal N
        for platform in self.hiragana_N:
            platform.rect.x += shift_x

        #####################################

        # for fix bug point
        for platform in self.special_enemy_list_A_lv2:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_I_lv2:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_U_lv2:
            platform.rect.x += shift_x

        for platform in self.hiragana_A_lv2:
            platform.rect.x += shift_x

        for platform in self.hiragana_I_lv2:
            platform.rect.x += shift_x

        for platform in self.hiragana_U_lv2:
            platform.rect.x += shift_x

        for platform in self.hiragana_KA_lv3:
            platform.rect.x += shift_x

        for platform in self.hiragana_KI_lv3:
            platform.rect.x += shift_x

        for platform in self.enemy_list:
            platform.rect.x += shift_x

        # For special enemys
        # Basic Vocal
        for platform in self.special_enemy_list_A:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_I:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_U:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_E:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_O:
            platform.rect.x += shift_x

        # Vocal K
        for platform in self.special_enemy_list_KA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_KI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_KU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_KE:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_KO:
            platform.rect.x += shift_x

        # Vocal S
        for platform in self.special_enemy_list_SA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_SI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_SU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_SE:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_SO:
            platform.rect.x += shift_x

        # Vocal T
        for platform in self.special_enemy_list_TA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_TI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_TU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_TE:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_TO:
            platform.rect.x += shift_x

        # Vocal N
        for platform in self.special_enemy_list_NA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_NI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_NU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_NE:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_NO:
            platform.rect.x += shift_x

        # Vocal H
        for platform in self.special_enemy_list_HA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_HI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_HU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_HE:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_HO:
            platform.rect.x += shift_x

        # Vocal M
        for platform in self.special_enemy_list_MA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_MI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_MU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_ME:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_MO:
            platform.rect.x += shift_x

        # Vocal Y
        for platform in self.special_enemy_list_YA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_YU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_YO:
            platform.rect.x += shift_x

        # Vocal R
        for platform in self.special_enemy_list_RA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_RI:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_RU:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_RE:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_RO:
            platform.rect.x += shift_x

        # Vocal W
        for platform in self.special_enemy_list_WA:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_WO:
            platform.rect.x += shift_x

        # Vocal N
        for platform in self.special_enemy_list_N:
            platform.rect.x += shift_x

        # for NPC
        for platform in self.grandpa_list:
            platform.rect.x += shift_x

        for platform in self.himesama_list:
            platform.rect.x += shift_x


# Create platforms for intro game
# for intro how to play the game
class Level_Tutorial(Level):
    """ This class for introduce the player """

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms.snow_dirt_wall, -140, 0],
                 [platforms.snow_dirt_intro, 0, 460],
                 [platforms.snow_dirt_big_wall, 769, 0]]

        portal = [[platforms.portal_snow, 700, 380]]

        for platform in intro:
            block = platforms.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)


class Level_Tutorial_Gameplay(Level):
    """ This class for introduce the player
            for how to play the game"""

    def __init__(self, player):
        """ Create intro how to play """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms.snow_dirt_wall, -140, 0],
                 [platforms.snow_dirt_intro, 0, 460],
                 [platforms.snow_dirt_big_wall, 769, 0]]

        special_enemy_pic = [[platforms.big_ogre_a, 67, 50]]
        enemy_pic = [[platforms.fat_frog, 70, 180]]
        health_pic = [[platforms.restore_health, 70, 260]]

        portal = [[platforms.portal_snow, 700, 380]]

        for platform in intro:
            block = platforms.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # for tutorial purpose
        # for special enemy
        for platform in special_enemy_pic:
            special_eaten_A = platforms.Platform_special_enemy(platform[0])
            special_eaten_A.rect.x = platform[1]
            special_eaten_A.rect.y = platform[2]
            special_eaten_A.player = self.player
            self.special_enemy_icon_list.add(special_eaten_A)

        # for enemy
        for platform in enemy_pic:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.general_enemy_icon_list.add(eaten)

        # for health point
        for platform in health_pic:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.health_icon_list.add(love_restore)


# for NPC section
class Level_Intro_NPC(Level):
    """ This class for introduce the player to NPC """

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms.snow_dirt_wall, -140, 0],
                 [platforms.snow_dirt_intro, 0, 460],
                 [platforms.snow_dirt_big_wall, 769, 0]]

        portal = [[platforms.portal_snow, 700, 380]]

        grandpa = [[platforms.grandpa_magus, 450, 370]]

        text_grandpa = [[platforms.text_grandpa, 450, 320]]

        for platform in intro:
            block = platforms.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # for NPC purpose
        for platform in grandpa:
            gate = platforms.Platform_NPC(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.grandpa_list.add(gate)

        for platform in text_grandpa:
            gate = platforms.Platform_NPC(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.grandpa_list.add(gate)


# Create platforms for the level
# Level 01
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create Level 1 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1166

        # Array with type of platform, and x, y location of the platform.
        # for level 01
        level01 = [[platforms.dirt_wall, -140, 0],
                   [platforms.dirt_medium_long_land, 0, 460],
                   [platforms.dirt_medium_long_land, 700, 460],
                   [platforms.dirt_medium_short_land, 770, 196],
                   [platforms.dirt_short_land, 1330, 460],
                   [platforms.dirt_grass_rounded, 1146, 319],
                   [platforms.dirt_medium_short_land, 1218, 125],
                   [platforms.dirt_medium_long_land, 1680, 460],
                   [platforms.dirt_big_wall, 2100, 0]]

        water_level01 = [[platforms.medium_long_water, 490, 531],
                         [platforms.medium_short_water, 1190, 531],
                         [platforms.medium_long_water, 1470, 531]]

        portal = [[platforms.portal_snow, 2030, 380]]

        love_health = [[platforms.restore_health, 1380, 400]]

        hiragana_a = [[platforms.hiragana_a, 400, 200]]
        hiragana_i = [[platforms.hiragana_i, 600, 48]]
        hiragana_u = [[platforms.hiragana_u, 200, 200]]

        toxic_frog = [[platforms.fat_frog, 300, 405],
                      [platforms.fat_frog, 400, 405],
                      [platforms.fat_frog, 1680, 405]]

        # for special enemy
        special_enemy_a = [[platforms.big_ogre_a, 700, 360]]
        special_enemy_i = [[platforms.big_ogre_i, 1250, 20]]

        for platform in level01:
            block = platforms.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level01:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # True Point increease scores player
        # Hiragana A Point
        for platform in hiragana_a:
            true_point_lv1 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv1.rect.x = platform[1]
            true_point_lv1.rect.y = platform[2]
            true_point_lv1.player = self.player
            self.hiragana_A.add(true_point_lv1)

        # Hiragana I Point
        for platform in hiragana_i:
            true_point_lv1 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv1.rect.x = platform[1]
            true_point_lv1.rect.y = platform[2]
            true_point_lv1.player = self.player
            self.hiragana_I.add(true_point_lv1)

        # False point decrease health player
        # Hiragana U Point
        for platform in hiragana_u:
            false_point_lv1 = platforms.Platform_hiragana_katakana(platform[0])
            false_point_lv1.rect.x = platform[1]
            false_point_lv1.rect.y = platform[2]
            false_point_lv1.player = self.player
            self.hiragana_U.add(false_point_lv1)

        for platform in toxic_frog:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # for special enemy/immune enemys
        for platform in special_enemy_a:
            special_eaten_A = platforms.Platform_special_enemy(platform[0])
            special_eaten_A.rect.x = platform[1]
            special_eaten_A.rect.y = platform[2]
            special_eaten_A.player = self.player
            self.special_enemy_list_A.add(special_eaten_A)

        for platform in special_enemy_i:
            special_eaten_I = platforms.Platform_special_enemy(platform[0])
            special_eaten_I.rect.x = platform[1]
            special_eaten_I.rect.y = platform[2]
            special_eaten_I.player = self.player
            self.special_enemy_list_I.add(special_eaten_I)

        # Moving Enemy
        eaten = platforms.MovingEnemy(platforms.fat_frog)
        eaten.rect.x = 780
        eaten.rect.y = 405
        eaten.boundary_left = 700
        eaten.boundary_right = 1100
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.fat_frog)
        eaten.rect.x = 790
        eaten.rect.y = 140
        eaten.boundary_left = 790
        eaten.boundary_right = 1000
        eaten.change_x = 6
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.fat_frog)
        eaten.rect.x = 1300
        eaten.rect.y = 70
        eaten.boundary_left = 1300
        eaten.boundary_right = 1450
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)


class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create Level 2 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1096

        # Array with type of platform, and x, y location of the platform.
        # for level 02
        level02 = [[platforms.dirt_wall, -140, 0],
                   [platforms.dirt_medium_long_land, 0, 460],
                   [platforms.dirt_medium_short_land, 0, 92],
                   [platforms.dirt_wall, 700, 100],
                   [platforms.dirt_medium_short_land, 1050, 460],
                   [platforms.dirt_medium_short_land, 1050, 180],
                   [platforms.dirt_short_land, 1540, 460],
                   [platforms.dirt_short_land, 1540, 180],
                   [platforms.dirt_medium_short_land, 1890, 460],
                   [platforms.dirt_big_wall, 2030, 0]]

        water_level02 = [[platforms.medium_long_water, 490, 531],
                         [platforms.medium_long_water, 840, 531],
                         [platforms.medium_long_water, 1330, 531],
                         [platforms.medium_long_water, 1680, 531]]

        portal = [[platforms.portal_snow, 1960, 380]]

        love_health = [[platforms.restore_health, 1860, 380]]

        # true point
        hiragana_u = [[platforms.hiragana_u, 20, 10]]
        hiragana_i = [[platforms.hiragana_i, 401, 258]]
        hiragana_o = [[platforms.hiragana_o, 1280, 350]]
        hiragana_a = [[platforms.hiragana_a, 1400, 280]]
        hiragana_e = [[platforms.hiragana_e, 1400, 100]]

        # false point
        hiragana_ka = [[platforms.hiragana_ka, 560, 232]]
        hiragana_ki = [[platforms.hiragana_ki, 910, 232]]

        # for special enemy
        special_enemy_u = [[platforms.big_ogre_u, 730, 2]]
        special_enemy_o = [[platforms.big_ogre_o, 1050, 75]]
        special_enemy_i = [[platforms.big_ogre_i, 1050, 350]]
        special_enemy_a = [[platforms.big_ogre_a, 1565, 75]]
        special_enemy_e = [[platforms.big_ogre_e, 1565, 350]]

        for platform in level02:
            block = platforms.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level02:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # True Point increease scores player
        # Hiragana U Point
        for platform in hiragana_u:
            true_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.hiragana_U_lv2.add(true_point_lv2)

        # Hiragana I
        for platform in hiragana_i:
            true_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.hiragana_I_lv2.add(true_point_lv2)

        # Hiragana O
        for platform in hiragana_o:
            true_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.hiragana_O.add(true_point_lv2)

        # Hiragana a
        for platform in hiragana_a:
            true_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.hiragana_A_lv2.add(true_point_lv2)

        # Hiragana e
        for platform in hiragana_e:
            true_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv2.rect.x = platform[1]
            true_point_lv2.rect.y = platform[2]
            true_point_lv2.player = self.player
            self.hiragana_E.add(true_point_lv2)

        # False Point
        # Hiragana Ka
        for platform in hiragana_ka:
            false_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            false_point_lv2.rect.x = platform[1]
            false_point_lv2.rect.y = platform[2]
            false_point_lv2.player = self.player
            self.hiragana_KA.add(false_point_lv2)

        # Hiragana Ki
        for platform in hiragana_ki:
            false_point_lv2 = platforms.Platform_hiragana_katakana(platform[0])
            false_point_lv2.rect.x = platform[1]
            false_point_lv2.rect.y = platform[2]
            false_point_lv2.player = self.player
            self.hiragana_KI.add(false_point_lv2)

        # for special enemy
        # Hiragana U
        for platform in special_enemy_u:
            special_eaten_U_lv2 = platforms.Platform_special_enemy(platform[0])
            special_eaten_U_lv2.rect.x = platform[1]
            special_eaten_U_lv2.rect.y = platform[2]
            special_eaten_U_lv2.player = self.player
            self.special_enemy_list_U_lv2.add(special_eaten_U_lv2)

        # Hiragana O
        for platform in special_enemy_o:
            special_eaten_O = platforms.Platform_special_enemy(platform[0])
            special_eaten_O.rect.x = platform[1]
            special_eaten_O.rect.y = platform[2]
            special_eaten_O.player = self.player
            self.special_enemy_list_O.add(special_eaten_O)

        # Hiragana I
        for platform in special_enemy_i:
            special_eaten_I_lv2 = platforms.Platform_special_enemy(platform[0])
            special_eaten_I_lv2.rect.x = platform[1]
            special_eaten_I_lv2.rect.y = platform[2]
            special_eaten_I_lv2.player = self.player
            self.special_enemy_list_I_lv2.add(special_eaten_I_lv2)

        # Hiragana A
        for platform in special_enemy_a:
            special_eaten_A_lv2 = platforms.Platform_special_enemy(platform[0])
            special_eaten_A_lv2.rect.x = platform[1]
            special_eaten_A_lv2.rect.y = platform[2]
            special_eaten_A_lv2.player = self.player
            self.special_enemy_list_A_lv2.add(special_eaten_A_lv2)

        # Hiragana E
        for platform in special_enemy_e:
            special_eaten_E = platforms.Platform_special_enemy(platform[0])
            special_eaten_E.rect.x = platform[1]
            special_eaten_E.rect.y = platform[2]
            special_eaten_E.player = self.player
            self.special_enemy_list_E.add(special_eaten_E)

        # add moving sprites
        block = platforms.MovingPlatform_dirt(platforms.dirt_grass_rounded)
        block.rect.x = 560
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform_dirt(platforms.dirt_grass_rounded)
        block.rect.x = 910
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemy
        eaten = platforms.MovingEnemy(platforms.bad_ogre)
        eaten.rect.x = 200
        eaten.rect.y = 400
        eaten.boundary_left = 200
        eaten.boundary_right = 450
        eaten.change_x = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.bad_ogre)
        eaten.rect.x = 70
        eaten.rect.y = 30
        eaten.boundary_left = 70
        eaten.boundary_right = 230
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.bad_ogre)
        eaten.rect.x = 1160
        eaten.rect.y = 120
        eaten.boundary_left = 1160
        eaten.boundary_right = 1300
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.bad_ogre)
        eaten.rect.x = 1160
        eaten.rect.y = 400
        eaten.boundary_left = 1160
        eaten.boundary_right = 1300
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)


# Level 03
class Level_03(Level):

    def __init__(self, player):
        """ Definition for Level 03 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/night_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1166

        # Array with type of platform, and x, y location of the platform.
        # for level 02
        level02 = [[platforms.brick_dark_wall, -140, 0],
                   [platforms.brick_medium_short_land, 0, 529],
                   [platforms.brick_medium_large_land, 0, 141],
                   [platforms.brick_dark_small_stairs1, 281, 459],
                   [platforms.brick_dark_small_stairs2, 351, 389],
                   [platforms.brick_dark_small_stairs3, 421, 319],
                   [platforms.brick_dark_grass_rounded, 281, 214],
                   [platforms.brick_small_short_land, 642, 102],
                   [platforms.brick_dark_grass_rounded, 713, 384],
                   [platforms.brick_medium_long_land, 840, 528],
                   [platforms.brick_medium_large_long_land, 869, 272],
                   [platforms.brick_half_short_land, 943, 131],
                   [platforms.brick_dark_small_stairs1, 1680, 480],
                   [platforms.brick_large_high_land, 1750, 410],
                   [platforms.brick_dark_big_wall, 2100, 0]]

        sharp_rock_level02 = [[platforms.medium_sharp_rock, 490, 540],
                              [platforms.small_sharp_rock, 700, 540],
                              [platforms.medium_sharp_rock, 1260, 540],
                              [platforms.medium_sharp_rock, 1470, 540]]

        portal = [[platforms.portal_snow, 2030, 335]]

        love_health = [[platforms.restore_health, 980, 80]]

        # enemys
        bad_bat = [[platforms.dark_bat, 280, 400],
                   [platforms.dark_bat, 350, 330],
                   [platforms.dark_bat, 420, 260],
                   [platforms.dark_bat, 280, 150],
                   [platforms.dark_bat, 1680, 400]]

        # special enemys
        special_enemy_ka = [[platforms.dark_rabbit_ka, 700, 2]]
        special_enemy_ki = [[platforms.dark_rabbit_ki, 710, 275]]
        special_enemy_ku = [[platforms.dark_rabbit_ku, 130, 30]]
        special_enemy_ke = [[platforms.dark_rabbit_ke, 1050, 170]]
        special_enemy_ko = [[platforms.dark_rabbit_ko, 1750, 300]]

        # hiragana point
        hiragana_ka = [[platforms.hiragana_ka, 30, 30]]
        hiragana_ki = [[platforms.hiragana_ki, 500, 180]]
        hiragana_ku = [[platforms.hiragana_ku, 280, 50]]
        hiragana_ke = [[platforms.hiragana_ke, 800, 150]]
        hiragana_ko = [[platforms.hiragana_ko, 1200, 400]]

        for platform in level02:
            block = platforms.Platform_dark_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in sharp_rock_level02:
            sharp_rock = platforms.Platform_dark_brick(platform[0])
            sharp_rock.rect.x = platform[1]
            sharp_rock.rect.y = platform[2]
            sharp_rock.player = self.player
            self.death_place_list.add(sharp_rock)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        for platform in bad_bat:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # Special enemys
        # Hiragana Ka
        for platform in special_enemy_ka:
            special_eaten_KA = platforms.Platform_special_enemy(platform[0])
            special_eaten_KA.rect.x = platform[1]
            special_eaten_KA.rect.y = platform[2]
            special_eaten_KA.player = self.player
            self.special_enemy_list_KA.add(special_eaten_KA)

        # Hiragana Ki
        for platform in special_enemy_ki:
            special_eaten_KI = platforms.Platform_special_enemy(platform[0])
            special_eaten_KI.rect.x = platform[1]
            special_eaten_KI.rect.y = platform[2]
            special_eaten_KI.player = self.player
            self.special_enemy_list_KI.add(special_eaten_KI)

        # Hiragana Ku
        for platform in special_enemy_ku:
            special_eaten_KU = platforms.Platform_special_enemy(platform[0])
            special_eaten_KU.rect.x = platform[1]
            special_eaten_KU.rect.y = platform[2]
            special_eaten_KU.player = self.player
            self.special_enemy_list_KU.add(special_eaten_KU)

        # Hiragana Ke
        for platform in special_enemy_ke:
            special_eaten_KE = platforms.Platform_special_enemy(platform[0])
            special_eaten_KE.rect.x = platform[1]
            special_eaten_KE.rect.y = platform[2]
            special_eaten_KE.player = self.player
            self.special_enemy_list_KE.add(special_eaten_KE)

        # Hiragana Ko
        for platform in special_enemy_ko:
            special_eaten_KO = platforms.Platform_special_enemy(platform[0])
            special_eaten_KO.rect.x = platform[1]
            special_eaten_KO.rect.y = platform[2]
            special_eaten_KO.player = self.player
            self.special_enemy_list_KO.add(special_eaten_KO)

        # Point
        # Hiragana Ka
        for platform in hiragana_ka:
            true_point_lv3 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KA_lv3.add(true_point_lv3)

        # Hiragana Ki
        for platform in hiragana_ki:
            true_point_lv3 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KI_lv3.add(true_point_lv3)

        # Hiragana Ku
        for platform in hiragana_ku:
            true_point_lv3 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KU.add(true_point_lv3)

        # Hiragana Ke
        for platform in hiragana_ke:
            true_point_lv3 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KE.add(true_point_lv3)

        # Hiragana Ko
        for platform in hiragana_ko:
            true_point_lv3 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv3.rect.x = platform[1]
            true_point_lv3.rect.y = platform[2]
            true_point_lv3.player = self.player
            self.hiragana_KO.add(true_point_lv3)

        # add moving sprites
        block = platforms.MovingPlatform_dark_brick(
            platforms.brick_half_small_land)
        block.rect.x = 1302
        block.rect.y = 483
        block.boundary_left = 1302
        block.boundary_right = 1600
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemys
        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 900
        eaten.rect.y = 200
        eaten.boundary_left = 900
        eaten.boundary_right = 1000
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 800
        eaten.rect.y = 450
        eaten.boundary_left = 800
        eaten.boundary_right = 1000
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)


class Level_04(Level):
    def __init__(self, player):
        """ Definition for Level 04 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1095

        # Array with type of platform, and x, y location of the platform.
        # for level 03
        level04 = [[platforms.brick_red_wall, -140, 0],
                   [platforms.brick_red_medium_long_land, 0, 529],
                   [platforms.brick_red_medium_long_land, 210, 529],
                   [platforms.brick_red_grass_rounded, 300, 150],
                   [platforms.brick_red_medium_short_land, 0, 150],
                   [platforms.brick_red_grass_left_right_long, 700, 180],
                   [platforms.brick_red_medium_long_land, 979, 80],
                   [platforms.brick_red_medium_long_land, 979, 280],
                   [platforms.brick_red_medium_high_land, 979, 470],
                   [platforms.brick_red_medium_short_land, 1049, 529],
                   [platforms.brick_red_medium_high_land, 1189, 470],
                   [platforms.brick_red_grass_left_right_long, 1400, 250],
                   [platforms.brick_red_grass_left_right_long, 1400, -300],
                   [platforms.brick_red_medium_high_large_land, 1609, 470],
                   [platforms.brick_red_medium_short_land, 1819, 540],
                   [platforms.brick_red_medium_short_land, 1959, 540],
                   [platforms.brick_red_big_wall, 2029, 0]]

        water_level04 = [[platforms.medium_long_water, 490, 532],
                         [platforms.medium_long_water, 770, 532],
                         [platforms.medium_long_water, 1260, 532],
                         [platforms.medium_short_water, 1470, 532]]

        portal = [[platforms.portal_snow, 1930, 440]]

        love_health = [[platforms.restore_health, 80, 50],
                       [platforms.restore_health, 1100, 480],
                       [platforms.restore_health, 1300, 340]]

        # special enemys
        special_enemy_sa = [[platforms.orange_slime_sa, 695, 80]]
        special_enemy_si = [[platforms.orange_slime_si, 295, 50]]
        special_enemy_su = [[platforms.orange_slime_su, 1180, 183]]
        special_enemy_se = [[platforms.orange_slime_se, 1395, 150]]
        special_enemy_so = [[platforms.orange_slime_so, 1609, 370]]

        # Hiragana Point
        hiragana_sa = [[platforms.hiragana_sa, 150, 50]]
        hiragana_si = [[platforms.hiragana_so, 560, 100]]
        hiragana_su = [[platforms.hiragana_su, 1189, 370]]
        hiragana_se = [[platforms.hiragana_se, 1189, 10]]
        hiragana_so = [[platforms.hiragana_so, 1500, 340]]

        for platform in level04:
            block = platforms.Platform_grass_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level04:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # Special enemys
        # Hiragana Sa
        for platform in special_enemy_sa:
            special_eaten_SA = platforms.Platform_special_enemy(platform[0])
            special_eaten_SA.rect.x = platform[1]
            special_eaten_SA.rect.y = platform[2]
            special_eaten_SA.player = self.player
            self.special_enemy_list_SA.add(special_eaten_SA)

        # Hiragana Si
        for platform in special_enemy_si:
            special_eaten_SI = platforms.Platform_special_enemy(platform[0])
            special_eaten_SI.rect.x = platform[1]
            special_eaten_SI.rect.y = platform[2]
            special_eaten_SI.player = self.player
            self.special_enemy_list_SI.add(special_eaten_SI)

        # Hiragana Su
        for platform in special_enemy_su:
            special_eaten_SU = platforms.Platform_special_enemy(platform[0])
            special_eaten_SU.rect.x = platform[1]
            special_eaten_SU.rect.y = platform[2]
            special_eaten_SU.player = self.player
            self.special_enemy_list_SU.add(special_eaten_SU)

        # Hiragana Se
        for platform in special_enemy_se:
            special_eaten_SE = platforms.Platform_special_enemy(platform[0])
            special_eaten_SE.rect.x = platform[1]
            special_eaten_SE.rect.y = platform[2]
            special_eaten_SE.player = self.player
            self.special_enemy_list_SE.add(special_eaten_SE)

        # Hiragana So
        for platform in special_enemy_so:
            special_eaten_SO = platforms.Platform_special_enemy(platform[0])
            special_eaten_SO.rect.x = platform[1]
            special_eaten_SO.rect.y = platform[2]
            special_eaten_SO.player = self.player
            self.special_enemy_list_SO.add(special_eaten_SO)

        # Point
        # Hiragana Sa
        for platform in hiragana_sa:
            true_point_lv4 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.hiragana_SA.add(true_point_lv4)

        # Hiragana Si
        for platform in hiragana_si:
            true_point_lv4 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.hiragana_SI.add(true_point_lv4)

        # Hiragana Si
        for platform in hiragana_su:
            true_point_lv4 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.hiragana_SU.add(true_point_lv4)

        # Hiragana Se
        for platform in hiragana_se:
            true_point_lv4 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.hiragana_SE.add(true_point_lv4)

        # Hiragana So
        for platform in hiragana_so:
            true_point_lv4 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv4.rect.x = platform[1]
            true_point_lv4.rect.y = platform[2]
            true_point_lv4.player = self.player
            self.hiragana_SO.add(true_point_lv4)

        # add moving sprites
        block = platforms.MovingPlatform_brick_red(
            platforms.brick_red_small_half)
        block.rect.x = 560
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_brick_red(
            platforms.brick_red_small_half)
        block.rect.x = 800
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Enemys
        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 0
        eaten.rect.y = 100
        eaten.boundary_left = 0
        eaten.boundary_right = 100
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 300
        eaten.rect.y = 480
        eaten.boundary_left = 300
        eaten.boundary_right = 400
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 350
        eaten.rect.y = 480
        eaten.boundary_left = 350
        eaten.boundary_right = 450
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1000
        eaten.rect.y = 230
        eaten.boundary_left = 1000
        eaten.boundary_right = 1150
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 560
        eaten.rect.y = 200
        eaten.boundary_top = 100
        eaten.boundary_bottom = 400
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 600
        eaten.rect.y = 20
        eaten.boundary_left = 600
        eaten.boundary_right = 800
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 800
        eaten.rect.y = 200
        eaten.boundary_top = 100
        eaten.boundary_bottom = 400
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 979
        eaten.rect.y = 370
        eaten.boundary_left = 979
        eaten.boundary_right = 1200
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1300
        eaten.rect.y = 200
        eaten.boundary_top = 100
        eaten.boundary_bottom = 400
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1500
        eaten.rect.y = 200
        eaten.boundary_top = 100
        eaten.boundary_bottom = 400
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1600
        eaten.rect.y = 280
        eaten.boundary_left = 1600
        eaten.boundary_right = 1800
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.fat_frog)
        eaten.rect.x = 979
        eaten.rect.y = 30
        eaten.boundary_left = 979
        eaten.boundary_right = 1100
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.fat_frog)
        eaten.rect.x = 1045
        eaten.rect.y = 480
        eaten.boundary_left = 1045
        eaten.boundary_right = 1150
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)


class Level_05(Level):
    def __init__(self, player):
        """ Definition for Level 05 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/snow_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1583

        # Array with type of platform, and x, y location of the platform.
        # for level 04
        level05 = [[platforms.brick_red_wall, -220, 0],
                   [platforms.brick_basic, -80, 530],
                   [platforms.brick_red_snow_medium_short_land, -20, 530],
                   [platforms.brick_red_medium_bottom, 500, 300],
                   [platforms.brick_red_snow_high_small_left_right, 499, 160],
                   [platforms.brick_red_snow_medium_short_land, 500, 90],
                   [platforms.brick_red_snow_medium_short_land, 640, 90],
                   [platforms.brick_basic, 980, 529],
                   [platforms.brick_red_snow_medium_short_land, 1050, 530],
                   [platforms.brick_red_snow_high_small_left_right, 978, 387],
                   [platforms.brick_red_snow_medium_short_land, 978, 317],
                   [platforms.brick_red_snow_high_small_left_right, 1188, 177],
                   [platforms.brick_red_snow_medium_short_land, 1188, 177],
                   [platforms.brick_red_snow_high_small_left_right, 1677, 177],
                   [platforms.brick_basic, 1680, 317],
                   [platforms.brick_red_snow_medium_short_land, 1750, 317],
                   [platforms.brick_basic, 2030, 317],
                   [platforms.brick_red_snow_high_small_left_right, 2027, 177],
                   [platforms.brick_red_snow_high_small_left_right, 2027, 37],
                   [platforms.brick_red_snow_medium_short_land, 2237, 530],
                   [platforms.brick_red_big_wall,  2517, 0],
                   [platforms.brick_red_wall, 2790, 0]]

        water_level05 = [[platforms.medium_short_water, 260, 531],
                         [platforms.medium_long_water, 280, 531],
                         [platforms.medium_long_water, 490, 531],
                         [platforms.medium_long_water, 700, 531],
                         [platforms.medium_short_water, 770, 531],
                         [platforms.medium_short_water, 840, 531],
                         [platforms.medium_long_water, 1330, 531],
                         [platforms.medium_long_water, 1540, 531],
                         [platforms.medium_long_water, 1750, 531],
                         [platforms.medium_long_water, 1960, 531],
                         [platforms.medium_short_water, 2100, 531]]

        portal = [[platforms.portal_snow, 2447, 440]]

        love_health = [[platforms.restore_health, 1130, 421]]

        # for special enemys
        special_enemy_ta = [[platforms.big_ogre_ta, 700, 190]]
        special_enemy_tu = [[platforms.big_ogre_tu, 1200, 421]]
        special_enemy_te = [[platforms.big_ogre_te, 1680, 70]]
        special_enemy_to = [[platforms.big_ogre_to, 2230, 421]]

        # for point hiragana
        hiragana_ta = [[platforms.hiragana_ta, 1000, 190]]
        hiragana_ti = [[platforms.hiragana_ti, 600, 190]]
        hiragana_tu = [[platforms.hiragana_tu, 1538, 200]]
        hiragana_te = [[platforms.hiragana_te, 1950, 190]]
        hiragana_to = [[platforms.hiragana_to, 1050, 421]]

        for platform in level05:
            block = platforms.Platform_grass_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level05:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # Special enemys
        # Hiragana Ta
        for platform in special_enemy_ta:
            special_eaten_TA = platforms.Platform_special_enemy(platform[0])
            special_eaten_TA.rect.x = platform[1]
            special_eaten_TA.rect.y = platform[2]
            special_eaten_TA.player = self.player
            self.special_enemy_list_TA.add(special_eaten_TA)

        # Hiragana Tu
        for platform in special_enemy_tu:
            special_eaten_TU = platforms.Platform_special_enemy(platform[0])
            special_eaten_TU.rect.x = platform[1]
            special_eaten_TU.rect.y = platform[2]
            special_eaten_TU.player = self.player
            self.special_enemy_list_TU.add(special_eaten_TU)

        # Hiragana Te
        for platform in special_enemy_te:
            special_eaten_TE = platforms.Platform_special_enemy(platform[0])
            special_eaten_TE.rect.x = platform[1]
            special_eaten_TE.rect.y = platform[2]
            special_eaten_TE.player = self.player
            self.special_enemy_list_TE.add(special_eaten_TE)

        # Hiragana To
        for platform in special_enemy_to:
            special_eaten_TO = platforms.Platform_special_enemy(platform[0])
            special_eaten_TO.rect.x = platform[1]
            special_eaten_TO.rect.y = platform[2]
            special_eaten_TO.player = self.player
            self.special_enemy_list_TO.add(special_eaten_TO)

        # Point
        # Hiragana Ta
        for platform in hiragana_ta:
            true_point_lv5 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.hiragana_TA.add(true_point_lv5)

        # Hiragana Ti
        for platform in hiragana_ti:
            true_point_lv5 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.hiragana_TI.add(true_point_lv5)

        # Hiragana Ti
        for platform in hiragana_tu:
            true_point_lv5 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.hiragana_TU.add(true_point_lv5)

        # Hiragana Te
        for platform in hiragana_te:
            true_point_lv5 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.hiragana_TE.add(true_point_lv5)

        # Hiragana To
        for platform in hiragana_to:
            true_point_lv5 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv5.rect.x = platform[1]
            true_point_lv5.rect.y = platform[2]
            true_point_lv5.player = self.player
            self.hiragana_TO.add(true_point_lv5)

        # add moving sprites
        block = platforms.MovingPlatform_brick_red(
            platforms.brick_red_snow_small_half)
        block.rect.x = 350
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_brick_red(
            platforms.brick_red_snow_small_half)
        block.rect.x = 850
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_brick_red(
            platforms.brick_red_snow_small_half)
        block.rect.x = 1538
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_brick_red(
            platforms.brick_red_snow_small_half)
        block.rect.x = 1302
        block.rect.y = 483
        block.boundary_left = 1302
        block.boundary_right = 2167
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # moving enemys
        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 500
        eaten.rect.y = 30
        eaten.boundary_left = 500
        eaten.boundary_right = 700
        eaten.change_x = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 600
        eaten.rect.y = 30
        eaten.boundary_left = 600
        eaten.boundary_right = 900
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 750
        eaten.rect.y = 190
        eaten.boundary_top = 120
        eaten.boundary_bottom = 300
        eaten.change_y = 6
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 950
        eaten.rect.y = 190
        eaten.boundary_top = 30
        eaten.boundary_bottom = 300
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 1185
        eaten.rect.y = 100
        eaten.boundary_left = 1185
        eaten.boundary_right = 1400
        eaten.change_x = 6
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1250
        eaten.rect.y = 300
        eaten.boundary_top = 300
        eaten.boundary_bottom = 500
        eaten.change_y = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1538
        eaten.rect.y = 190
        eaten.boundary_top = 30
        eaten.boundary_bottom = 300
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1800
        eaten.rect.y = 190
        eaten.boundary_top = 30
        eaten.boundary_bottom = 300
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 1830
        eaten.rect.y = 250
        eaten.boundary_left = 1830
        eaten.boundary_right = 1900
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 1850
        eaten.rect.y = 250
        eaten.boundary_left = 1850
        eaten.boundary_right = 1930
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        # Moving Special Enemys
        # for sample proto special enemy move

        special_eaten_TI = platforms.MovingEnemySpecial(platforms.big_ogre_ti)
        special_eaten_TI.rect.x = 1185
        special_eaten_TI.rect.y = 70
        special_eaten_TI.boundary_left = 1185
        special_eaten_TI.boundary_right = 1400
        special_eaten_TI.change_x = 5
        special_eaten_TI.player = self.player
        special_eaten_TI.level = self
        self.special_enemy_list_TI.add(special_eaten_TI)


class Level_06(Level):
    def __init__(self, player):
        """ Definition for Level 06 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/snow_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1146

        # Array with type of platform, and x, y location of the platform.
        # for level 06
        level06 = [[platforms.snow_dirt_wall, -140, 0],
                   [platforms.snow_dirt_grass_medium_large, 0, 530],
                   [platforms.snow_dirt_grass_short_tall, 490, 390],
                   [platforms.snow_dirt_grass_medium_tall, 560, 320],
                   [platforms.snow_dirt_grass_rounded, 320, 190],
                   [platforms.snow_dirt_tall_grass_left_right, 740, 0],
                   [platforms.snow_dirt_grass_small_large, 0, 120],
                   [platforms.snow_dirt_tall_grass_left_right, 1240, 260],
                   [platforms.snow_dirt_grass_up_down, 1310, 260],
                   [platforms.snow_dirt_grass_medium_large, 1380, 460],
                   [platforms.snow_dirt_grass_medium_large, 1870, 460],
                   [platforms.snow_dirt_big_wall, 2080, 0]]

        water_level06 = [[platforms.medium_long_water, 280, 531],
                         [platforms.medium_long_water, 630, 531],
                         [platforms.medium_long_water, 840, 531],
                         [platforms.medium_long_water, 1030, 531],
                         [platforms.medium_short_water, 1310, 531],
                         [platforms.medium_long_water, 1660, 531]]

        portal = [[platforms.portal_snow, 2010, 390]]

        love_health = [[platforms.restore_health, 0, 40],
                       [platforms.restore_health, 1450, 350]]

        # hiragana point
        hiragana_na = [[platforms.hiragana_na, 560, 100]]
        hiragana_ni = [[platforms.hiragana_ni, 200, 175]]
        hiragana_nu = [[platforms.hiragana_nu, 640, 0]]
        hiragana_ne = [[platforms.hiragana_ne, 830, 35]]
        hiragana_no = [[platforms.hiragana_no, 1380, 350]]

        # enemys
        ghost = [[platforms.skull_ghost, 490, 330],
                 [platforms.skull_ghost, 580, 260]]

        # special enemys
        special_enemy_na = [[platforms.dark_rabbit_na, 320, 80]]
        special_enemy_ni = [[platforms.dark_rabbit_ni, 50, 15]]
        special_enemy_no = [[platforms.dark_rabbit_no, 1870, 350]]

        for platform in level06:
            block = platforms.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level06:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # Enemys
        for platform in ghost:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # Special enemys
        # Hiragana Na
        for platform in special_enemy_na:
            special_eaten_NA = platforms.Platform_special_enemy(platform[0])
            special_eaten_NA.rect.x = platform[1]
            special_eaten_NA.rect.y = platform[2]
            special_eaten_NA.player = self.player
            self.special_enemy_list_NA.add(special_eaten_NA)

        # Hiragana Ni
        for platform in special_enemy_ni:
            special_eaten_NI = platforms.Platform_special_enemy(platform[0])
            special_eaten_NI.rect.x = platform[1]
            special_eaten_NI.rect.y = platform[2]
            special_eaten_NI.player = self.player
            self.special_enemy_list_NI.add(special_eaten_NI)

        # Hiragana No
        for platform in special_enemy_no:
            special_eaten_NO = platforms.Platform_special_enemy(platform[0])
            special_eaten_NO.rect.x = platform[1]
            special_eaten_NO.rect.y = platform[2]
            special_eaten_NO.player = self.player
            self.special_enemy_list_NO.add(special_eaten_NO)

        # Point
        # Hiragana Na
        for platform in hiragana_na:
            true_point_lv6 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NA.add(true_point_lv6)

        # Hiragana Ni
        for platform in hiragana_ni:
            true_point_lv6 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NI.add(true_point_lv6)

        # Hiragana Nu
        for platform in hiragana_nu:
            true_point_lv6 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NU.add(true_point_lv6)

        # Hiragana Ne
        for platform in hiragana_ne:
            true_point_lv6 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NE.add(true_point_lv6)

        # Hiragana No
        for platform in hiragana_no:
            true_point_lv6 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv6.rect.x = platform[1]
            true_point_lv6.rect.y = platform[2]
            true_point_lv6.player = self.player
            self.hiragana_NO.add(true_point_lv6)

        # add moving sprites
        block = platforms.MovingPlatform_snow(platforms.snow_dirt_half)
        block.rect.x = 690
        block.rect.y = 483
        block.boundary_left = 690
        block.boundary_right = 1100
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform_snow(platforms.snow_dirt_half)
        block.rect.x = 820
        block.rect.y = 343
        block.boundary_left = 820
        block.boundary_right = 1100
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 690
        eaten.rect.y = 430
        eaten.boundary_left = 690
        eaten.boundary_right = 1100
        eaten.change_x = 2
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 690
        eaten.rect.y = 380
        eaten.boundary_left = 690
        eaten.boundary_right = 1100
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.skull_ghost)
        eaten.rect.x = 1350
        eaten.rect.y = 200
        eaten.boundary_left = 1350
        eaten.boundary_right = 1450
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        # add moving special enemys
        special_eaten_NU = platforms.MovingEnemySpecial(
            platforms.dark_rabbit_nu)
        special_eaten_NU.rect.x = 820
        special_eaten_NU.rect.y = 235
        special_eaten_NU.boundary_left = 820
        special_eaten_NU.boundary_right = 1100
        special_eaten_NU.change_x = 4
        special_eaten_NU.player = self.player
        special_eaten_NU.level = self
        self.special_enemy_list_NU.add(special_eaten_NU)

        special_eaten_NE = platforms.MovingEnemySpecial(
            platforms.dark_rabbit_ne)
        special_eaten_NE.rect.x = 1310
        special_eaten_NE.rect.y = 150
        special_eaten_NE.boundary_left = 1310
        special_eaten_NE.boundary_right = 1450
        special_eaten_NE.change_x = 4
        special_eaten_NE.player = self.player
        special_eaten_NE.level = self
        self.special_enemy_list_NE.add(special_eaten_NE)


class Level_07(Level):
    def __init__(self, player):
        """ Definition for Level 07 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1586

        # Array with type of platform, and x, y location of the platform.
        # for level 06
        level07 = [[platforms.sand_dirt_wall, -140, 0],
                   [platforms.sand_dirt_medium_long_land, 0, 530],
                   [platforms.sand_dirt_tall_small, 560, 390],
                   [platforms.sand_dirt_tall_medium, 630, 320],
                   [platforms.sand_dirt_tall_long, 700, 250],
                   [platforms.sand_dirt_half, 560, 120],
                   [platforms.sand_dirt_wall, 920, -250],
                   [platforms.sand_dirt_basic_medium, 280, 120],
                   [platforms.sand_dirt_basic_medium, 0, 120],
                   [platforms.sand_dirt_tall_large_medium, 1190, 390],
                   [platforms.sand_dirt_medium_long_land, 1330, 460],
                   [platforms.sand_dirt_tall_large_medium, 1680, 390],
                   [platforms.sand_dirt_long_soft_up_down, 1200, 190],
                   [platforms.sand_dirt_medium_long_land, 2240, 460],
                   [platforms.sand_dirt_big_wall, 2660, 0],
                   [platforms.sand_dirt_wall, 2520, 0]]

        water_level07 = [[platforms.medium_long_water, 350, 531],
                         [platforms.medium_long_water, 770, 531],
                         [platforms.medium_long_water, 980, 531],
                         [platforms.medium_long_water, 1820, 531],
                         [platforms.medium_long_water, 2030, 531]]

        portal = [[platforms.portal_snow, 2450, 389]]

        # hiragana point
        hiragana_ha = [[platforms.hiragana_ha, 420, 210]]
        hiragana_hi = [[platforms.hiragana_hi, 820, 10]]
        hiragana_hu = [[platforms.hiragana_hu, 180, 130]]
        hiragana_he = [[platforms.hiragana_he, 0, 20]]
        hiragana_ho = [[platforms.hiragana_ho, 1520, 380]]

        # Enemys
        skull_zombie = [[platforms.old_skull, 570, 340],
                        [platforms.old_skull, 650, 270],
                        [platforms.old_skull, 710, 199]]

        # Special Enemys
        special_enemy_ha = [[platforms.orange_slime_ha, 555, 20]]
        special_enemy_hi = [[platforms.orange_slime_hi, 280, 20]]
        special_enemy_hu = [[platforms.orange_slime_hu, 60, 20]]
        special_enemy_he = [[platforms.orange_slime_he, 1200, 290]]
        special_enemy_ho = [[platforms.orange_slime_ho, 1680, 290]]

        for platform in level07:
            block = platforms.Platform_dirt_sand(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level07:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # Enemys
        for platform in skull_zombie:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # Special enemys
        # Hiragana Ha
        for platform in special_enemy_ha:
            special_eaten_HA = platforms.Platform_special_enemy(platform[0])
            special_eaten_HA.rect.x = platform[1]
            special_eaten_HA.rect.y = platform[2]
            special_eaten_HA.player = self.player
            self.special_enemy_list_HA.add(special_eaten_HA)

        # Hiragana Hi
        for platform in special_enemy_hi:
            special_eaten_HI = platforms.Platform_special_enemy(platform[0])
            special_eaten_HI.rect.x = platform[1]
            special_eaten_HI.rect.y = platform[2]
            special_eaten_HI.player = self.player
            self.special_enemy_list_HI.add(special_eaten_HI)

        # Hiragana Hu
        for platform in special_enemy_hu:
            special_eaten_HU = platforms.Platform_special_enemy(platform[0])
            special_eaten_HU.rect.x = platform[1]
            special_eaten_HU.rect.y = platform[2]
            special_eaten_HU.player = self.player
            self.special_enemy_list_HU.add(special_eaten_HU)

        # Hiragana He
        for platform in special_enemy_he:
            special_eaten_HE = platforms.Platform_special_enemy(platform[0])
            special_eaten_HE.rect.x = platform[1]
            special_eaten_HE.rect.y = platform[2]
            special_eaten_HE.player = self.player
            self.special_enemy_list_HE.add(special_eaten_HE)

        # Hiragana Ho
        for platform in special_enemy_ho:
            special_eaten_HO = platforms.Platform_special_enemy(platform[0])
            special_eaten_HO.rect.x = platform[1]
            special_eaten_HO.rect.y = platform[2]
            special_eaten_HO.player = self.player
            self.special_enemy_list_HO.add(special_eaten_HO)

        # Point
        # Hiragana Ha
        for platform in hiragana_ha:
            true_point_lv7 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.hiragana_HA.add(true_point_lv7)

        # Hiragana Hi
        for platform in hiragana_hi:
            true_point_lv7 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.hiragana_HI.add(true_point_lv7)

        # Hiragana Hu
        for platform in hiragana_hu:
            true_point_lv7 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.hiragana_HU.add(true_point_lv7)

        # Hiragana He
        for platform in hiragana_he:
            true_point_lv7 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.hiragana_HE.add(true_point_lv7)

        # Hiragana Ho
        for platform in hiragana_ho:
            true_point_lv7 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv7.rect.x = platform[1]
            true_point_lv7.rect.y = platform[2]
            true_point_lv7.player = self.player
            self.hiragana_HO.add(true_point_lv7)

        # Moving Platforms
        block = platforms.MovingPlatform_dirt_sand(platforms.sand_dirt_half)
        block.rect.x = 820
        block.rect.y = 483
        block.boundary_top = 70
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform_dirt_sand(platforms.sand_dirt_half)
        block.rect.x = 820
        block.rect.y = 483
        block.boundary_left = 820
        block.boundary_right = 1100
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemys
        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 820
        eaten.rect.y = 120
        eaten.boundary_top = 70
        eaten.boundary_bottom = 500
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1380
        eaten.rect.y = 400
        eaten.boundary_left = 1380
        eaten.boundary_right = 1700
        eaten.change_x = 6
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1380
        eaten.rect.y = 400
        eaten.boundary_left = 1380
        eaten.boundary_right = 1700
        eaten.change_x = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1380
        eaten.rect.y = 400
        eaten.boundary_left = 1380
        eaten.boundary_right = 1700
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)


class Level_08(Level):
    def __init__(self, player):
        """ Definition for Level 08 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1586

        # Array with type of platform, and x, y location of the platform.
        # for level 08
        level08 = [[platforms.sand_dirt_wall, -140, 0],
                   [platforms.sand_dirt_medium_long_land, 0, 530],
                   [platforms.sand_dirt_tall_small, 560, 390],
                   [platforms.sand_dirt_tall_medium, 630, 320],
                   [platforms.sand_dirt_tall_long, 700, 250],
                   [platforms.sand_dirt_half, 560, 120],
                   [platforms.sand_dirt_wall, 920, -250],
                   [platforms.sand_dirt_basic_medium, 280, 120],
                   [platforms.sand_dirt_basic_medium, 0, 120],
                   [platforms.sand_dirt_tall_large_medium, 1190, 390],
                   [platforms.sand_dirt_medium_long_land, 1330, 460],
                   [platforms.sand_dirt_tall_large_medium, 1680, 390],
                   [platforms.sand_dirt_long_soft_up_down, 1200, 190],
                   [platforms.sand_dirt_medium_long_land, 2240, 460],
                   [platforms.sand_dirt_big_wall, 2660, 0],
                   [platforms.sand_dirt_wall, 2520, 0]]

        water_level08 = [[platforms.medium_long_water, 350, 531],
                         [platforms.medium_long_water, 770, 531],
                         [platforms.medium_long_water, 980, 531],
                         [platforms.medium_long_water, 1820, 531],
                         [platforms.medium_long_water, 2030, 531]]

        portal = [[platforms.portal_snow, 2450, 389]]

        # hiragana point
        hiragana_ma = [[platforms.hiragana_ma, 420, 210]]
        hiragana_mi = [[platforms.hiragana_mi, 820, 10]]
        hiragana_mu = [[platforms.hiragana_mu, 180, 130]]
        hiragana_me = [[platforms.hiragana_me, 0, 20]]
        hiragana_mo = [[platforms.hiragana_mo, 1520, 380]]

        # Enemys
        skull_zombie = [[platforms.old_skull, 570, 340],
                        [platforms.old_skull, 650, 270],
                        [platforms.old_skull, 710, 199]]

        # Special Enemys
        special_enemy_ma = [[platforms.zombie_skull_ma, 555, 20]]
        special_enemy_mi = [[platforms.zombie_skull_mi, 280, 20]]
        special_enemy_mu = [[platforms.zombie_skull_mu, 60, 20]]
        special_enemy_me = [[platforms.zombie_skull_me, 1200, 290]]
        special_enemy_mo = [[platforms.zombie_skull_mo, 1680, 290]]

        for platform in level08:
            block = platforms.Platform_dirt_sand(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level08:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # Enemys
        for platform in skull_zombie:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # Special enemys
        # Hiragana Ma
        for platform in special_enemy_ma:
            special_eaten_MA = platforms.Platform_special_enemy(platform[0])
            special_eaten_MA.rect.x = platform[1]
            special_eaten_MA.rect.y = platform[2]
            special_eaten_MA.player = self.player
            self.special_enemy_list_MA.add(special_eaten_MA)

        # Hiragana Mi
        for platform in special_enemy_mi:
            special_eaten_MI = platforms.Platform_special_enemy(platform[0])
            special_eaten_MI.rect.x = platform[1]
            special_eaten_MI.rect.y = platform[2]
            special_eaten_MI.player = self.player
            self.special_enemy_list_MI.add(special_eaten_MI)

        # Hiragana Mu
        for platform in special_enemy_mu:
            special_eaten_MU = platforms.Platform_special_enemy(platform[0])
            special_eaten_MU.rect.x = platform[1]
            special_eaten_MU.rect.y = platform[2]
            special_eaten_MU.player = self.player
            self.special_enemy_list_MU.add(special_eaten_MU)

        # Hiragana Me
        for platform in special_enemy_me:
            special_eaten_ME = platforms.Platform_special_enemy(platform[0])
            special_eaten_ME.rect.x = platform[1]
            special_eaten_ME.rect.y = platform[2]
            special_eaten_ME.player = self.player
            self.special_enemy_list_ME.add(special_eaten_ME)

        # Hiragana Mo
        for platform in special_enemy_mo:
            special_eaten_MO = platforms.Platform_special_enemy(platform[0])
            special_eaten_MO.rect.x = platform[1]
            special_eaten_MO.rect.y = platform[2]
            special_eaten_MO.player = self.player
            self.special_enemy_list_MO.add(special_eaten_MO)

        # Point
        # Hiragana Ma
        for platform in hiragana_ma:
            true_point_lv8 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.hiragana_MA.add(true_point_lv8)

        # Hiragana Mi
        for platform in hiragana_mi:
            true_point_lv8 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.hiragana_MI.add(true_point_lv8)

        # Hiragana Mu
        for platform in hiragana_mu:
            true_point_lv8 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.hiragana_MU.add(true_point_lv8)

        # Hiragana Me
        for platform in hiragana_me:
            true_point_lv8 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.hiragana_ME.add(true_point_lv8)

        # Hiragana Mo
        for platform in hiragana_mo:
            true_point_lv8 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv8.rect.x = platform[1]
            true_point_lv8.rect.y = platform[2]
            true_point_lv8.player = self.player
            self.hiragana_MO.add(true_point_lv8)

        # Moving Platforms
        block = platforms.MovingPlatform_dirt_sand(platforms.sand_dirt_half)
        block.rect.x = 820
        block.rect.y = 483
        block.boundary_top = 70
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform_dirt_sand(platforms.sand_dirt_half)
        block.rect.x = 820
        block.rect.y = 483
        block.boundary_left = 820
        block.boundary_right = 1100
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving Enemys
        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 820
        eaten.rect.y = 120
        eaten.boundary_top = 70
        eaten.boundary_bottom = 500
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1380
        eaten.rect.y = 400
        eaten.boundary_left = 1380
        eaten.boundary_right = 1700
        eaten.change_x = 6
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1380
        eaten.rect.y = 400
        eaten.boundary_left = 1380
        eaten.boundary_right = 1700
        eaten.change_x = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1380
        eaten.rect.y = 400
        eaten.boundary_left = 1380
        eaten.boundary_right = 1700
        eaten.change_x = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)


class Level_09(Level):
    def __init__(self, player):
        """ Definition for Level 09 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1686

        # Array with type of platform, and x, y location of the platform.
        # for level 09
        level09 = [[platforms.ancient_brick_wall, -140, 0],
                   [platforms.ancient_brick_tall_large_long, 0, 530],
                   [platforms.ancient_brick_tall_large_long, 0, 74],
                   [platforms.ancient_brick_tall_sand_left_right, 420, 180],
                   [platforms.ancient_brick_basic, 420, 130],
                   [platforms.ancient_brick_medium_sand_top_down, 490, 130],
                   [platforms.ancient_brick_medium_sand_top_down, 490, 340],
                   [platforms.ancient_brick_tall_large_small, 910, 410],
                   [platforms.ancient_brick_tall_large_medium, 980, 480],
                   [platforms.ancient_brick_short_land, 1570, 100],
                   [platforms.ancient_brick_tall_large_long, 2200, 530],
                   [platforms.ancient_brick_tall_large_long, 2410, 530],
                   [platforms.ancient_brick_big_wall, 2620, 0],
                   [platforms.ancient_brick_wall, 2900, 0]]

        water_level09 = [[platforms.medium_long_water, 210, 531],
                         [platforms.medium_long_water, 490, 531],
                         [platforms.medium_long_water, 700, 531],
                         [platforms.medium_long_water, 1120, 531],
                         [platforms.medium_long_water, 1330, 531],
                         [platforms.medium_long_water, 1540, 531],
                         [platforms.medium_short_water, 1660, 531],
                         [platforms.medium_long_water, 1730, 531],
                         [platforms.medium_long_water, 1940, 531],
                         [platforms.medium_short_water, 2060, 531]]

        portal = [[platforms.portal_snow, 2550, 459]]

        love_health = [[platforms.restore_health, 600, 250]]

        # hiragana
        hiragana_ya = [[platforms.hiragana_ya, 20, 10]]
        hiragana_yu = [[platforms.hiragana_yu, 500, 250]]
        hiragana_yo = [[platforms.hiragana_yo, 1150, 20]]

        # Special enemy
        special_enemy_ya = [[platforms.zombie_skull_ya, 420, 35]]

        for platform in level09:
            block = platforms.Platform_ancient_brick(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level09:
            water_suicide = platforms.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # Special enemys
        # Hiragana Ya
        for platform in special_enemy_ya:
            special_eaten_YA = platforms.Platform_special_enemy(platform[0])
            special_eaten_YA.rect.x = platform[1]
            special_eaten_YA.rect.y = platform[2]
            special_eaten_YA.player = self.player
            self.special_enemy_list_YA.add(special_eaten_YA)

        # Point
        # Hiragana Ya
        for platform in hiragana_ya:
            true_point_lv9 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv9.rect.x = platform[1]
            true_point_lv9.rect.y = platform[2]
            true_point_lv9.player = self.player
            self.hiragana_YA.add(true_point_lv9)

        # Hiragana Yu
        for platform in hiragana_yu:
            true_point_lv9 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv9.rect.x = platform[1]
            true_point_lv9.rect.y = platform[2]
            true_point_lv9.player = self.player
            self.hiragana_YU.add(true_point_lv9)

        # Hiragana Yo
        for platform in hiragana_yo:
            true_point_lv9 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv9.rect.x = platform[1]
            true_point_lv9.rect.y = platform[2]
            true_point_lv9.player = self.player
            self.hiragana_YO.add(true_point_lv9)

        # add moving sprites
        block = platforms.MovingPlatform_ancient_brick(
            platforms.ancient_brick_half)
        block.rect.x = 280
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_ancient_brick(
            platforms.ancient_brick_half)
        block.rect.x = 700
        block.rect.y = 483
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_ancient_brick(
            platforms.ancient_brick_half)
        block.rect.x = 1120
        block.rect.y = 343
        block.boundary_left = 1120
        block.boundary_right = 1500
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving sprites
        block = platforms.MovingPlatform_ancient_brick(
            platforms.ancient_brick_half)
        block.rect.x = 1120
        block.rect.y = 203
        block.boundary_left = 1120
        block.boundary_right = 1500
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 70
        eaten.rect.y = 25
        eaten.boundary_left = 70
        eaten.boundary_right = 180
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 280
        eaten.rect.y = 100
        eaten.boundary_top = 100
        eaten.boundary_bottom = 450
        eaten.change_y = 4
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 700
        eaten.rect.y = 100
        eaten.boundary_top = 100
        eaten.boundary_bottom = 450
        eaten.change_y = 2
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        # add moving special enemy
        # Hiragana Yu
        special_eaten_YU = platforms.MovingEnemySpecial(
            platforms.zombie_skull_yu)
        special_eaten_YU.rect.x = 1120
        special_eaten_YU.rect.y = 110
        special_eaten_YU.boundary_left = 1120
        special_eaten_YU.boundary_right = 1500
        special_eaten_YU.change_x = 3
        special_eaten_YU.player = self.player
        special_eaten_YU.level = self
        self.special_enemy_list_YU.add(special_eaten_YU)

        # Hiragana Yo
        special_eaten_YO = platforms.MovingEnemySpecial(
            platforms.zombie_skull_yo)
        special_eaten_YO.rect.x = 1570
        special_eaten_YO.rect.y = 10
        special_eaten_YO.boundary_left = 1570
        special_eaten_YO.boundary_right = 1670
        special_eaten_YO.change_x = 3
        special_eaten_YO.player = self.player
        special_eaten_YO.level = self
        self.special_enemy_list_YO.add(special_eaten_YO)


class Level_10(Level):
    def __init__(self, player):
        """ Definition for Level 10"""

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/lava_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1656

        # Array with type of platform, and x, y location of the platform.
        # for level 09
        level10 = [[platforms.lava_rock_wall, -140, 0],
                   [platforms.lava_rock_medium_large_land, 0, 530],
                   [platforms.lava_rock_medium_large_land, 280, 530],
                   [platforms.lava_rock_small_tall, 770, 390],
                   [platforms.lava_rock_medium_tall, 840, 320],
                   [platforms.lava_rock_long_tall, 910, 250],
                   [platforms.lava_rock_basic, 1050, 98],
                   [platforms.lava_rock_basic_medium, 560, 105],
                   [platforms.lava_rock_short_small_land, 0, 98],
                   [platforms.lava_rock_medium_large_land, 1540, 410],
                   [platforms.lava_rock_long_tall, 2100, 110],
                   [platforms.lava_rock_medium_large_land, 2380, 410],
                   [platforms.lava_rock_big_wall, 2590, 0],
                   [platforms.lava_rock_wall, 2870, 0]]

        lava_water_level10 = [[platforms.lava_water_long, 560, 531],
                              [platforms.lava_water_long, 980, 531],
                              [platforms.lava_water_long, 1190, 531],
                              [platforms.lava_water, 1400, 531],
                              [platforms.lava_water, 1470, 531],
                              [platforms.lava_water_long, 1820, 531],
                              [platforms.lava_water, 2030, 531],
                              [platforms.lava_water_long, 2170, 531]]

        portal = [[platforms.portal_snow, 2520, 340]]

        love_health = [[platforms.restore_health, 70, 20]]

        # Hiragana Point
        hiragana_ra = [[platforms.hiragana_ra, 1050, 20]]
        hiragana_ri = [[platforms.hiragana_ri, 350, 100]]
        hiragana_ru = [[platforms.hiragana_ru, 0, 20]]
        hiragana_re = [[platforms.hiragana_re, 1650, 100]]
        hiragana_ro = [[platforms.hiragana_ro, 1800, 100]]

        # enemys
        slime_lava = [[platforms.orange_slime, 770, 357],
                      [platforms.orange_slime, 805, 357],
                      [platforms.orange_slime, 840, 286],
                      [platforms.orange_slime, 875, 286],
                      [platforms.orange_slime, 910, 216],
                      [platforms.orange_slime, 945, 216]]

        # special enemys
        special_enemy_ro = [[platforms.slime_lava_ro, 2100, 10]]

        for platform in level10:
            block = platforms.Platform_lava_rock(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in lava_water_level10:
            lava_water_suicide = platforms.Platform_lava_rock(platform[0])
            lava_water_suicide.rect.x = platform[1]
            lava_water_suicide.rect.y = platform[2]
            lava_water_suicide.player = self.player
            self.death_place_list.add(lava_water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # Enemys
        for platform in slime_lava:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # Special enemys
        # Hiragana Ro
        for platform in special_enemy_ro:
            special_eaten_RO = platforms.Platform_special_enemy(platform[0])
            special_eaten_RO.rect.x = platform[1]
            special_eaten_RO.rect.y = platform[2]
            special_eaten_RO.player = self.player
            self.special_enemy_list_RO.add(special_eaten_RO)

        # Point
        # Hiragana Ra
        for platform in hiragana_ra:
            true_point_lv10 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.hiragana_RA.add(true_point_lv10)

        # Hiragana RI
        for platform in hiragana_ri:
            true_point_lv10 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.hiragana_RI.add(true_point_lv10)

        # Hiragana Ru
        for platform in hiragana_ru:
            true_point_lv10 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.hiragana_RU.add(true_point_lv10)

        # Hiragana Re
        for platform in hiragana_re:
            true_point_lv10 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.hiragana_RE.add(true_point_lv10)

        # Hiragana Ro
        for platform in hiragana_ro:
            true_point_lv10 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv10.rect.x = platform[1]
            true_point_lv10.rect.y = platform[2]
            true_point_lv10.player = self.player
            self.hiragana_RO.add(true_point_lv10)

        # add moving sprites
        block = platforms.MovingPlatform_lava_rock(platforms.lava_rock_half)
        block.rect.x = 1960
        block.rect.y = 110
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1540
        eaten.rect.y = 350
        eaten.boundary_left = 1540
        eaten.boundary_right = 1780
        eaten.change_x = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1540
        eaten.rect.y = 350
        eaten.boundary_left = 1540
        eaten.boundary_right = 1780
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1540
        eaten.rect.y = 350
        eaten.boundary_left = 1540
        eaten.boundary_right = 1780
        eaten.change_x = 2
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1960
        eaten.rect.y = 110
        eaten.boundary_top = 100
        eaten.boundary_bottom = 450
        eaten.change_y = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        # add moving special enemys
        # Hiragana Ra
        special_eaten_RA = platforms.MovingEnemySpecial(
            platforms.slime_lava_ra)
        special_eaten_RA.rect.x = 560
        special_eaten_RA.rect.y = 10
        special_eaten_RA.boundary_left = 560
        special_eaten_RA.boundary_right = 630
        special_eaten_RA.change_x = 3
        special_eaten_RA.player = self.player
        special_eaten_RA.level = self
        self.special_enemy_list_RA.add(special_eaten_RA)

        # Hiragana Ri
        special_eaten_RI = platforms.MovingEnemySpecial(
            platforms.slime_lava_ri)
        special_eaten_RI.rect.x = 50
        special_eaten_RI.rect.y = 10
        special_eaten_RI.boundary_left = 50
        special_eaten_RI.boundary_right = 150
        special_eaten_RI.change_x = 3
        special_eaten_RI.player = self.player
        special_eaten_RI.level = self
        self.special_enemy_list_RI.add(special_eaten_RI)

        # Hiragana Ru
        special_eaten_RU = platforms.MovingEnemySpecial(
            platforms.slime_lava_ru)
        special_eaten_RU.rect.x = 1540
        special_eaten_RU.rect.y = 320
        special_eaten_RU.boundary_left = 1540
        special_eaten_RU.boundary_right = 1780
        special_eaten_RU.change_x = 4
        special_eaten_RU.player = self.player
        special_eaten_RU.level = self
        self.special_enemy_list_RU.add(special_eaten_RU)

        # Hiragana Re
        special_eaten_RE = platforms.MovingEnemySpecial(
            platforms.slime_lava_re)
        special_eaten_RE.rect.x = 1960
        special_eaten_RE.rect.y = 110
        special_eaten_RE.boundary_top = 100
        special_eaten_RE.boundary_bottom = 450
        special_eaten_RE.change_y = 3
        special_eaten_RE.player = self.player
        special_eaten_RE.level = self
        self.special_enemy_list_RE.add(special_eaten_RE)


class Level_11(Level):
    def __init__(self, player):
        """ Definition for Level 11"""

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/lava_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1656

        # Array with type of platform, and x, y location of the platform.
        # for level 11
        level11 = [[platforms.lava_rock_wall, -140, 0],
                   [platforms.lava_rock_medium_large_land, 0, 530],
                   [platforms.lava_rock_medium_large_land, 280, 530],
                   [platforms.lava_rock_small_tall, 770, 390],
                   [platforms.lava_rock_medium_tall, 840, 320],
                   [platforms.lava_rock_long_tall, 910, 250],
                   [platforms.lava_rock_basic, 1050, 98],
                   [platforms.lava_rock_basic_medium, 560, 105],
                   [platforms.lava_rock_short_small_land, 0, 98],
                   [platforms.lava_rock_medium_large_land, 1540, 410],
                   [platforms.lava_rock_long_tall, 2100, 110],
                   [platforms.lava_rock_medium_large_land, 2380, 410],
                   [platforms.lava_rock_big_wall, 2590, 0],
                   [platforms.lava_rock_wall, 2870, 0]]

        lava_water_level11 = [[platforms.lava_water_long, 560, 531],
                              [platforms.lava_water_long, 980, 531],
                              [platforms.lava_water_long, 1190, 531],
                              [platforms.lava_water, 1400, 531],
                              [platforms.lava_water, 1470, 531],
                              [platforms.lava_water_long, 1820, 531],
                              [platforms.lava_water, 2030, 531],
                              [platforms.lava_water_long, 2170, 531]]

        portal = [[platforms.portal_snow, 2520, 340]]

        love_health = [[platforms.restore_health, 70, 20]]

        # Hiragana Point
        hiragana_wa = [[platforms.hiragana_wa, 1050, 20]]
        hiragana_wo = [[platforms.hiragana_wo, 350, 100]]
        hiragana_n = [[platforms.hiragana_n, 0, 20]]

        # enemys
        slime_lava = [[platforms.orange_slime, 770, 357],
                      [platforms.orange_slime, 805, 357],
                      [platforms.orange_slime, 840, 286],
                      [platforms.orange_slime, 875, 286],
                      [platforms.orange_slime, 910, 216],
                      [platforms.orange_slime, 945, 216]]

        for platform in level11:
            block = platforms.Platform_lava_rock(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in lava_water_level11:
            lava_water_suicide = platforms.Platform_lava_rock(platform[0])
            lava_water_suicide.rect.x = platform[1]
            lava_water_suicide.rect.y = platform[2]
            lava_water_suicide.player = self.player
            self.death_place_list.add(lava_water_suicide)

        for platform in portal:
            gate = platforms.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        for platform in love_health:
            love_restore = platforms.Platform_hiragana_katakana(platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        # Enemys
        for platform in slime_lava:
            eaten = platforms.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # Point
        # Hiragana Wa
        for platform in hiragana_wa:
            true_point_lv11 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv11.rect.x = platform[1]
            true_point_lv11.rect.y = platform[2]
            true_point_lv11.player = self.player
            self.hiragana_WA.add(true_point_lv11)

        # Hiragana Wo
        for platform in hiragana_wo:
            true_point_lv11 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv11.rect.x = platform[1]
            true_point_lv11.rect.y = platform[2]
            true_point_lv11.player = self.player
            self.hiragana_WO.add(true_point_lv11)

        # Hiragana N
        for platform in hiragana_n:
            true_point_lv11 = platforms.Platform_hiragana_katakana(platform[0])
            true_point_lv11.rect.x = platform[1]
            true_point_lv11.rect.y = platform[2]
            true_point_lv11.player = self.player
            self.hiragana_N.add(true_point_lv11)

        # add moving sprites
        block = platforms.MovingPlatform_lava_rock(platforms.lava_rock_half)
        block.rect.x = 1960
        block.rect.y = 110
        block.boundary_top = 100
        block.boundary_bottom = 600
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # add moving enemys
        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1540
        eaten.rect.y = 350
        eaten.boundary_left = 1540
        eaten.boundary_right = 1780
        eaten.change_x = 5
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1540
        eaten.rect.y = 350
        eaten.boundary_left = 1540
        eaten.boundary_right = 1780
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.old_skull)
        eaten.rect.x = 1540
        eaten.rect.y = 350
        eaten.boundary_left = 1540
        eaten.boundary_right = 1780
        eaten.change_x = 2
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms.MovingEnemy(platforms.dark_bat)
        eaten.rect.x = 1960
        eaten.rect.y = 110
        eaten.boundary_top = 100
        eaten.boundary_bottom = 450
        eaten.change_y = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        # add moving special enemys
        # Hiragana Wa
        special_eaten_WA = platforms.MovingEnemySpecial(
            platforms.slime_lava_wa)
        special_eaten_WA.rect.x = 560
        special_eaten_WA.rect.y = 10
        special_eaten_WA.boundary_left = 560
        special_eaten_WA.boundary_right = 630
        special_eaten_WA.change_x = 3
        special_eaten_WA.player = self.player
        special_eaten_WA.level = self
        self.special_enemy_list_WA.add(special_eaten_WA)

        # Hiragana Wo
        special_eaten_WO = platforms.MovingEnemySpecial(
            platforms.slime_lava_wo)
        special_eaten_WO.rect.x = 50
        special_eaten_WO.rect.y = 10
        special_eaten_WO.boundary_left = 50
        special_eaten_WO.boundary_right = 150
        special_eaten_WO.change_x = 3
        special_eaten_WO.player = self.player
        special_eaten_WO.level = self
        self.special_enemy_list_WO.add(special_eaten_WO)

        # Hiragana N
        special_eaten_N = platforms.MovingEnemySpecial(platforms.slime_lava_n)
        special_eaten_N.rect.x = 1540
        special_eaten_N.rect.y = 320
        special_eaten_N.boundary_left = 1540
        special_eaten_N.boundary_right = 1780
        special_eaten_N.change_x = 4
        special_eaten_N.player = self.player
        special_eaten_N.level = self
        self.special_enemy_list_N.add(special_eaten_N)


class Level_Ending(Level):
    """ This class for introduce the player """

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/snow_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms.dirt_wall, -140, 0],
                 [platforms.dirt_medium_long_land, 0, 460],
                 [platforms.dirt_medium_long_land, 480, 460],
                 [platforms.dirt_big_wall, 769, 0]]

        portal = [[platforms.portal_snow, 700, 380]]

        himesama = [[platforms.himesama_blonde, 450, 385]]

        text_himesama = [[platforms.text_himesama, 450, 340]]

        for platform in intro:
            block = platforms.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # for NPC
        for platform in himesama:
            kiss_himesama = platforms.Platform_NPC(platform[0])
            kiss_himesama.rect.x = platform[1]
            kiss_himesama.rect.y = platform[2]
            kiss_himesama.player = self.player
            self.himesama_list.add(kiss_himesama)

        for platform in text_himesama:
            gate = platforms.Platform_NPC(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.himesama_list.add(gate)
