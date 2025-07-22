import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
score = 0
attempts = 3
game_over = False

# Physics setup 
space = pymunk.Space()
space.gravity = (0, 900)
draw_options = pymunk.pygame_util.DrawOptions(screen)

pin_image = pygame.image.load("Games/Pymunk/ROLL N STRIKE/pin.png")
pin_image = pygame.transform.scale(pin_image, (60, 95))

# Create bowling ball
def create_ball():
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = (300, 470)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.2
    space.add(body, shape)
    return body, shape

# Create pin
def make_pin(x, y):
    body = pymunk.Body(1, pymunk.moment_for_box(1, (10,40)))
    body.position = (x, y)
    shape = pymunk.Poly.create_box(body, size=(10, 40))  # Added size for realism
    shape.elasticity = 0.8
    space.add(body, shape)
    return body, shape

def floor():
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (400,560)
    shape = pymunk.Poly.create_box(body,size=(600,10))
    shape.elasticity = 0.4
    space.add(body,shape)
    return body,shape
    
# Create pins
pins = []
rows = [4, 3, 2, 1]  # Number of pins per row
start_x = 600
start_y = 520
dx = 30
dy = 70

for row_index, num_pins in enumerate(rows):
    row_y = start_y - row_index * dy
    row_start_x = start_x - ((num_pins - 1) * dx) / 2
    for i in range(num_pins):
        x = row_start_x + i * dx
        y = row_y
        pins.append(make_pin(x, y))

# Create ball
ball_body, ball_shape = create_ball()
floor_body, floor_shape = floor()

# Draw function
def draw_game():
    screen.fill("black")  # Clear screen
    space.debug_draw(draw_options)
    
    for body,shape in pins:
        x,y = body.position
        pin_rect = pin_image.get_rect(center = (x,y))
        screen.blit(pin_image, pin_rect)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            ball_body.position = (300, 470)
            ball_body.velocity = ((mousePos[0]-300)*4,(mousePos[1]-470)*4)

    space.step(1/60)
    draw_game()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()