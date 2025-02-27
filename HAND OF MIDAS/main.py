import pygame
import pgzrun
from random import randint
import time

pygame.init

"set width and height"
WIDTH = 800
HEIGHT = 800
 
"sets width and height of the window as well as caption"   
display = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("The Hand of Midas")

change_sfx = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/HAND OF MIDAS/coinbag-91016.mp3")

mc_dx = 0
mc_dy = 0
xcor = 360
ycor = 360
score = 0
FPS = 30

"sets the statue colors and if they are golden or not"
statue1Color = "darkgray"
statue2Color = "darkgray"
statue3Color = "darkgray"
statue4Color = "darkgray"
statueOmegaColor = "#d8bc70"

statue1IsGolden = False
statue2IsGolden = False
statue3IsGolden = False
statue4IsGolden = False

"defines variables for protagonist and statues"
protagonist = pygame.draw.rect(display,("blue"),(xcor,ycor,40,40))
statue1 = pygame.draw.rect(display,(statue1Color),(600,200,20,20))
statue2 = pygame.draw.rect(display,(statue2Color),(200,600,60,60))
statue3 = pygame.draw.rect(display,(statue3Color),(600,200,60,60))
statue4 = pygame.draw.rect(display,(statue4Color),(600,600,60,60))

"starts gameloop"
gameloop = True
while gameloop:
    "stops the gameloop once the window closes so it doesn't crash"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    "move the protagonist up,down,left,right"
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            mc_dy = -5
            ycor += mc_dy
            mc_dx = 0
        if event.key == pygame.K_DOWN:
            mc_dy = 5
            ycor += mc_dy
            mc_dx = 0
        if event.key == pygame.K_RIGHT:
            mc_dx = 5
            xcor += mc_dx
            mc_dy = 0
        if event.key == pygame.K_LEFT:
            mc_dx = -5
            xcor += mc_dx
            mc_dy = 0
    
    "changes statues to gold if protagonist touches them"
    if protagonist.colliderect(statue1):
        change_sfx.play()
        statue1Color = "yellow"
        statue1IsGolden = True
        
    if protagonist.colliderect(statue2):
        change_sfx.play()
        statue2Color = "yellow"
        statue2IsGolden = True
        
    if protagonist.colliderect(statue3):
        change_sfx.play()
        statue3Color = "yellow"
        statue3IsGolden = True
        
    if protagonist.colliderect(statue4):
        change_sfx.play()
        statue4Color = "yellow"
        statue4IsGolden = True
        

    "creates ending statue and ending"
    if statue1IsGolden == True and statue2IsGolden == True and statue3IsGolden == True and statue4IsGolden == True:
        statueOmegaColor = "red"
        
        if protagonist.colliderect(statueOmega):
            #statueOmegaColor = "green"
            
            statue1Color = "darkgreen"
            
            statue2Color = "darkgreen"
            
            statue3Color = "darkgreen"
            
            statue4Color = "darkgreen"
            
            statueOmegaColor = "yellow"
            pygame.display.set_caption("You Win!")
            
            
    
    "sets the bg color and creates the statues + protagonist"
    display.fill("#d8bc70")
    statueOmega = pygame.draw.rect(display,(statueOmegaColor),(340,340,80,80))
    protagonist = pygame.draw.rect(display,("blue"),(xcor,ycor,40,40))
    statue1 = pygame.draw.rect(display,(statue1Color),(160,160,60,60))
    statue2 = pygame.draw.rect(display,(statue2Color),(160,560,60,60))
    statue3 = pygame.draw.rect(display,(statue3Color),(560,160,60,60))
    statue4 = pygame.draw.rect(display,(statue4Color),(560,560,60,60))
    

    
    "updates the screen"
    pygame.display.flip()
    
    "maintains/limits the fps to be 60"
    pygame.time.Clock().tick(60)


"quits the game once the loop ends"
pygame.quit()

