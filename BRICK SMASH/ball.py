import pygame

WIDTH = 800
HEIGHT = 600

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2,HEIGHT-50,10,10)
        self.xvelocity = 15
        self.yvelocity = 15

    def move(self):
        self.rect.x += self.xvelocity 
        self.rect.y -= self.yvelocity
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.xvelocity *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.yvelocity *= -1
    
    def draw(self,screen,color):
        pygame.draw.rect(screen, color, self.rect)