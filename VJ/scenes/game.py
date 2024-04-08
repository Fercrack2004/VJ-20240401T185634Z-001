import pygame
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
deadmenu=pygame.image.load("VJ/assets/deadjorge.png")
pygame.display.set_caption("Jorge The Game")
lol=0
def muerte(screen):
    pygame.mixer.music.pause()

    restart = pygame.image.load('VJ/assets/restart.png').convert_alpha()
    restartbuttom = Boton(500, 300, pygame.transform.scale(restart,(100,700)),1)
    backtomenu = pygame.image.load('VJ/assets/backmenu.png').convert_alpha()
    backtomenubuttom = Boton(500, 450, pygame.transform.scale(backtomenu,(100,700)),1)

    run = True

    while run:
        screen.blit(deadmenu, [0, 0])


        if restartbuttom.draw(screen):
            return True
        if backtomenubuttom.draw(screen):
            return False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                return pygame.quit()
        
        pygame.display.update()
        

def StartScene(lol):
    ''' iniciamos los modulos de pygame'''
    pygame.display.set_caption("Jorge The Game")
    
    # Cargar y reproducir la música del menú
    pygame.mixer.music.load("VJ/assets/musicgoofyass/Quando.wav")
    pygame.mixer.music.play(-1)

    pausado = True
    cual_menu = "main"
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

    jorge = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    jorge_group = pygame.sprite.Group()
    jorge_group.add(jorge)

    clock = pygame.time.Clock()
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    
    puntaje = 0
    font = pygame.font.Font('freesansbold.ttf', 32)


    running = True
    while running: 
        if pausado == True:
            screen.blit(menuback, [0,0])
            if cual_menu == "main":
                if lol==1:
                    pausado = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("VJ/assets/musicgoofyass/vordt.wav")
                    pygame.mixer.music.play(-1)
                    all_sprites.add(player)
                if start_boton.draw(screen):
                    pausado = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("VJ/assets/musicgoofyass/vordt.wav")
                    pygame.mixer.music.play(-1)
                    all_sprites.add(player)
                if lore_boton.draw(screen):
                    cual_menu = "lore"
                if quitboton.draw(screen):
                    running = False
            if cual_menu == "lore":
                screen.blit(sobrevive_img,(sobrevive_rect))
                if atras_boton.draw(screen):
                    cual_menu = "main"
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
                    
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = True
    
            if event.type == pygame.QUIT:
                running = False
        screen.blit(font.render(str(puntaje), True, (255,255,255), (0,0,0)), (0,0)) 
        for entity in all_sprites:
            if isinstance(entity, Player):
                screen.blit(entity.surf, entity.rect)
                pressed_keys = pygame.key.get_pressed()
                entity.update(pressed_keys)
                entity.mask = pygame.mask.from_surface(entity.surf)
            elif isinstance(entity, Enemy):
                screen.blit(entity.image, entity.rect)
                entity.mask = pygame.mask.from_surface(entity.image)
        for entity in enemies:
            score = entity.update()
            puntaje += score
        if pygame.sprite.spritecollide(player, enemies, False):
            if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
                player.kill()
                death = muerte(screen)
                if death == True:
                    lol=1
                    StartScene(lol)
                    running=False
                elif death == False:
                    lol=0
                    StartScene(lol)
                    running=False
    

        clock.tick(40)

        pygame.display.flip()

  

    



  