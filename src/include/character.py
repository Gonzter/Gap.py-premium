import pygame
from include.media import AudioPath, ImgPath, Music
from pygame.locals import *

class Character:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image = pygame.image.load(ImgPath.seb).convert_alpha()
        self.rect = self.image.get_rect()

        self.image_scale_factor = 0.7
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.image_scale_factor), int(self.rect.height * self.image_scale_factor)))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect = self.image.get_rect()
        self.rect.center = (1000, 688)
        self.vitesse_x = 2
        self.vitesse_y = 0
        self.jumpSound = Music.createSound(AudioPath.jump)
        self.isJumping = False
        self.gravite = 0.08

    def update(self, keys):
        if (keys[K_UP] or keys[K_SPACE]) and not self.isJumping:
            self.jump()
        self.jump_handler()

    def jump_handler(self):
        if self.isJumping:
            self.rect.y -= self.vitesse_y
            self.vitesse_y -= self.gravite
            if self.rect.y >= 623:
                self.rect.y = 623
                self.isJumping = False
    def jump(self):
        Music.runSound(self.jumpSound)
        self.isJumping = True
        self.vitesse_y = 8

    def draw(self):
        self.fenetre.blit(self.image, self.rect)
