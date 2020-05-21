import pygame
from setting import *
from os import path

imgDir = path.join(path.dirname(__file__), 'img')


class Boll(pygame.sprite.Sprite):
    """Класс отвечающйи за шарик"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(imgDir, 'Boll.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = BOLL_POZX
        self.rect.y = BOLL_POZY

        self.radius = BOLL_RAD
        self.flag = False
        self.speedx = 0
        self.speedy = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if not self.flag:
            if keys[pygame.K_SPACE]:
                self.speedx = BOLL_SPEEDX
                self.speedy = BOLL_SPEEDY
                self.flag = True
            if keys[pygame.K_LEFT] and self.rect.x-PLAT_WIDTH/2 > 2:
                self.rect.x -= PLAT_SPEED
            if keys[pygame.K_RIGHT] and self.rect.x < HEIGHT-230:
                self.rect.x += PLAT_SPEED
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.x < 5:
                self.speedx = -self.speedx
            if self.rect.x + self.radius > HEIGHT-200:
                self.speedx = -self.speedx
            if self.rect.y + self.radius < 25:
                self.speedy = -self.speedy
