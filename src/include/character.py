import pygame
from include.media import AudioPath, ImgPath, Music
from pygame.locals import *

class Character:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.original_image = pygame.image.load(ImgPath.seb).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()


        self.image_scale_factor = 0.7
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.image_scale_factor), int(self.rect.height * self.image_scale_factor)))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect = self.image.get_rect()
        self.rect.center = (1000, 688)
        self.vitesse_x = 2
        self.saut_en_cours = False
        self.jumpSound = Music.createSound(AudioPath.jump)
        self.gravite = 0.08

    def update(self, keys):
        if keys[K_LEFT] or keys[K_q]:
            self.rect.x -= self.vitesse_x
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.x += self.vitesse_x

        if self.saut_en_cours:
            self.rect.y -= self.vitesse_y
            self.vitesse_y -= self.gravite
            # Limiter le saut à la hauteur de 623
            if self.rect.y >= 623:  # Limite de saut en y
                self.rect.y = 623
                self.saut_en_cours = False

        # Activation du saut si la touche UP ou SPACE est enfoncée et le personnage n'est pas en train de sauter
        if (keys[K_UP] or keys[K_SPACE]) and not self.saut_en_cours:
            self.sauter()

    def sauter(self):
        Music.runSound(self.jumpSound)
        self.saut_en_cours = True
        self.vitesse_y = 8

    def draw(self):
        self.fenetre.blit(self.image, self.rect)  # Dessine le personnage sur la fenêtre
