import pygame
from pygame.locals import *
from include.sprite import *
from include.character import Character
from include.media import AudioPath, ImgPath, Music

class Coord:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1920, 1080
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Gap.py Premium")
        self.character = Character(self.window)
        self.sprites = pygame.sprite.Group()
        self.add_sprite(ImgPath.door, (500, 500))
        self.font = pygame.font.Font(None, 36)

    def add_sprite(self, image_path, position):
        sprite = Sprite(image_path, position)
        self.sprites.add(sprite)

    def new_button(self, text, size:Coord, height):
        new_button = pygame.Rect((self.width - size.x) // 2, height, size.x, size.y)
        pygame.draw.rect(self.window, (220,20,60), (new_button.x, new_button.y, size.x, size.y))
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (new_button.x + size.x // 2, new_button.y + size.y // 2)
        self.window.blit(text_surface, text_rect)
        return new_button

    def main_menu(self):
        # create and display background
        self.background = pygame.image.load(ImgPath.menu).convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.window.blit(self.background, (0, 0))
        #create buttons
        button_size = Coord(200,50)
        play_button = self.new_button("Play", button_size, 500)
        settings_button_rect = self.new_button("Settings", button_size, 600)
        quit_button_rect = self.new_button("Quit", button_size, 700)
        #display loop
        display = True
        while (display):
            for event in pygame.event.get():
                if event.type == QUIT:
                    display = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        display = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button.collidepoint(mouse_pos):
                        self.run()
                        display = False
                    elif settings_button_rect.collidepoint(mouse_pos):
                        print("Settings button clicked")
                    elif quit_button_rect.collidepoint(mouse_pos):
                        display = False
            if (display):
                pygame.display.flip()
        pygame.quit()

    def run(self):
        self.camera_x = 0
        self.background = pygame.image.load(ImgPath.bg).convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.background_width = self.background.get_width()
        display = True
        Music.runMusic(AudioPath.main_music)
        while 42:
            for event in pygame.event.get():
                if event.type == QUIT:
                    display = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        display = False
            if (display == False):
                break
            keys = pygame.key.get_pressed()
            # move map
            if keys[K_LEFT] or keys[K_q]:
                self.camera_x += self.character.vitesse_x
            elif keys[K_RIGHT] or keys[K_d]:
                self.camera_x -= self.character.vitesse_x
            # display background
            self.window.blit(self.background, (self.camera_x % self.background_width - self.background_width, 0))
            self.window.blit(self.background, (self.camera_x % self.background_width, 0))
            self.window.blit(self.background, (self.camera_x % self.background_width + self.background_width, 0))

            # Mise à jour du personnage
            self.character.update(keys)
            self.character.draw()

            pygame.display.flip()

        pygame.quit()