import pygame
from include.media import ImgPath

class Ennemy:
    def __init__(self):
        print("Nothing to see here")

class Slime(Ennemy):
    def __init__(self, x, y, speed):
        sprite_sheet = pygame.image.load(ImgPath.slime)
        self.size = 24
        self.tiles = {
            "up": [],
            "side": [],
            "down": []
        }
        self.speed = speed
        for i, dir in enumerate(self.tiles):
            for j in range(3):
                self.tiles[dir].append(sprite_sheet.subsurface(pygame.Rect(j * self.size, i * self.size, self.size, self.size)))
                print("NewSlime", dir , "[" , i , "]" , j)
        self.size = 100
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.cur_sprite = self.tiles["down"][0]
        self.cur_sprite =  pygame.transform.scale(self.cur_sprite, (self.size, self.size))

    def update(self, direction:int, tile_value = 0):
        self.cur_sprite = self.tiles["side"][tile_value]
        if (direction < 0):
            self.cur_sprite = pygame.transform.flip(self.cur_sprite, True, False)
        self.cur_sprite =  pygame.transform.scale(self.cur_sprite, (self.size, self.size))

    def draw(self, window):
        window.blit(self.cur_sprite, self.rect)
