import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paddle Game")

#load the sound and play it when required
hit_sfx = pygame.mixer.Sound("PING PONG - TEST/hit.mp3")
go_sfx = pygame.mixer.Sound("PING PONG - TEST/game_over.mp3")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Default font, size 36
# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class RedPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_player=True):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.score= 0
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 15:
            self.rect.y += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 15:
            self.rect.y -= self.velocity
        #write the code for the player to move

class BluePaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_player=True):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.score=0
    
    def update(self):
        #write the code for the other player's movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 15:
            self.rect.y -= self.velocity
        if keys[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT - 15:
            self.rect.y += self.velocity
        
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = 3
        self.velocity_y = 3
    
    def update(self):
       #write the code for ball movement
       self.rect.x += self.velocity_x
       self.rect.y += self.velocity_y

       #write the code for the bounce off condition
       if self.rect.bottom > WINDOW_HEIGHT or self.rect.top < 0:
           self.velocity_y *= -1
           hit_sfx.play()
       if pygame.sprite.collide_rect(ball, red_paddle) or pygame.sprite.collide_rect(ball, blue_paddle):
           hit_sfx.play()
           ball.velocity_x *= -1
           
#Combo count
red_combo = 0
blue_combo = 0       

# Create game objects
red_paddle = RedPaddle(30, WINDOW_HEIGHT//2, is_player=True)
blue_paddle = BluePaddle(WINDOW_WIDTH-50, WINDOW_HEIGHT//2, is_player=True)
ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(red_paddle, blue_paddle, ball)

# Main game loop
running = True
gameover=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update objects
    red_paddle.update()
    blue_paddle.update()
    ball.update()


    player_score_text = font.render(f"Red Score: {red_paddle.score}", True, WHITE)
    player_score_rect = player_score_text.get_rect(topleft=(10, 10)) 

    computer_score_text = font.render(f"Blue Score: {blue_paddle.score}", True, WHITE)
    computer_score_rect = computer_score_text.get_rect(topright=(780, 10)) 


    gameover_text = font.render(f"Game Over", True, WHITE)
    gameover_rect = gameover_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


    #Write the conditions if the ball goes out of bound
    if ball.rect.left <= 0:
        blue_paddle.score += 1
        blue_combo += 1
        red_combo = 0
        ball.rect.centerx = WINDOW_WIDTH//2
        ball.rect.centery = WINDOW_HEIGHT//2
        ball.velocity_x *= -1
        
    if ball.rect.right >= WINDOW_WIDTH:
        red_paddle.score += 1
        red_combo += 1
        blue_combo = 0
        ball.rect.centerx = WINDOW_WIDTH//2
        ball.rect.centery = WINDOW_HEIGHT//2
        ball.velocity_x *= -1
        
    combo_text = font.render("", True, WHITE)  # Default empty
    combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH // 2, 40))
    #combo system
    if red_combo == 2:
        combo_text = font.render(f"DOUBLE!", True, RED)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
    
    if red_combo == 3:
        combo_text = font.render(f"TRIPLE!", True, RED)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
        
    if red_combo == 4:
        combo_text = font.render(f"QUADRA!", True, RED)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
    
    if red_combo > 4:
        combo_text = font.render(f"ABSOLUTE DOMINATION!", True, RED)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
    
    if blue_combo == 2:
        combo_text = font.render(f"DOUBLE!", True, BLUE)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
    
    if blue_combo == 3:
        combo_text = font.render(f"TRIPLE!", True, BLUE)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
        
    if blue_combo == 4:
        combo_text = font.render(f"QUADRA!", True, BLUE)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
        
    if blue_combo > 4:
        combo_text = font.render(f"ABSOLUTE DOMINATION!", True, BLUE)
        combo_rect = combo_text.get_rect(midtop=(WINDOW_WIDTH//2, 40))
    #write gameover condition

    #Write Ball collision with paddles condition
   
   
    # Draw everything
    display_surface.fill((0,0,0))
    display_surface.blit(combo_text, combo_rect)
    all_sprites.draw(display_surface)

    display_surface.blit(player_score_text, player_score_rect)
    display_surface.blit(computer_score_text, computer_score_rect)
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()