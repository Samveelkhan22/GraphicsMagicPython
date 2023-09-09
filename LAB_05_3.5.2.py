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

# Function to draw a diamond shape
def draw_diamond(x, y, size):
    diamond_points = [
        (x, y - size),  # Top point
        (x - size, y),  # Left point
        (x, y + size),  # Bottom point
        (x + size, y)   # Right point
    ]
    pygame.draw.polygon(screen, blue, diamond_points, 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the three connected diamonds
    draw_diamond(300, 300, 100)
    draw_diamond(450, 450, 100)
    draw_diamond(600, 300, 100)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
