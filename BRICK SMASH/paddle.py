import pygame

WIDTH = 800
HEIGHT = 600

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2,HEIGHT-40,100,10)
        self.velocity = 15

    def move(self,keys):
        if self.rect.right < WIDTH and keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if self.rect.left > 0 and keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity   
    
    def draw(self,screen,color):
        pygame.draw.rect(screen, color, self.rect)