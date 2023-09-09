import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 800, 600

# Create the window
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# OpenGL initialization
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, width, height, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Input field variables
first_name = ""
last_name = ""

# Define a Pygame font
font = pygame.font.Font(None, 36)  # You can change the font and size as needed

# Function to draw the input fields and labels
def draw_input_fields():
    # Clear the screen with a white background
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # First Name Label
    first_name_label = font.render("First name:", True, (0, 0, 0))
    screen.blit(first_name_label, (50, 100))

    # First Name Input Field (Rectangle)
    pygame.draw.rect(screen, (0, 0, 0), (200, 100, 200, 30), 2)

    # Render First Name Text
    first_name_text = font.render(first_name, True, (0, 0, 0))
    screen.blit(first_name_text, (205, 105))

    # Last Name Label
    last_name_label = font.render("Last name:", True, (0, 0, 0))
    screen.blit(last_name_label, (50, 150))

    # Last Name Input Field (Rectangle)
    pygame.draw.rect(screen, (0, 0, 0), (200, 150, 200, 30), 2)

    # Render Last Name Text
    last_name_text = font.render(last_name, True, (0, 0, 0))
    screen.blit(last_name_text, (205, 155))

    # Submit Button (Rectangle)
    pygame.draw.rect(screen, (0, 0, 255), (300, 200, 100, 40))

    # Render Submit Text
    submit_text = font.render("Submit", True, (255, 255, 255))
    screen.blit(submit_text, (320, 205))

# Function to handle form submission
def handle_submit():
    print("First Name:", first_name)
    print("Last Name:", last_name)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                handle_submit()
            elif event.key == pygame.K_BACKSPACE:
                if event.widget == 0:
                    first_name = first_name[:-1]
                else:
                    last_name = last_name[:-1]
            elif event.widget == 0:
                first_name += event.unicode
            else:
                last_name += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the submit button was clicked
            if 300 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 240:
                handle_submit()

    draw_input_fields()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
