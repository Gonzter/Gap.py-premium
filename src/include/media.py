import pygame

class ImgPath :
    bg = "assets/images/background.png"
    door = "assets/images/door.png"
    seb = "assets/images/seb.png"

class AudioPath :
    main_music = "assets/music/rpg_title.ogg"
    jump = "assets/music/cartoon_jump.ogg"

class Music:
    def runMusic(playlist, volume:float=1.0):
        if (isinstance(playlist, str)):
            pygame.mixer.music.load(playlist)
            pygame.mixer.music.play(loops=-1)
        elif (isinstance(playlist, list)):
            for item in playlist:
                pygame.music.mixer.queue(item)

    def createSound(path:str, volume:float=1.0):
        try:
            newSound = pygame.mixer.Sound(path)
            newSound.set_volume(volume)
            return newSound
        except Exception as error:
            print(error)

    def runSound(sound):
        try:
            sound.play()
        except Exception as error:
            print(error)
