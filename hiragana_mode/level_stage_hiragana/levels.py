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
        self.enemy_list_tutorial = None
        
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
        self.death_place_list_tutorial = None

        # for health point
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

        # sprite content for hiragana
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
        self.enemy_list_tutorial = pygame.sprite.Group()
        
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
        self.death_place_list_tutorial = pygame.sprite.Group()

        # for health point
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

        # group sprite for hiragana
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
        self.death_place_list_tutorial.update()

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
        self.enemy_list_tutorial.update()

        
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

        # for update sprites hiragana
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
        self.death_place_list_tutorial.draw(screen)

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
        self.enemy_list_tutorial.draw(screen)

        # for health restore
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

        # for hiragana sprites
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
        
        for platform in self.death_place_list_tutorial:
            platform.rect.x += shift_x

        # for health restore
        for platform in self.love_restore_health:
            platform.rect.x += shift_x

        # for hiragana sprites
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
        
        for platform in self.enemy_list_tutorial:
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
