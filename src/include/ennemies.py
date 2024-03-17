import pygame
from include.media import ImgPath

class Ennemy:
    def __init__(self):
        print("Nothing to see here")

class Slime(Ennemy):
    def __init__(self, sprite_path:str):
        sprite_sheet = pygame.image.load(ImgPath.slime)
        self.size = 24
        self.tiles = {
            "up": [],
            "down": [],
            "side": []
        }
        for i, dir in enumerate(self.tiles, start=1):
            for j in range(4, start=1):
                self.tiles[dir].append(pygame.Surface((j * self.size, i * self.size)))
        print("Slime")
