import pygame
from pygame.locals import *
from character import Character

class Game:
    def __init__(self):
        pygame.init()

        self.largeur, self.hauteur = 1920, 1080
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))

        self.camera_x = 0

        self.character = Character(self.fenetre)

        # Charger l'arrière-plan et le redimensionner
        self.background = pygame.image.load("background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))
        self.background_width = self.background.get_width()

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

            # Défilement de la carte
            if keys[K_LEFT] or keys[K_q]:
                self.camera_x += self.character.vitesse_x
            elif keys[K_RIGHT] or keys[K_d]:
                self.camera_x -= self.character.vitesse_x

            # Afficher le fond en boucle
            self.fenetre.blit(self.background, (self.camera_x % self.background_width - self.background_width, 0))
            self.fenetre.blit(self.background, (self.camera_x % self.background_width, 0))
            self.fenetre.blit(self.background, (self.camera_x % self.background_width + self.background_width, 0))

            # Mise à jour du personnage
            self.character.update(keys)

            # Dessiner le personnage à une position fixe sur l'écran
            self.character.draw()

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()



# import pygame
# from pygame.locals import *
# from character import Character

# class Game:
#     def __init__(self):
#         pygame.init()

#         self.largeur, self.hauteur = 1920, 1080
#         self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))

#         self.camera_x = 0

#         self.character = Character(self.fenetre)

#         # Charger l'arrière-plan et le redimensionner
#         self.background = pygame.image.load("background.png").convert()
#         self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))

#         # Dupliquer le fond pour créer un effet de défilement continu
#         self.background_width = self.background.get_width()
#         self.background_duplicated = pygame.Surface((self.background_width * 3, self.hauteur))
#         self.background_duplicated.blit(self.background, (0, 0))
#         self.background_duplicated.blit(self.background, (self.background_width, 0))
#         self.background_duplicated.blit(self.background, (self.background_width * 2, 0))

#     def run(self):
#         en_cours = True
#         while en_cours:
#             for event in pygame.event.get():
#                 if event.type == QUIT:
#                     en_cours = False
#                 elif event.type == KEYDOWN:
#                     if event.key == K_ESCAPE:
#                         en_cours = False

#             keys = pygame.key.get_pressed()

#             # Défilement de la carte
#             if keys[K_LEFT] or keys[K_q]:
#                 self.camera_x += self.character.vitesse_x
#             elif keys[K_RIGHT] or keys[K_d]:
#                 self.camera_x -= self.character.vitesse_x

#             # Afficher la partie appropriée de l'arrière-plan en fonction de la position de la caméra
#             self.fenetre.blit(self.background_duplicated, (self.camera_x % self.background_width - self.background_width, 0))

#             # Dessiner les autres éléments du jeu
#             self.character.draw()

#             pygame.display.flip()

#         pygame.quit()

# if __name__ == "__main__":
#     game = Game()
#     game.run()
