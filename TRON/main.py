import pygame
import random

pygame.init()

"create constants width and height"
WIDTH = 1800
HEIGHT = 900
 
"sets width and height of the window as well as caption"   
display = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Tron Simulator")



cycle_dx = 0
cycle_dy = 0
cycleX = 400
cycleY = 300

score = 0
speed = 15

FPS = 30

headposition = (cycleX,cycleY,40,40)
trailposition = (cycleX,cycleY,20,20)


lightcycle = pygame.draw.rect(display,("lime"),headposition)
trail = []

"starts gameloop"
gameloop = True
while gameloop:
    "stops the gameloop once the window closes so it doesn't crash"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    "set bg color"
    display.fill("black")
    
    "make lightcycle move with arrow keys"
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            cycle_dy = -1*speed
            cycle_dx = 0
        if event.key == pygame.K_DOWN:
            cycle_dy = 1*speed
            cycle_dx = 0
        if event.key == pygame.K_RIGHT:
            cycle_dx = 1*speed
            cycle_dy = 0
        if event.key == pygame.K_LEFT:
            cycle_dx = -1*speed
            cycle_dy = 0
    
    "update cycle position"
    cycleX = cycleX + cycle_dx
    cycleY = cycleY + cycle_dy
    headposition = (cycleX,cycleY,40,40)
    trailposition = (cycleX+10,cycleY+10,20,20)
     
    "constantly create squares behind the lightcycle to make the 'trail' effect"
    trail.append(trailposition)

    for x in trail:
        pygame.draw.rect(display, "cyan",x)

    
    "create the lightcycle"
    lightcycle = pygame.draw.rect(display,("blue"),headposition)
    
    "updates the screen"
    pygame.display.flip()
    
    "maintains/limits the fps to be 60"
    pygame.time.Clock().tick(60)


"quits the game once the loop ends"
pygame.quit()

