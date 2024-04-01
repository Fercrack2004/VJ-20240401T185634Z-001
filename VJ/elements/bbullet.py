import pygame
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
GREEN=(0,255,0)
bullet = pygame.Surface((10,10))
bullet.fill(RED)
bullet_mask=pygame.mask.from_surface(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet
        self.rect=self.image.get_rect()
        self.image.fill(RED)
        self.mask = pygame.mask.from_surface(self.image)
    def update (self, colour):
        pos = pygame.mouse.get_pos()
        self.rect.center = (pos)
        self.image.fill(colour)