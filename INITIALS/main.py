import pygame

pygame.init()

WIDTH = 1100
HEIGHT = 900

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("initials")

position1 = (100, 100, 100, 700)
position2a = (130, 100, 100, 300)
position2b = (210, 200, 50, 300)
position2c = (230, 300, 50, 300)
position2d = (250, 400, 50, 300)
position2e = (270, 500, 50, 200)
position2f = (290, 600, 50, 200)
position3 = (340, 100, 100, 700)

position4 = (600, 100, 100, 700)
position5a = (630, 100, 100, 300)
position5b = (710, 200, 50, 300)
position5c = (730, 300, 50, 300)
position5d = (750, 400, 50, 300)
position5e = (770, 500, 50, 200)
position5f = (790, 600, 50, 200)
position6 = (840, 100, 100, 700)



gameloop = True

while gameloop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
            
    display.fill("darkblue")
    firstletter_1 = pygame.draw.rect(display,("green"),position1)
    firstletter_2a = pygame.draw.rect(display,("green"),position2a)
    firstletter_2b = pygame.draw.rect(display,("green"),position2b)
    firstletter_2c = pygame.draw.rect(display,("green"),position2c)
    firstletter_2d = pygame.draw.rect(display,("green"),position2d)
    firstletter_2e = pygame.draw.rect(display,("green"),position2e)
    firstletter_2f = pygame.draw.rect(display,("green"),position2f)
    firstletter_3 = pygame.draw.rect(display,("green"),position3)
    
    secondletter_1 = pygame.draw.rect(display,("green"),position4)
    secondletter_2a = pygame.draw.rect(display,("green"),position5a)
    secondletter_2b = pygame.draw.rect(display,("green"),position5b)
    secondletter_2c = pygame.draw.rect(display,("green"),position5c)
    secondletter_2d = pygame.draw.rect(display,("green"),position5d)
    secondletter_2e = pygame.draw.rect(display,("green"),position5e)
    secondletter_2f = pygame.draw.rect(display,("green"),position5f)
    secondletter_3 = pygame.draw.rect(display,("green"),position6)
    
    pygame.display.flip()
            
pygame.quit()