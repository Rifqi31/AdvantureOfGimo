# name file: levels.py
# python version 3

# import pygame module
import pygame
# import constants variable
import constants

class Level():

    def __init__(self, player):

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.portal_list = None
        
        self.enemy_list_lv1 = None
        self.enemy_list_lv2 = None
        self.enemy_list_lv3 = None
        self.enemy_list_lv4 = None
        self.enemy_list_lv5 = None
        self.enemy_list_lv6 = None
        self.enemy_list_lv7 = None
        self.enemy_list_lv8 = None
        self.enemy_list_lv9 = None
        self.enemy_list_lv10 = None
        self.enemy_list_lv11 = None
        
        # you will die with it
        self.death_place_list_lv1 = None
        self.death_place_list_lv2 = None
        self.death_place_list_lv3 = None
        self.death_place_list_lv4 = None
        self.death_place_list_lv5 = None
        self.death_place_list_lv6 = None
        self.death_place_list_lv7 = None
        self.death_place_list_lv8 = None
        self.death_place_list_lv9 = None
        self.death_place_list_lv10 = None
        self.death_place_list_lv11 = None
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

        # sprite content for katakana
        # basic vocal
        self.katakana_A = None
        self.katakana_I = None
        self.katakana_U = None
        self.katakana_E = None
        self.katakana_O = None

        # Vocal K
        self.katakana_KA = None
        self.katakana_KI = None
        self.katakana_KU = None
        self.katakana_KE = None
        self.katakana_KO = None

        # Vocal S
        self.katakana_SA = None
        self.katakana_SI = None
        self.katakana_SU = None
        self.katakana_SE = None
        self.katakana_SO = None

        # Vocal T
        self.katakana_TA = None
        self.katakana_TI = None
        self.katakana_TU = None
        self.katakana_TE = None
        self.katakana_TO = None

        # Vocal N
        self.katakana_NA = None
        self.katakana_NI = None
        self.katakana_NU = None
        self.katakana_NE = None
        self.katakana_NO = None

        # Vocal H
        self.katakana_HA = None
        self.katakana_HI = None
        self.katakana_HU = None
        self.katakana_HE = None
        self.katakana_HO = None

        # Vocal M
        self.katakana_MA = None
        self.katakana_MI = None
        self.katakana_MU = None
        self.katakana_ME = None
        self.katakana_MO = None

        # Vocal Y
        self.katakana_YA = None
        self.katakana_YU = None
        self.katakana_YO = None

        # Vocal R
        self.katakana_RA = None
        self.katakana_RI = None
        self.katakana_RU = None
        self.katakana_RE = None
        self.katakana_RO = None

        # Vocal W
        self.katakana_WA = None
        self.katakana_WO = None

        # Vocal N
        self.katakana_N = None

        # for fix bug point
        # prototype
        self.special_enemy_list_A_lv2 = None
        self.special_enemy_list_I_lv2 = None
        self.special_enemy_list_U_lv2 = None

        self.katakana_A_lv2 = None
        self.katakana_I_lv2 = None
        self.katakana_U_lv2 = None

        self.katakana_KA_lv3 = None
        self.katakana_KI_lv3 = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.platform_list = pygame.sprite.Group()
        self.portal_list = pygame.sprite.Group()

        self.enemy_list_lv1 = pygame.sprite.Group()
        self.enemy_list_lv2 = pygame.sprite.Group()
        self.enemy_list_lv3 = pygame.sprite.Group()
        self.enemy_list_lv4 = pygame.sprite.Group()
        self.enemy_list_lv5 = pygame.sprite.Group()
        self.enemy_list_lv6 = pygame.sprite.Group()
        self.enemy_list_lv7 = pygame.sprite.Group()
        self.enemy_list_lv8 = pygame.sprite.Group()
        self.enemy_list_lv9 = pygame.sprite.Group()
        self.enemy_list_lv10 = pygame.sprite.Group()
        self.enemy_list_lv11 = pygame.sprite.Group()

        # you will die with it
        self.death_place_list_lv1 = pygame.sprite.Group()
        self.death_place_list_lv2 = pygame.sprite.Group()
        self.death_place_list_lv3 = pygame.sprite.Group()
        self.death_place_list_lv4 = pygame.sprite.Group()
        self.death_place_list_lv5 = pygame.sprite.Group()
        self.death_place_list_lv6 = pygame.sprite.Group()
        self.death_place_list_lv7 = pygame.sprite.Group()
        self.death_place_list_lv8 = pygame.sprite.Group()
        self.death_place_list_lv9 = pygame.sprite.Group()
        self.death_place_list_lv10 = pygame.sprite.Group()
        self.death_place_list_lv11 = pygame.sprite.Group()



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

        # group sprite for katakana
        # Basic Vokal
        self.katakana_A = pygame.sprite.Group()
        self.katakana_I = pygame.sprite.Group()
        self.katakana_U = pygame.sprite.Group()
        self.katakana_E = pygame.sprite.Group()
        self.katakana_O = pygame.sprite.Group()

        # Vocal K
        self.katakana_KA = pygame.sprite.Group()
        self.katakana_KI = pygame.sprite.Group()
        self.katakana_KU = pygame.sprite.Group()
        self.katakana_KE = pygame.sprite.Group()
        self.katakana_KO = pygame.sprite.Group()

        # Vocal S
        self.katakana_SA = pygame.sprite.Group()
        self.katakana_SI = pygame.sprite.Group()
        self.katakana_SU = pygame.sprite.Group()
        self.katakana_SE = pygame.sprite.Group()
        self.katakana_SO = pygame.sprite.Group()

        # Vocal T
        self.katakana_TA = pygame.sprite.Group()
        self.katakana_TI = pygame.sprite.Group()
        self.katakana_TU = pygame.sprite.Group()
        self.katakana_TE = pygame.sprite.Group()
        self.katakana_TO = pygame.sprite.Group()

        # Vocal N
        self.katakana_NA = pygame.sprite.Group()
        self.katakana_NI = pygame.sprite.Group()
        self.katakana_NU = pygame.sprite.Group()
        self.katakana_NE = pygame.sprite.Group()
        self.katakana_NO = pygame.sprite.Group()

        # Vocal H
        self.katakana_HA = pygame.sprite.Group()
        self.katakana_HI = pygame.sprite.Group()
        self.katakana_HU = pygame.sprite.Group()
        self.katakana_HE = pygame.sprite.Group()
        self.katakana_HO = pygame.sprite.Group()

        # Vocal M
        self.katakana_MA = pygame.sprite.Group()
        self.katakana_MI = pygame.sprite.Group()
        self.katakana_MU = pygame.sprite.Group()
        self.katakana_ME = pygame.sprite.Group()
        self.katakana_MO = pygame.sprite.Group()

        # Vocal Y
        self.katakana_YA = pygame.sprite.Group()
        self.katakana_YU = pygame.sprite.Group()
        self.katakana_YO = pygame.sprite.Group()

        # Vocal R
        self.katakana_RA = pygame.sprite.Group()
        self.katakana_RI = pygame.sprite.Group()
        self.katakana_RU = pygame.sprite.Group()
        self.katakana_RE = pygame.sprite.Group()
        self.katakana_RO = pygame.sprite.Group()

        # Vocal W
        self.katakana_WA = pygame.sprite.Group()
        self.katakana_WO = pygame.sprite.Group()

        # Vocal N
        self.katakana_N = pygame.sprite.Group()

        # for fix bug
        self.special_enemy_list_A_lv2 = pygame.sprite.Group()
        self.special_enemy_list_I_lv2 = pygame.sprite.Group()
        self.special_enemy_list_U_lv2 = pygame.sprite.Group()

        self.katakana_A_lv2 = pygame.sprite.Group()
        self.katakana_I_lv2 = pygame.sprite.Group()
        self.katakana_U_lv2 = pygame.sprite.Group()

        self.katakana_KA_lv3 = pygame.sprite.Group()
        self.katakana_KI_lv3 = pygame.sprite.Group()

        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.portal_list.update()
        
        # you will die with it
        self.death_place_list_lv1.update()
        self.death_place_list_lv2.update()
        self.death_place_list_lv3.update()
        self.death_place_list_lv4.update()
        self.death_place_list_lv5.update()
        self.death_place_list_lv6.update()
        self.death_place_list_lv7.update()
        self.death_place_list_lv8.update()
        self.death_place_list_lv9.update()
        self.death_place_list_lv10.update()
        self.death_place_list_lv11.update()

        self.enemy_list_lv1.update()
        self.enemy_list_lv2.update()
        self.enemy_list_lv3.update()
        self.enemy_list_lv4.update()
        self.enemy_list_lv5.update()
        self.enemy_list_lv6.update()
        self.enemy_list_lv7.update()
        self.enemy_list_lv8.update()
        self.enemy_list_lv9.update()
        self.enemy_list_lv10.update()
        self.enemy_list_lv11.update()


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

        # for update sprites katakana
        # Basic Vocal
        self.katakana_A.update()
        self.katakana_I.update()
        self.katakana_U.update()
        self.katakana_E.update()
        self.katakana_O.update()

        # Vocal K
        self.katakana_KA.update()
        self.katakana_KI.update()
        self.katakana_KU.update()
        self.katakana_KE.update()
        self.katakana_KO.update()

        # Vocal S
        self.katakana_SA.update()
        self.katakana_SI.update()
        self.katakana_SU.update()
        self.katakana_SE.update()
        self.katakana_SO.update()

        # Vocal T
        self.katakana_TA.update()
        self.katakana_TI.update()
        self.katakana_TU.update()
        self.katakana_TE.update()
        self.katakana_TO.update()

        # Vocal N
        self.katakana_NA.update()
        self.katakana_NI.update()
        self.katakana_NU.update()
        self.katakana_NE.update()
        self.katakana_NO.update()

        # Vocal H
        self.katakana_HA.update()
        self.katakana_HI.update()
        self.katakana_HU.update()
        self.katakana_HE.update()
        self.katakana_HO.update()

        # Vocal M
        self.katakana_MA.update()
        self.katakana_MI.update()
        self.katakana_MU.update()
        self.katakana_ME.update()
        self.katakana_MO.update()

        # Vocal Y
        self.katakana_YA.update()
        self.katakana_YU.update()
        self.katakana_YO.update()

        # Vocal R
        self.katakana_RA.update()
        self.katakana_RI.update()
        self.katakana_RU.update()
        self.katakana_RE.update()
        self.katakana_RO.update()

        # Vocal W
        self.katakana_WA.update()
        self.katakana_WO.update()

        # Vocal N
        self.katakana_N.update()

        # for fix bug point
        self.special_enemy_list_A.update()
        self.special_enemy_list_I.update()
        self.special_enemy_list_U.update()

        self.katakana_A_lv2.update()
        self.katakana_I_lv2.update()
        self.katakana_U_lv2.update()

        self.katakana_KA_lv3.update()
        self.katakana_KI_lv3.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.portal_list.draw(screen)

        # you will die with it
        self.death_place_list_lv1.draw(screen)
        self.death_place_list_lv2.draw(screen)
        self.death_place_list_lv3.draw(screen)
        self.death_place_list_lv4.draw(screen)
        self.death_place_list_lv5.draw(screen)
        self.death_place_list_lv6.draw(screen)
        self.death_place_list_lv7.draw(screen)
        self.death_place_list_lv8.draw(screen)
        self.death_place_list_lv9.draw(screen)
        self.death_place_list_lv10.draw(screen)
        self.death_place_list_lv11.draw(screen)

        self.enemy_list_lv1.draw(screen)
        self.enemy_list_lv2.draw(screen)
        self.enemy_list_lv3.draw(screen)
        self.enemy_list_lv4.draw(screen)
        self.enemy_list_lv5.draw(screen)
        self.enemy_list_lv6.draw(screen)
        self.enemy_list_lv7.draw(screen)
        self.enemy_list_lv8.draw(screen)
        self.enemy_list_lv9.draw(screen)
        self.enemy_list_lv10.draw(screen)
        self.enemy_list_lv11.draw(screen)
        
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

        # for katakana sprites
        # Basic Vocal
        self.katakana_A.draw(screen)
        self.katakana_I.draw(screen)
        self.katakana_U.draw(screen)
        self.katakana_E.draw(screen)
        self.katakana_O.draw(screen)

        # Vocal K
        self.katakana_KA.draw(screen)
        self.katakana_KI.draw(screen)
        self.katakana_KU.draw(screen)
        self.katakana_KE.draw(screen)
        self.katakana_KO.draw(screen)

        # Vocal S
        self.katakana_SA.draw(screen)
        self.katakana_SI.draw(screen)
        self.katakana_SU.draw(screen)
        self.katakana_SE.draw(screen)
        self.katakana_SO.draw(screen)

        # Vocal T
        self.katakana_TA.draw(screen)
        self.katakana_TI.draw(screen)
        self.katakana_TU.draw(screen)
        self.katakana_TE.draw(screen)
        self.katakana_TO.draw(screen)

        # Vocal N
        self.katakana_NA.draw(screen)
        self.katakana_NI.draw(screen)
        self.katakana_NU.draw(screen)
        self.katakana_NE.draw(screen)
        self.katakana_NO.draw(screen)

        # Vocal H
        self.katakana_HA.draw(screen)
        self.katakana_HI.draw(screen)
        self.katakana_HU.draw(screen)
        self.katakana_HE.draw(screen)
        self.katakana_HO.draw(screen)

        # Vocal M
        self.katakana_MA.draw(screen)
        self.katakana_MI.draw(screen)
        self.katakana_MU.draw(screen)
        self.katakana_ME.draw(screen)
        self.katakana_MO.draw(screen)

        # Vocal Y
        self.katakana_YA.draw(screen)
        self.katakana_YU.draw(screen)
        self.katakana_YO.draw(screen)

        # Vocal R
        self.katakana_RA.draw(screen)
        self.katakana_RI.draw(screen)
        self.katakana_RU.draw(screen)
        self.katakana_RE.draw(screen)
        self.katakana_RO.draw(screen)

        # Vocal W
        self.katakana_WA.draw(screen)
        self.katakana_WO.draw(screen)

        # Vocal N
        self.katakana_N.draw(screen)

        # for fix bug point
        self.special_enemy_list_A_lv2.draw(screen)
        self.special_enemy_list_I_lv2.draw(screen)
        self.special_enemy_list_U_lv2.draw(screen)

        self.katakana_A_lv2.draw(screen)
        self.katakana_I_lv2.draw(screen)
        self.katakana_U_lv2.draw(screen)

        self.katakana_KA_lv3.draw(screen)
        self.katakana_KI_lv3.draw(screen)

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

        # you will die with it
        for platform in self.death_place_list_lv1:
            platform.rect.x += shift_x
        
        for platform in self.death_place_list_lv2:
            platform.rect.x += shift_x
        
        for platform in self.death_place_list_lv3:
            platform.rect.x += shift_x

        for platform in self.death_place_list_lv4:
            platform.rect.x += shift_x

        for platform in self.death_place_list_lv5:
            platform.rect.x += shift_x

        for platform in self.death_place_list_lv6:
            platform.rect.x += shift_x

        for platform in self.death_place_list_lv7:
            platform.rect.x += shift_x

        for platform in self.death_place_list_lv8:
            platform.rect.x += shift_x
        
        for platform in self.death_place_list_lv9:
            platform.rect.x += shift_x
        
        for platform in self.death_place_list_lv10:
            platform.rect.x += shift_x

        for platform in self.death_place_list_lv11:
            platform.rect.x += shift_x

        for platform in self.love_restore_health:
            platform.rect.x += shift_x

        # for katakana sprites
        # Basic Vocal

        for platform in self.katakana_A:
            platform.rect.x += shift_x

        for platform in self.katakana_I:
            platform.rect.x += shift_x

        for platform in self.katakana_U:
            platform.rect.x += shift_x

        for platform in self.katakana_E:
            platform.rect.x += shift_x

        for platform in self.katakana_O:
            platform.rect.x += shift_x

        # Vocal K
        for platform in self.katakana_KA:
            platform.rect.x += shift_x

        for platform in self.katakana_KI:
            platform.rect.x += shift_x

        for platform in self.katakana_KU:
            platform.rect.x += shift_x

        for platform in self.katakana_KE:
            platform.rect.x += shift_x

        for platform in self.katakana_KO:
            platform.rect.x += shift_x

        # Vocal S
        for platform in self.katakana_SA:
            platform.rect.x += shift_x

        for platform in self.katakana_SI:
            platform.rect.x += shift_x

        for platform in self.katakana_SU:
            platform.rect.x += shift_x

        for platform in self.katakana_SE:
            platform.rect.x += shift_x

        for platform in self.katakana_SO:
            platform.rect.x += shift_x

        # Vocal T
        for platform in self.katakana_TA:
            platform.rect.x += shift_x

        for platform in self.katakana_TI:
            platform.rect.x += shift_x

        for platform in self.katakana_TU:
            platform.rect.x += shift_x

        for platform in self.katakana_TE:
            platform.rect.x += shift_x

        for platform in self.katakana_TO:
            platform.rect.x += shift_x

        # Vocal N
        for platform in self.katakana_NA:
            platform.rect.x += shift_x

        for platform in self.katakana_NI:
            platform.rect.x += shift_x

        for platform in self.katakana_NU:
            platform.rect.x += shift_x

        for platform in self.katakana_NE:
            platform.rect.x += shift_x

        for platform in self.katakana_NO:
            platform.rect.x += shift_x

        # Vocal H
        for platform in self.katakana_HA:
            platform.rect.x += shift_x

        for platform in self.katakana_HI:
            platform.rect.x += shift_x

        for platform in self.katakana_HU:
            platform.rect.x += shift_x

        for platform in self.katakana_HE:
            platform.rect.x += shift_x

        for platform in self.katakana_HO:
            platform.rect.x += shift_x

        # Vocal M
        for platform in self.katakana_MA:
            platform.rect.x += shift_x

        for platform in self.katakana_MI:
            platform.rect.x += shift_x

        for platform in self.katakana_MU:
            platform.rect.x += shift_x

        for platform in self.katakana_ME:
            platform.rect.x += shift_x

        for platform in self.katakana_MO:
            platform.rect.x += shift_x

        # Vocal Y
        for platform in self.katakana_YA:
            platform.rect.x += shift_x

        for platform in self.katakana_YU:
            platform.rect.x += shift_x

        for platform in self.katakana_YO:
            platform.rect.x += shift_x

        # Vocal R
        for platform in self.katakana_RA:
            platform.rect.x += shift_x

        for platform in self.katakana_RI:
            platform.rect.x += shift_x

        for platform in self.katakana_RU:
            platform.rect.x += shift_x

        for platform in self.katakana_RE:
            platform.rect.x += shift_x

        for platform in self.katakana_RO:
            platform.rect.x += shift_x

        # Vocal W
        for platform in self.katakana_WA:
            platform.rect.x += shift_x

        for platform in self.katakana_WO:
            platform.rect.x += shift_x

        # Vocal N
        for platform in self.katakana_N:
            platform.rect.x += shift_x

        # for fix bug point
        for platform in self.special_enemy_list_A_lv2:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_I_lv2:
            platform.rect.x += shift_x

        for platform in self.special_enemy_list_U_lv2:
            platform.rect.x += shift_x

        for platform in self.katakana_A_lv2:
            platform.rect.x += shift_x

        for platform in self.katakana_I_lv2:
            platform.rect.x += shift_x

        for platform in self.katakana_U_lv2:
            platform.rect.x += shift_x

        for platform in self.katakana_KA_lv3:
            platform.rect.x += shift_x

        for platform in self.katakana_KI_lv3:
            platform.rect.x += shift_x

        # enemy
        for platform in self.enemy_list_lv1:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv2:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv3:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv4:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv5:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv6:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv7:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv8:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv9:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv10:
            platform.rect.x += shift_x
        
        for platform in self.enemy_list_lv11:
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