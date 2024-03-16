import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
