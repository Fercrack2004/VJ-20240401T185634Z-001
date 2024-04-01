"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)
JorgePNG = pygame.image.load("assets/JorgeVJ.png")
JorgePNG_rect=JorgePNG.get_rect()
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80,80))
JorgePNG_mask=pygame.mask.from_surface(JorgePNG_scaled)
mask_image=JorgePNG_mask.to_surface()




class Player(pygame.sprite.Sprite):
    def __init__ (self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()
        self.image = mask_image
        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.image.get_rect()
        self.mask=JorgePNG_mask
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
       

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4,0)
        