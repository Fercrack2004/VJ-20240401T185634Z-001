import pygame
import random
from pygame.locals import (RLEACCEL)

rayopng = pygame.image.load("VJ/assets/raidpng.png")
rayopng_scaled = pygame.transform.scale(rayopng, (64, 64))
rayopng_mask = pygame.mask.from_surface(rayopng_scaled)

class Rayo(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Rayo, self).__init__()
        self.image = rayopng_scaled
        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                SCREEN_WIDTH + 100,
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.mask = rayopng_mask
        self.speed = random.randint(5,7)
        self.explosion_index = 0 


    def update(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            
            self.kill()

            
         
        return 0
    