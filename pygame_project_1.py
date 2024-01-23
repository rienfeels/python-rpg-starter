import pygame
import random
import os

pygame.init()

# Set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join('p1_jump.png'))


# Initialize pygame and create the window
pygame.mixer.init()
screen = pygame.display.set_mode((460, 580))  # Set an initial size for the display
pygame.display.set_caption("My Game")
Clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Convert the player_img surface after initializing the display
player_img = pygame.Surface.convert(player_img)

BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (460 / 2, 580 / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > 460:
            self.rect.right = 0

player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Keep loop running at the right speed
    Clock.tick(30)
    
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    
    # Draw / Render
    screen.fill((0, 0, 0))  # Use a tuple for the color
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
