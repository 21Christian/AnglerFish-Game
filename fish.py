import pygame
from constants import *

from itertools import cycle

fish_pic = pygame.transform.scale(pygame.image.load("assets/fish.png"), (20, 20))
fish_pic = pygame.transform.flip(fish_pic, True, False)

class Fish(pygame.sprite.Sprite):
    def __init__(self, ready, pos_y):
        super().__init__()

        # Attributes
        self.damage = damage
        self.ready = ready
        self.pos_y = pos_y
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(0, pos_y))

        # Phase
        self.attack = False
        self.move = False

    def update(self):
        # updating the position
        if self.attack == True:
            self.rect.x += fish_speed





