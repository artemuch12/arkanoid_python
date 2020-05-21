import pygame
from setting import *
from os import path

imgDir = path.join(path.dirname(__file__), 'img')

class Player(pygame.sprite.Sprite):
    """Класс отвечающий за платформу игрока"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(imgDir, 'Platform.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (PLAT_POZX, PLAT_POZY)
        self.speed = PLAT_SPEED
    def update(self):
        """Вызывается при обновлении кадра"""
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 10:
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x < HEIGHT-PLAT_WIDTH-200:
            self.rect.x += self.speed
