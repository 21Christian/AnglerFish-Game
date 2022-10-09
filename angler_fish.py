import pygame
from constants import *
import random

# images
rectangle = pygame.transform.scale(pygame.image.load("assets/angler_fish.gif"), (40, 40))
rectangle2 = pygame.transform.flip(rectangle, True, False)



class BigFish(pygame.sprite.Sprite):
    def __init__(self, forward, backward):
        super().__init__()

        # Attributes
        self.health = 1
        self.ready = forward
        self.backward_pic = backward
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(760, random.randint(30, screen_height-30)))

        # Phase
        self.up = False
        self.down = False
        self.forward = False
        self.backward = False
        self.heal = False
        self.damage = False

    def update(self):
        # updating the position
        if self.up == True:
            self.rect.y -= speed
        if self.down == True:
            self.rect.y += speed
        if self.forward == True:
            self.rect.x -= speed
        if self.backward == True:
            self.rect.x += speed
        # updating the image according to the side the fish is facing
            self.image = self.backward_pic
        else:
            self.image = self.ready

        # updating the health
        if self.heal == True:
            self.health += heal
            self.heal = False
        if self.damage == True:
            self.health -= damage
            self.damage = False
        if self.health >= 40:
            self.health = 40






