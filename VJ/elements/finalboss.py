import pygame
import random
from pygame.locals import (RLEACCEL)
# Definición de colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BAR_LENGTH = 400
BAR_HEIGHT = 20
jorgemalo = pygame.image.load("VJ/assets/jorgemalo.png")
jorgemalo_scaled = pygame.transform.scale(jorgemalo, (463, 319))
class FinalBoss(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        
        self.image = jorgemalo_scaled
        self.image.set_colorkey((0,0,0), RLEACCEL)
        if self.image is None:
            print("Error: No se pudo cargar la imagen del jefe.")
        else:
            print("La imagen del jefe se cargó correctamente.")
        
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.health = 1000
        self.rect = self.image.get_rect(
            center=(
                SCREEN_WIDTH+100,
                SCREEN_HEIGHT//2)
            )
        self.speed=2
        self.moving_to_center=True
    def update(self):
        
        # Desplazamiento hacia la izquierda
        if self.moving_to_center:
            if self.rect.centerx < self.screen_width-200:
                self.rect.move_ip(-self.speed, 0)
            else:
                self.rect.centerx = self.screen_width-200
                self.speed = 0
                self.moving_to_center = False

    def draw_health_bar(self, screen):
        outline_rect = pygame.Rect(10, self.screen_height - 30, BAR_LENGTH, BAR_HEIGHT)
        inner_rect = pygame.Rect(10, self.screen_height - 30, int(self.health / 10000 * BAR_LENGTH), BAR_HEIGHT)
        pygame.draw.rect(screen, RED, outline_rect, 2)
        pygame.draw.rect(screen, GREEN, inner_rect)