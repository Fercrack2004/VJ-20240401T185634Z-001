'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame
pygame.init() 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("VJ/assets/pixelBackground.jpg").convert()

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy
from elements.botones import Boton
from elements.bbullet import Bullet
pygame.display.set_caption("Jorge The Game")


def StartScene():
    ''' iniciamos los modulos de pygame'''
 # Inicializar Pygame aquí

    pygame.display.set_caption("Jorge The Game")

     #Menu#
    pausado = True
    cual_menu = "main"
    start_img = pygame.image.load("VJ/assets/start_paint.png").convert_alpha()
    lore_img = pygame.image.load("VJ/assets/Lore.png").convert_alpha()
    sobrevive_img = pygame.image.load("VJ/assets/sobrevive2.png")
    imagen_atras = pygame.image.load("VJ/assets/atras.png").convert_alpha()
    sobrevive_rect = sobrevive_img.get_rect(topleft=(0,0))
    start_boton = Boton(304,125,start_img,1)
    lore_boton = Boton(336,375,lore_img,1)
    atras_boton = Boton(336,400,imagen_atras,1)

    jorge = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    jorge_group = pygame.sprite.Group()
    jorge_group.add(jorge)

    

    clock = pygame.time.Clock()
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True
    while running: 
        if pausado == False:
            screen.blit(background_image, [0, 0])

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
                elif event.type == ADDENEMY:
                    new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
        if pausado == True:
            screen.fill((52,78,91))
            if cual_menu == "main":

                if start_boton.draw(screen):
                    pausado = False
                if lore_boton.draw(screen):
                    cual_menu = "lore"

            if cual_menu == "lore":
                screen.blit(sobrevive_img,(sobrevive_rect))
                if atras_boton.draw(screen):
                    cual_menu = "main"
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = True
    
        if event.type == pygame.QUIT:
            break
        for entity in all_sprites:
            if isinstance(entity, Player):
                screen.blit(entity.surf, entity.rect)
                pressed_keys = pygame.key.get_pressed()
                entity.update(pressed_keys)
                entity.mask = pygame.mask.from_surface(entity.surf)
            elif isinstance(entity, Enemy):
                screen.blit(entity.image, entity.rect)
                entity.mask = pygame.mask.from_surface(entity.image)



        if pygame.sprite.spritecollide(player, enemies, False):
            if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
                player.kill()
                running = False

        clock.tick(40)
        enemies.update()
        pygame.display.flip()

        pygame.display.update()




  