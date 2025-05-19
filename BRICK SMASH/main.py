import pygame
from paddle import Paddle
from ball import Ball
from bricks import Bricks

pygame.init()

"create constants width and height"
WIDTH = 800
HEIGHT = 600
 
"sets width and height of the window as well as caption"   
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Brick Smash")

x = 0
y = 0
brick_group = pygame.sprite.Group()
paddle = Paddle()
ball = Ball()
brick = Bricks(x,y)
brick_group.add(Bricks)

FPS = 20

row = 7
col = 7
startx = 80
starty = 20
spacex = 100
spacey = 30

for row in range(row):
    for col in range(col):
        x = startx + col * spacex
        y = starty + row * spacey
        

"starts gameloop"
gameloop = True
while gameloop:
    "stops the gameloop once the window closes so it doesn't crash"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    keys = pygame.key.get_pressed()
    paddle.move(keys)
    ball.move()
    screen.fill("black")
    ball.draw(screen, "red")
    brick_group.draw(screen)
    paddle.draw(screen,"blue")
    
    "updates the screen"
    pygame.display.flip()
    
    "maintains/limits the fps to be 20"
    pygame.time.Clock().tick(20)


"quits the game once the loop ends"
pygame.quit()

