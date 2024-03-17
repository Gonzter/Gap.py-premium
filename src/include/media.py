import pygame

class ImgPath :
    bg = "assets/images/background.png"
    butonFrame = "assets/images/butonFrame.png"
    door = "assets/images/door.png"
    gappy = "assets/images/Gappy.jpg"
    old_man = "assets/images/old_man.png"
    seb = "assets/images/seb.png"
    slime = "assets/images/slime_spritesheet.png"
    menu = "assets/images/menu.png"

class AudioPath :
    collide = "assets/music/slime_jump.wav"
    main_music = "assets/music/rpg_title.ogg"
    main_title = "assets/music/Scarlet_Forest_TubeRipper.cc.ogg"
    jump = "assets/music/cartoon_jump.ogg"

class Fonts :
    default = "assets/font.ttf"

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
