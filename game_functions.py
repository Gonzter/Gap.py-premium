import pygame
from pygame.locals import *

def update_screen(fenetre, couleur_fond, character):
    fenetre.fill(couleur_fond)
    character.draw()
    pygame.display.flip()
