# file name : configsounds.py
# python version 3

# import pygame module
import pygame

# intialize
pygame.init()

# for music
background_music = pygame.mixer.Sound("sounds/01_Invitation.ogg")
ending_music = pygame.mixer.Sound("sounds/05_Thought_Soup.ogg")

# for SFX
menu_sfx = pygame.mixer.Sound("sounds/menu_sfx.wav")
push_button_sfx = pygame.mixer.Sound("sounds/push_button_sfx.wav")
jump_sfx = pygame.mixer.Sound("sounds/jump_sfx.wav")
game_over_sfx = pygame.mixer.Sound("sounds/game_over_sfx.wav")
coin_sfx = pygame.mixer.Sound("sounds/mattix_8bit-coin.wav")
magic_sfx = pygame.mixer.Sound("sounds/8bit-laser-shot.wav")
ouch_sfx = pygame.mixer.Sound("sounds/ouch_sfx.wav")
portal_sfx = pygame.mixer.Sound("sounds/retro-accomplished-sfx.wav")
denied_sfx = pygame.mixer.Sound("sounds/suntemple_access-denied.wav")

# for SFX hiragana/katakana
# vocal
effect_a = pygame.mixer.Sound("sounds/a.wav")
effect_i = pygame.mixer.Sound("sounds/i.wav")
effect_u = pygame.mixer.Sound("sounds/u.wav")
effect_e = pygame.mixer.Sound("sounds/e.wav")
effect_o = pygame.mixer.Sound("sounds/o.wav")
# vocal k
effect_ka = pygame.mixer.Sound("sounds/ka.wav")
effect_ki = pygame.mixer.Sound("sounds/ki.wav")
effect_ku = pygame.mixer.Sound("sounds/ku.wav")
effect_ke = pygame.mixer.Sound("sounds/ke.wav")
effect_ko = pygame.mixer.Sound("sounds/ko.wav")
# vocal s
effect_sa = pygame.mixer.Sound("sounds/sa.wav")
effect_shi = pygame.mixer.Sound("sounds/shi.wav")
effect_su = pygame.mixer.Sound("sounds/su.wav")
effect_se = pygame.mixer.Sound("sounds/se.wav")
effect_so = pygame.mixer.Sound("sounds/so.wav")
# vocal t
effect_ta = pygame.mixer.Sound("sounds/ta.wav")
effect_chi = pygame.mixer.Sound("sounds/chi.wav")
effect_tsu = pygame.mixer.Sound("sounds/tsu.wav")
effect_te = pygame.mixer.Sound("sounds/te.wav")
effect_to = pygame.mixer.Sound("sounds/to.wav")
# vocal n
effect_na = pygame.mixer.Sound("sounds/na.wav")
effect_ni = pygame.mixer.Sound("sounds/ni.wav")
effect_nu = pygame.mixer.Sound("sounds/nu.wav")
effect_ne = pygame.mixer.Sound("sounds/ne.wav")
effect_no = pygame.mixer.Sound("sounds/no.wav")
# vocal h
effect_ha = pygame.mixer.Sound("sounds/ha.wav")
effect_hi = pygame.mixer.Sound("sounds/hi.wav")
effect_fu = pygame.mixer.Sound("sounds/fu.wav")
effect_he = pygame.mixer.Sound("sounds/he.wav")
effect_ho = pygame.mixer.Sound("sounds/ho.wav")
# vocal m
effect_ma = pygame.mixer.Sound("sounds/ma.wav")
effect_mi = pygame.mixer.Sound("sounds/mi.wav")
effect_mu = pygame.mixer.Sound("sounds/mu.wav")
effect_me = pygame.mixer.Sound("sounds/me.wav")
effect_mo = pygame.mixer.Sound("sounds/mo.wav")
# vocal y
effect_ya = pygame.mixer.Sound("sounds/ya.wav")
effect_yu = pygame.mixer.Sound("sounds/yu.wav")
effect_yo = pygame.mixer.Sound("sounds/yo.wav")
# vocal r
effect_ra = pygame.mixer.Sound("sounds/ra.wav")
effect_ri = pygame.mixer.Sound("sounds/ri.wav")
effect_ru = pygame.mixer.Sound("sounds/ru.wav")
effect_re = pygame.mixer.Sound("sounds/re.wav")
effect_ro = pygame.mixer.Sound("sounds/ro.wav")
# vocal w
effect_wa = pygame.mixer.Sound("sounds/wa.wav")
effect_wo = pygame.mixer.Sound("sounds/o.wav")
# vocal n
effect_n = pygame.mixer.Sound("sounds/n.wav")

# ----- For Sounds Settings -----
def turn_off_sounds():
    """ This function for turn off all sounds """
    pygame.mixer.stop()


def turn_on_sounds():
    """ This function for turn on all sounds """
    background_music.play(-1)
    background_music.set_volume(0.5)
