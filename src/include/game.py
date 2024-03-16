import pygame
from pygame.locals import *
from include.character import Character
from include.media import MediaPath
from include.sprite import *

class Game:
    def __init__(self):
        pygame.init()

        self.largeur, self.hauteur = 1920, 1080
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))

        self.NOIR = (0, 0, 0)

        self.character = Character(self.fenetre)

        self.sprites = pygame.sprite.Group()
        self.add_sprite(MediaPath.door, (500, 500))

        # Charger l'arrière-plan et le redimensionner
        self.background = pygame.image.load(MediaPath.bg).convert()
        self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))

    def add_sprite(self, image_path, position):
        sprite = Sprite(image_path, position)
        self.sprites.add(sprite)

    def run(self):
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == QUIT:
                    en_cours = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        en_cours = False

            keys = pygame.key.get_pressed()
            self.character.update(keys)

            # Afficher l'arrière-plan
            self.fenetre.blit(self.background, (0, 0))

            # Dessiner les autres éléments du jeu
            self.character.draw()
            self.sprites.draw(self.fenetre)

            pygame.display.flip()

        pygame.quit()