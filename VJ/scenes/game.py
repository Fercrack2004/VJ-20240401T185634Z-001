import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_SPACE)
from elements.jorge import Player
from elements.bug import (Enemy, explosion_frames)
from elements.rayo import Rayo
from elements.botones import Boton
from elements.bbullet import Bullet
from elements.bala import Bala
from elements.finalboss import FinalBoss

pygame.init() 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("VJ/assets/pixelBackground.jpg").convert()
menuback=pygame.image.load("VJ/assets/jorgemenu.png").convert()
deadmenu=pygame.image.load("VJ/assets/deadjorge.png")
winmenu=pygame.image.load("VJ/assets/jorgewin.png")
pygame.display.set_caption("Jorge The Game")
lol=0
class Explosion(pygame.sprite.Sprite):
    def __init__(self, frames, x, y):
        super().__init__()
        self.frames = frames
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.index += 1
        if self.index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[self.index]
            self.rect = self.image.get_rect(center=self.rect.center)

def muerte(screen):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("VJ/assets/musicgoofyass/besame.wav")
    pygame.mixer.music.play(-1)
    menuclick=pygame.mixer.Sound("VJ/assets/musicgoofyass/mineboton.wav")
    restart = pygame.image.load('VJ/assets/restart.png').convert_alpha()
    restartbuttom = Boton(500, 300, pygame.transform.scale(restart,(100,700)),1)
    backtomenu = pygame.image.load('VJ/assets/backmenu.png').convert_alpha()
    backtomenubuttom = Boton(500, 450, pygame.transform.scale(backtomenu,(100,700)),1)

    run = True

    while run:
        screen.blit(deadmenu, [0, 0])


        if restartbuttom.draw(screen):
            menuclick.play()
            pygame.mixer.music.stop()
            return True
        if backtomenubuttom.draw(screen):
            menuclick.play()
            pygame.mixer.music.stop()
            return False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                return pygame.quit()
        
        pygame.display.update()
def win(screen):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("VJ/assets/musicgoofyass/win.wav")
    pygame.mixer.music.play(-1)
    menuclick=pygame.mixer.Sound("VJ/assets/musicgoofyass/mineboton.wav")
    restart = pygame.image.load('VJ/assets/restart.png').convert_alpha()
    restartbuttom = Boton(500, 300, pygame.transform.scale(restart,(100,700)),1)
    backtomenu = pygame.image.load('VJ/assets/backmenu.png').convert_alpha()
    backtomenubuttom = Boton(500, 450, pygame.transform.scale(backtomenu,(100,700)),1)

    run = True

    while run:
        screen.blit(winmenu, [0, 0])


        if restartbuttom.draw(screen):
            menuclick.play()
            pygame.mixer.music.stop()
            return True
        if backtomenubuttom.draw(screen):
            menuclick.play()
            pygame.mixer.music.stop()
            return False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                return pygame.quit()
        
        pygame.display.update()       

def StartScene(lol):
    ''' iniciamos los modulos de pygame'''
    pygame.display.set_caption("Jorge The Game")
    vidas=3
    # Cargar y reproducir la música del menú
    pygame.mixer.music.load("VJ/assets/musicgoofyass/Quando.wav")
    pygame.mixer.music.play(-1)
    menuclick=pygame.mixer.Sound("VJ/assets/musicgoofyass/mineboton.wav")
    explosionfart=pygame.mixer.Sound("VJ/assets/musicgoofyass/explosion.wav")
    dañosound=pygame.mixer.Sound("VJ/assets/musicgoofyass/oof.wav")
    espada=pygame.mixer.Sound("VJ/assets/musicgoofyass/bow.wav")
    realdead=pygame.mixer.Sound("VJ/assets/musicgoofyass/metalgear.wav")
    nolodiga=pygame.mixer.Sound("VJ/assets/musicgoofyass/nolodiga.wav")
    jefe=pygame.mixer.Sound("VJ/assets/musicgoofyass/jefe.wav")
    pausado = True
    cual_menu = "main"
    corazon_img = pygame.image.load("VJ/assets/cora.png").convert_alpha()
    corazon_img = pygame.transform.scale(corazon_img, (40, 40))
    start_img = pygame.image.load("VJ/assets/startmedieval.png").convert_alpha()
    lore_img = pygame.image.load("VJ/assets/lorelol.png").convert_alpha()
    sobrevive_img = pygame.image.load("VJ/assets/papiro.png")
    objetivo=pygame.image.load("VJ/assets/letreropng.png")
    imagen_atras = pygame.image.load("VJ/assets/back.png").convert_alpha()
    quitimg=pygame.image.load("VJ/assets/quit.png").convert_alpha()
    sobrevive_rect = sobrevive_img.get_rect(topleft=(0,0))
    objetivolol=objetivo.get_rect(topright=(1000,0))
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

    ADDRAYO = pygame.USEREVENT + 10
    pygame.time.set_timer(ADDRAYO, 700)

    ADD_FINAL_BOSS = pygame.USEREVENT + 2
    pygame.time.set_timer(ADD_FINAL_BOSS, 1200)

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemies = pygame.sprite.Group()
    rayos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    explosions = pygame.sprite.Group() 

    final_boss = None
    final_boss_group = pygame.sprite.Group()
    final_boss_created= False
    juegocomenzado=False
    puntaje = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    frame_index=0
    disparo=False
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
                    juegocomenzado=True
                    all_sprites.add(player)
                if start_boton.draw(screen):
                    menuclick.play()
                    pausado = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("VJ/assets/musicgoofyass/vordt.wav")
                    pygame.mixer.music.play(-1)
                    juegocomenzado=True
                    all_sprites.add(player)
                if lore_boton.draw(screen):
                    menuclick.play()
                    cual_menu = "lore"
                if quitboton.draw(screen):
                    menuclick.play()
                    running = False
            if cual_menu == "lore":
                screen.blit(sobrevive_img,(sobrevive_rect))
                screen.blit(objetivo,(objetivolol))
                if atras_boton.draw(screen):
                    menuclick.play()
                    cual_menu = "main"
        if pausado == False:
            screen.blit(background_image, [0, 0])

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key ==K_SPACE:
                        if disparo == False:
                            espada.play()
                            bullet = Bala(player.rect.centerx + 20, player.rect.centery + 2)
                            balas.add(bullet)
                            disparo = True
                elif event.type == QUIT:
                    running = False
                elif event.type == ADDENEMY:
                    new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                elif event.type == ADD_FINAL_BOSS:
                    if puntaje >= 1000 and not final_boss_created:
                        final_boss = FinalBoss(SCREEN_WIDTH, SCREEN_HEIGHT)
                        final_boss_group.add(final_boss)
                        all_sprites.add(final_boss)
                        final_boss_created = True
                        explosion = Explosion(explosion_frames, final_boss.rect.centerx, final_boss.rect.centery)
                        explosions.add(explosion)
                        nolodiga.play()
                elif final_boss_created:
                    if event.type==ADDRAYO:
                        new_rayo = Rayo(SCREEN_WIDTH, SCREEN_HEIGHT)
                        enemies.add(new_rayo)
                        all_sprites.add(new_rayo)
        
        if juegocomenzado:
            corazon_x = SCREEN_WIDTH - 40
            corazon_y = 10
            for i in range(vidas):
                screen.blit(corazon_img, (corazon_x - i * 40, corazon_y))           
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = True
    
            if event.type == pygame.QUIT:
                running = False
        if juegocomenzado:
            screen.blit(font.render(str(puntaje), True, (255,255,255), (0,0,0)), (0,0)) 
        for entity in balas:
            entity.update()
            screen.blit(entity.surf,entity.rect)
            disparo=entity.update()
            
        for entity in all_sprites:
            if isinstance(entity, Player):
                screen.blit(entity.surf, entity.rect)
                pressed_keys = pygame.key.get_pressed()
                entity.update(pressed_keys)
                entity.mask = pygame.mask.from_surface(entity.surf)
            elif isinstance(entity, Enemy):
                screen.blit(entity.image, entity.rect)
                entity.mask = pygame.mask.from_surface(entity.image)
            elif isinstance(entity, Rayo):
                screen.blit(entity.image, entity.rect)
                entity.mask = pygame.mask.from_surface(entity.image)
        for entity in enemies:
            score = entity.update()
            puntaje += score
        collisions = pygame.sprite.groupcollide(balas, enemies, True, True, pygame.sprite.collide_mask)
        for bullet, enemy in collisions.items():
            for hit_enemy in enemy:
                explosion = Explosion(explosion_frames, hit_enemy.rect.centerx, hit_enemy.rect.centery)
                explosions.add(explosion)
                explosionfart.play()  # Agregar la explosión al grupo de explosiones
                puntaje += 100
                disparo = False
        
        collisions_final_boss = pygame.sprite.groupcollide(balas, final_boss_group, True, False, pygame.sprite.collide_mask)
        for bullet, final_boss_list in collisions_final_boss.items():  # Itera sobre las instancias de FinalBoss en final_boss_group
            for final_boss in final_boss_list:
                explosion = Explosion(explosion_frames, final_boss.rect.centerx, final_boss.rect.centery)
                explosions.add(explosion)
                explosionfart.play()
                final_boss.health -= 100  # Reducir la salud del Final Boss
                disparo = False
        
                if final_boss.health <= 0:
                    player.kill()
                    nolodiga.stop()
                    realdead.play()
                    death = win(screen)
                    if death == True:
                # Reiniciar el juego
                        lol = 1
                        StartScene(lol)
                        running = False
                    elif death == False:
                # Regresar al menú principal
                        lol = 0
                        StartScene(lol)
                        running = False
    # Actualizar y dibujar FinalBoss si está presente
        if final_boss_created:
            
            for entity in final_boss_group:
                entity.draw_health_bar(screen)  
                    
                if isinstance(entity, FinalBoss):
                    screen.blit(entity.image, entity.rect)
                    entity.mask = pygame.mask.from_surface(entity.image)
                    final_boss_group.update()
                    
        if pygame.sprite.spritecollide(player, enemies, False):
            if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
            
                vidas -= 1

                if vidas <= 0:
                    player.kill()
                    nolodiga.stop()
                    realdead.play()
                    death = muerte(screen)
                    if death == True:
                # Reiniciar el juego
                        lol = 1
                        StartScene(lol)
                        running = False
                    elif death == False:
                # Regresar al menú principal
                        lol = 0
                        StartScene(lol)
                        running = False
                else:
                    for enemy in pygame.sprite.spritecollide(player, enemies, False):
                        enemy.kill()
                    dañosound.play()
        if pygame.sprite.spritecollide(player, rayos, False):
            if pygame.sprite.spritecollide(player, rayos, False, pygame.sprite.collide_mask):
                
                vidas -= 1

                if vidas <= 0:
                    player.kill()
                    nolodiga.stop()
                    realdead.play()
                    death = muerte(screen)
                    if death == True:
                # Reiniciar el juego
                        lol = 1
                        StartScene(lol)
                        running = False
                    elif death == False:
                # Regresar al menú principal
                        lol = 0
                        StartScene(lol)
                        running = False
                else:
                    for enemy in pygame.sprite.spritecollide(player, enemies, False):
                        enemy.kill()
                    dañosound.play()
                
                    
        explosions.update()
        explosions.draw(screen)

        clock.tick(40)

        pygame.display.flip()

  

    



  