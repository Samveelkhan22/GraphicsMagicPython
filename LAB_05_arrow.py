import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Create the display surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
black = (0, 0, 0)
blue = (0, 0, 255)

# Starting position
x, y = 100, 300

# Arrow parameters
arrow_length = 100
arrow_head_width = 20
arrow_head_length = 30

# Arrow movement speed
arrow_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= arrow_speed
    if keys[pygame.K_RIGHT]:
        x += arrow_speed
    if keys[pygame.K_UP]:
        y -= arrow_speed
    if keys[pygame.K_DOWN]:
        y += arrow_speed

    # Clear the screen
    screen.fill(black)

    # Draw the arrow using relative moves and draws
    pygame.draw.line(screen, blue, (x, y), (x + arrow_length, y), 5)
    pygame.draw.polygon(screen, blue, [(x + arrow_length, y), 
                                      (x + arrow_length - arrow_head_length, y - arrow_head_width // 2),
                                      (x + arrow_length - arrow_head_length, y + arrow_head_width // 2)])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
