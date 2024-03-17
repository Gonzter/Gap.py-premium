import pygame

class Music:
    def __init__(self, music):
        if (isinstance(music, str)):
            pygame.music.mixer.load(music)
            pygame.music.mixer.play(loops=-1)
        elif (isinstance(music, list)):
            for item in music:
                pygame.music.mixer.queue(item)

    def useSound(path:str):
        try:
            pygame.mixer.Sound(path)
        except Exception as error:
            print(error)