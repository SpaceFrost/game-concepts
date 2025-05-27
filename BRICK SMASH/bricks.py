import pygame
import random

WIDTH = 800
HEIGHT = 600

class Bricks(pygame.sprite.Sprite):
    def __init__(self,x,y):
        brick_colors = ["red", "blue", "yellow", "green"]
        self.color = random.choice(brick_colors)
        self.rect = pygame.Rect(x,y,80,20)
