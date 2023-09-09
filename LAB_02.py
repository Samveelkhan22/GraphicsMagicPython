import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen (width, height)
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption for the window
pygame.display.set_caption("Scenery with Long Road, Clouds, Rain, and Standard House")

# Colors
black = (0, 0, 0)
blue = (135, 206, 250)
gray = (128, 128, 128)
white = (255, 255, 255)
blue_sky = (25, 25, 112)
green = (34, 139, 34)
red = (255, 0, 0)
brown = (165, 42, 42)
yellow = (255, 255, 0)
dark_green = (0, 100, 0)

# Cloud properties
cloud_width = 100
cloud_height = 50

# Raindrop properties
raindrop_width = 2
raindrop_height = 10
max_raindrops = 100

# House properties
house_width = 200
house_height = 150
window_width = 60
window_height = 80
gate_width = 100
gate_height = 40

# Create a list to store clouds
clouds = []

# Create a list to store raindrops
raindrops = []

def draw_background():
    # Black background
    screen.fill(black)

    # Ground
    pygame.draw.rect(screen, green, (0, screen_height * 0.7, screen_width, screen_height * 0.3))

def draw_moon(x, y):
    pygame.draw.circle(screen, white, (x, y), 50)

def create_clouds():
    # Generate small clouds
    for i in range(3):
        x = 150 + i * 250
        y = 100 + i * 50
        clouds.append([x, y])

def draw_cloud(x, y):
    pygame.draw.circle(screen, gray, (x, y), cloud_width // 3)
    pygame.draw.circle(screen, gray, (x + cloud_width // 2, y), cloud_width // 3)
    pygame.draw.circle(screen, gray, (x + cloud_width, y), cloud_width // 3)
    pygame.draw.ellipse(screen, gray, (x, y - cloud_height // 2, cloud_width, cloud_height))
    pygame.draw.ellipse(screen, gray, (x + cloud_width // 2, y - cloud_height // 2, cloud_width, cloud_height))

def create_raindrops():
    # Generate random raindrops
    for _ in range(max_raindrops):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        raindrops.append([x, y])

def draw_raindrops():
    for drop in raindrops:
        pygame.draw.rect(screen, white, (drop[0], drop[0], raindrop_width, raindrop_height))

def move_raindrops():
    for drop in raindrops:
        drop[1] += 5  # Move raindrop down
        if drop[1] > screen_height:
            drop[0] = random.randint(0, screen_width)
            drop[1] = random.randint(-screen_height, 0)


def draw_house(x, y):
    # Black border around the house
    pygame.draw.rect(screen, black, (x, y, 200, 150), 2)

    # House base with a white fill
    pygame.draw.rect(screen, blue, (x, y, 200, 150))

    # Roof with a white fill
    pygame.draw.polygon(screen, blue, [(x, y), (x + 100, y - 100), (x + 200, y)])
    
    # Black border separating the roof and base
    pygame.draw.line(screen, black, (x, y), (x + 200, y), 2)

    # Window with a black border
    pygame.draw.rect(screen, black, (x + 50, y + 50, 50, 50), 2)

    # Door with a black border
    pygame.draw.rect(screen, black, (x + 125, y + 50, 50, 100), 2)

def draw_scene():
    draw_background()

    # Draw the moon in the top left corner
    draw_moon(100, 100)


    # Draw the small clouds
    for cloud in clouds:
        draw_cloud(cloud[0], cloud[1])

    # Draw the raindrops
    draw_raindrops()

    # Draw the house in the center
    draw_house((screen_width - house_width) // 2, screen_height - house_height - 50)

running = True
create_clouds()  # Initialize small clouds
create_raindrops()  # Initialize raindrops
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the raindrops
    move_raindrops()

    # Clear the screen
    screen.fill(black)

    # Draw the scenery scene with long road, clouds, rain, and standard house
    draw_scene()

    # Update the screen
    pygame.display.update()

# Quit the program
pygame.quit()
sys.exit()