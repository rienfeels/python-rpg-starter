import pygame
import random

# Size of the game screen player sees.
WIDTH = 360
HEIGHT = 480
FPS = 30

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame and create the window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height
player_speed = 5
jump = False
jump_count = 10

# Platform settings
platform_width = 100
platform_height = 20
platform_speed = 5
platforms = []

# Function to create a new platform
def create_platform():
    platform_x = random.randrange(0, WIDTH - platform_width)
    platform_y = 0
    platforms.append([platform_x, platform_y])

# Function to check collision between player and platforms
def is_collision(player_rect, platform_rect):
    return player_rect.colliderect(platform_rect)

# Game loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not jump:
                    jump = True

    # Update
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    if jump:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    # Move platforms
    for platform in platforms:
        platform[1] += platform_speed
        # Check if player lands on a platform
        if is_collision(pygame.Rect(player_x, player_y, player_width, player_height),
                        pygame.Rect(platform[0], platform[1], platform_width, platform_height)):
            if jump_count < 0 and player_y < platform[1]:
                player_y = platform[1] - player_height
                jump = False
                jump_count = 10

        # Check if platform reaches the bottom
        if platform[1] > HEIGHT:
            platforms.remove(platform)
            create_platform()

    # Create new platforms at random intervals
    if random.randrange(0, 100) < 2:  # Reduced platform creation frequency
        create_platform()

    # Check if the player falls to the bottom
    if player_y > HEIGHT:
        player_y = HEIGHT - player_height
        jump = False
        jump_count = 10

    # Draw / Render
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [player_x, player_y, player_width, player_height])

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, WHITE, [platform[0], platform[1], platform_width, platform_height])

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
