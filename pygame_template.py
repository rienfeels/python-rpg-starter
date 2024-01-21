# Pygame Template - skeleton for a new pygame project.

import pygame
import random
#size of the game screen player sees.

WIDTH = 360
HEIGHT = 480
FPS = 30
# define the colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#initialize pygame and create the window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
Clock = pygame.time.Clock()

#Game loop

running = True
while running:
    #Keep loop running at the right speed
    Clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
    #update
    
    #Draw / Render
            
    screen.fill(BLACK)
    # *after* drawing everything, filp the display
    
    pygame.display.flip()

pygame.quit()