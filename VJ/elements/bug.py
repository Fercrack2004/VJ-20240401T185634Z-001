"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""
import pygame
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load("VJ/assets/bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))
BUGpng_mask = pygame.mask.from_surface(BUGpng_scaled)
explosion_frames = [
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-8.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-9.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-10.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-11.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-12.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-13.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-14.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-15.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-16.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-1.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-2.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-3.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-4.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-5.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-6.png"),
    pygame.image.load("VJ/assets/explosion/explosionpng/5caeace96a10427deb40542d66fe83beoOh5aReaD8WelvVP-7.png")
    
    # Agrega aquí los fotogramas adicionales de tu animación
]
class Enemy(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy, self).__init__()
        self.image = BUGpng_scaled
        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                SCREEN_WIDTH + 100,
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.mask = BUGpng_mask
        self.speed = random.randint(5,7)
        self.explosion_index = 0 


    def update(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            
            self.kill()

            
         
        return 0
    def explode(self, screen):
        """
        Método para reproducir la animación de explosión.
        """
        if self.explosion_index < len(explosion_frames):
            # Dibujar el siguiente fotograma de la explosión en la pantalla
            screen.blit(explosion_frames[self.explosion_index], self.rect)
            self.explosion_index += 1
        else:
            # Si se alcanza el último fotograma, se reinicia la animación
            self.explosion_index = 0