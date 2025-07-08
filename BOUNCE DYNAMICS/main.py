import pygame
import pymunk
import pymunk.pygame_util

def create_ball(space, position, elasticity):
  #write the code to create ball object
  return space
def create_floor(space):
    """Creates a static floor for the balls to bounce on."""
    floor = pymunk.Segment(space.static_body, (50, 500), (750, 500), 5)
    floor.elasticity = 1.0  # Maximum bounce
    space.add(floor)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Elasticity Demo")
    clock = pygame.time.Clock()

    #create pymunk space
    space = pymunk.Space() 

    #gravity to pull downward
    
    space.gravity = (0,981)

    #Update physics simulation
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    
    # Create a floor
    create_floor(space)

    infiniteBalls = False
    balls = []

    # Create balls with different elasticity
    
    
    def makeBall1(space):
        body = pymunk.Body(1,pymunk.moment_for_circle(1,0,30))
        body.position = (200,50)
        shape = pymunk.Circle(body,20)
        shape.elasticity = 0.8
        space.add(body,shape)
        return body,shape

    def makeBall2(space):
        body = pymunk.Body(1,pymunk.moment_for_circle(1,0,30))
        body.position = (400,50)
        shape = pymunk.Circle(body,20)
        shape.elasticity = 0.5
        space.add(body,shape)
        return body,shape

    def makeBall3(space):
        body = pymunk.Body(1,pymunk.moment_for_circle(1,0,30))
        body.position = (600,50)
        shape = pymunk.Circle(body,20)
        shape.elasticity = 0.2
        space.add(body,shape)
        return body,shape
    
    def reset_balls():
        balls.append(makeBall1(space))
        balls.append(makeBall2(space))
        balls.append(makeBall3(space))
        
    def spawn_balls():
        makeBall1(space)
        makeBall2(space)
        makeBall3(space)
        
    reset_balls()
    
    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                screen.fill((0, 0, 0))

                if event.key == pygame.K_r:
                    for body, shape in balls:
                        space.remove(body, shape)
                    balls.clear()
                    reset_balls()

                elif event.key == pygame.K_BACKSLASH:
                    infiniteBalls = not infiniteBalls  # toggle on/off

                elif infiniteBalls:
                    spawn_balls()
                    
                    
        # Update physics simulation
        
        space.step(1/60)
        
        # Draw objects
        
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()