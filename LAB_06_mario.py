import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 830
CHAR_WIDTH, CHAR_HEIGHT = 80, 80
BACKGROUND_COLOR = (192, 192, 192)  # #C0C0C0

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

# Character attributes
char_x = WIDTH // 2 - CHAR_WIDTH // 2
char_y = HEIGHT - CHAR_HEIGHT - 50  # Position Mario above the bottom by 50 pixels
char_vel_x = 0
char_vel_y = 0
jumping = False

# Load Mario images (replace with your image file paths)
standing_img = pygame.image.load(r'd:\Users\J.I Traders\Downloads\MarioStanding.BMP')
running_img = pygame.image.load(r'd:\Users\J.I Traders\Downloads\MarioRun1.BMP')
jumping_img = pygame.image.load(r'd:\Users\J.I Traders\Downloads\MarioJump.BMP')

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        char_vel_x = -5
    elif keys[pygame.K_RIGHT]:
        char_vel_x = 5
    else:
        char_vel_x = 0

    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            char_vel_y = -10  # Negative value to jump upwards

    # Apply gravity
    char_vel_y += 1  # Increase the vertical velocity to simulate gravity

    # Update character position
    char_x += char_vel_x
    char_y += char_vel_y

    # Collision with ground
    if char_y >= HEIGHT - CHAR_HEIGHT - 50:
        char_y = HEIGHT - CHAR_HEIGHT - 50  # Prevent from going below the floor
        jumping = False

    # Clear the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the character based on state
    if jumping:
        screen.blit(jumping_img, (char_x, char_y))
    elif char_vel_x != 0:
        screen.blit(running_img, (char_x, char_y))
    else:
        screen.blit(standing_img, (char_x, char_y))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
