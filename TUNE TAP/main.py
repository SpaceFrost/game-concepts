import pygame

pygame.init()

display = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("Xylophone")

redNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308 (1)(1).mp3")
orangeNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308.mp3")
yellowNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308(1).mp3")
greenNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308(2).mp3")
blueNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308(3).mp3")
purpleNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308(4).mp3")
pinkNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/0308(5).mp3")
secretNoise = pygame.mixer.Sound("C:/Users/neiln/OneDrive/Desktop/Game Concepts/TUNE TAP/jump-and-spark-6136.mp3")

complete1 = False
complete2 = False
complete3 = False
complete4 = False

gameloop = True
while gameloop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        click_pos = pygame.mouse.get_pos()
        if  (400,50) < click_pos < (500,850):
            redNoise.play()
            complete2 = True
            complete3 = False
            complete4 = False
        if  (550,100) < click_pos < (650,800):
            orangeNoise.play()
        if  (700,150) < click_pos < (800,750):
            yellowNoise.play()
        if  (850,200) < click_pos < (950,800):
            greenNoise.play() 
            complete4 = True
        if  (1000,250) < click_pos < (1100,650):
            blueNoise.play()  
            complete1 = True
            complete2 = False
            complete3 = False
            complete4 = False
        if  (1150,300) < click_pos < (1250,500):
            purpleNoise.play()    
            complete3 = True
            complete4 = False
        if  (1300,350) < click_pos < (1400,450):
            pinkNoise.play()    
    
    
    if complete1 == True and complete2 == True and complete3 == True and complete4 == True:
        pygame.time.delay(2000)
        secretNoise.set_volume(100)
        secretNoise.play()
            
            
    display.fill("black")
    redKey = pygame.draw.rect(display, "red", (400, 50, 100, 800))
    orangeKey = pygame.draw.rect(display, "orange", (550, 100, 100, 700))
    yellowKey = pygame.draw.rect(display, "yellow", (700, 150, 100, 600))
    greenKey = pygame.draw.rect(display, "green", (850, 200, 100, 500))
    blueKey = pygame.draw.rect(display, "blue", (1000, 250, 100, 400))
    purpleKey = pygame.draw.rect(display, "purple", (1150, 300, 100, 300))
    pinkKey = pygame.draw.rect(display, "hotpink", (1300, 350, 100, 200))
    
    pygame.display.flip()
    
    

pygame.time.clock(tick(60))
pygame.quit()
