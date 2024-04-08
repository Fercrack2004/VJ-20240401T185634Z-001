'''import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)
from elements.jorge import Player
from elements.bug import Enemy
from elements.botones import Boton
from elements.bbullet import Bullet
pygame.init() 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("VJ/assets/pixelBackground.jpg").convert()
menuback=pygame.image.load("VJ/assets/jorgemenu.png").convert()
deadmenu=pygame.image.load("VJ/assets/deadjorge.png").convert()
pygame.display.set_caption("Jorge The Game")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def mainmenu():
    pausado = True
    cual_menu = "main"
    pygame.mixer.music.load("VJ/assets/musicgoofyass/Quando.wav")
    pygame.mixer.music.play(-1)
    start_img = pygame.image.load("VJ/assets/startmedieval.png").convert_alpha()
    lore_img = pygame.image.load("VJ/assets/lorelol.png").convert_alpha()
    sobrevive_img = pygame.image.load("VJ/assets/papiro.png")
    imagen_atras = pygame.image.load("VJ/assets/back.png").convert_alpha()
    quitimg=pygame.image.load("VJ/assets/quit.png").convert_alpha()
    sobrevive_rect = sobrevive_img.get_rect(topleft=(0,0))
    start_boton = Boton(336,375,pygame.transform.scale(start_img,(100,700)),1)
    lore_boton = Boton(336,500,pygame.transform.scale(lore_img,(100,700)),1)
    quitboton=Boton(336,625,pygame.transform.scale(quitimg,(100,700)),1)
    atras_boton = Boton(200,400,pygame.transform.scale(imagen_atras,(100,700)),1)
    running=True
    while running:
        if pausado == True:
            screen.blit(menuback, [0,0])
            if cual_menu == "main":
                if start_boton.draw(screen):
                    pausado = False
                    pygame.mixer.music.stop()
                    StartScene(screen)
                if lore_boton.draw(screen):
                    cual_menu = "lore"
                if quitboton.draw(screen):
                    running = False
            if cual_menu == "lore":
                screen.blit(sobrevive_img,(sobrevive_rect))
                if atras_boton.draw(screen):
                    cual_menu = "main"
        if pausado == False:
            screen.blit(background_image, [0, 0])'''