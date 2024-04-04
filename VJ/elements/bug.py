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
        


    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        return 0