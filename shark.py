import pygame
from constants import *

shark_pic = pygame.image.load("assets/Shark1.png")

class Shark(pygame.sprite.Sprite):
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
        if self.attack == True:
            self.rect.x += shark_speed





