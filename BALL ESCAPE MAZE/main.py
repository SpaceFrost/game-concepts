import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ball Escape Maze')
clock = pygame.time.Clock()
f = pygame.font.SysFont("Comic Sans MS",40)
draw_options = pymunk.pygame_util.DrawOptions(screen)
gameloop = True

# Physics setup
space = pymunk.Space()
space.gravity = (0, 900)

# Platform setup
def create_platform(x, y, width, height):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x,y)
    shape = pymunk.Poly.create_box(body,(width,height),5)
    shape.elasticity = 0.8
    space.add(body,shape)
    return body,shape

# create the maze
create_platform(400, 550, 700, 30)
create_platform(200, 425, 300, 30)
create_platform(625, 425, 250, 30)
create_platform(550, 300, 400, 30)
create_platform(125, 300, 150, 30)
create_platform(375, 175, 550, 30)

# Ball setup
def create_ball():
    body = pymunk.Body(1, pymunk.moment_for_circle(1,0,20))
    body.position = (400, 470)
    shape = pymunk.Circle(body,20)
    shape.elasticity = 0.5
    space.add(body,shape)
    return body,shape
  
# Exit door
exit_rect = pygame.Rect(750, 50, 50, 100)

# Game Over and Win Functions
def game_over():
    screen.fill("black")
    txt = f.render("GAME OVER",True,"red")
    rect = txt.get_rect(center = (400,300))
    screen.blit(txt,rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    gameloop = False


def game_win():
    screen.fill("black")
    txt = f.render("You Win!",True,"Green")
    rect = txt.get_rect(center = (400,300))
    screen.blit(txt,rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    gameloop = False
   


ball,ball_shape = create_ball()
# Main loop
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball.apply_impulse_at_local_point((0, -50))
    if keys[pygame.K_LEFT]:
        ball.apply_impulse_at_local_point((-10, 0))
    if keys[pygame.K_RIGHT]:
        ball.apply_impulse_at_local_point((10, 0))

    # Ball falling check
   
    if ball.position.y > 600 or ball.position.x > 800 or ball.position.x < 0:
        game_over()

    # Win check
    
    ball_pos = int(ball.position.x), int(ball.position.y)
    if exit_rect.collidepoint(ball_pos):
        game_win()

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), exit_rect)
    space.debug_draw(draw_options)
    
    # Step the simulation
    space.step(1 / 60.0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()