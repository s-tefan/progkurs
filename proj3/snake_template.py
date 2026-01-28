import pygame
import random
import time

snake_head_x=100
snake_head_y=100
snake_width=10
snake_height=10
snake_dir=0
snake_speed=5
#snake tail should be declared in some way
snake_tail=[] # x,y

score=0

# Apple variables
apple_position = (150, 150)

# Screen dimensions
WIDTH = 640
HEIGHT = 480

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK=(0,0,0)

def initScreen():
    # Create the screen
    global screen
    global score_font
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255,255,255))
    pygame.display.set_caption('Snake')
    # Update the display
    pygame.display.flip()
    # Score font
    score_font = pygame.font.Font(None, 36)

def moveAndDrawsnake_tail():
    print("draw the snakes tail")
    
def main():
    global apple_position
    global score
    global snake_head_x,snake_head_y,snake_width,snake_height
    global snake_dir

    initScreen()
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Clear the screen
        screen.fill(WHITE)

        # Draw the apple
        pygame.draw.circle(screen, RED, apple_position, 15)

        # Draw the score
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (500, 10))

        keys = pygame.key.get_pressed()
        # Control the snake
        if keys[pygame.K_RIGHT]:
            print("key right")
        # continue with other keys

        #move the snake        

        # Draw the snake
        # To be done
        pygame.draw.rect(screen, BLACK, (snake_head_x, snake_head_y, snake_width, snake_height))
        
        # Move the snakes tail
        
        
        # Collision detection between snake and apple

        # Update the display
        pygame.display.flip()
        time.sleep(0.1)
main()
pygame.quit()