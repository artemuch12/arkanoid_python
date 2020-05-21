import pygame
from setting import *
from os import path

imgDir = path.join(path.dirname(__file__), 'img')

class Stones(pygame.sprite.Sprite):
    """Класс отвечающйи за кирпичики"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(imgDir, 'Brics.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
