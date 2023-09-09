import glfw
from OpenGL.GL import *
import os
import pygame

# Background color (initially black)
background_color = (0.0, 0.0, 0.0, 1.0)

# List to store the positions of the red dots
red_dots_positions = []

# Handler for window resize event
def framebuffer_size_callback(window, width, height):
    global background_color
    glViewport(0, 0, width, height)
    if width > 0 and height > 0:
        # Set background color to white when the window is resized
        background_color = (1.0, 1.0, 1.0, 1.0)
    else:
        # Set background color to black when the window is minimized
        background_color = (0.0, 0.0, 0.0, 1.0)

# Handler for mouse click event
def mouse_button_callback(window, button, action, mods):
    global red_dots_positions
    window_width, window_height = glfw.get_framebuffer_size(window)  # Get window size
    if action == glfw.PRESS and button == glfw.MOUSE_BUTTON_LEFT:
        xpos, ypos = glfw.get_cursor_pos(window)
        normalized_x = xpos * 2 / window_width - 1
        normalized_y = 1 - ypos * 2 / window_height
        red_dots_positions.append((normalized_x, normalized_y))

# Handler for keyboard key press event
def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS and key == glfw.KEY_SPACE:
        play_sound_effect()

def play_sound_effect():
    sound_path = os.path.join(os.path.expanduser("~"), "Downloads", "attack2t22wav-14511.mp3")
    if os.path.exists(sound_path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    else:
        print(f"Sound file not found: {sound_path}")

# Main function
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a window
    window_width = 640
    window_height = 480
    window = glfw.create_window(window_width, window_height, "Resizable White Window", None, None)
    if not window:
        glfw.terminate()
        return

    # Set the OpenGL context
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    # Register the key_callback for keyboard key press event
    glfw.set_key_callback(window, key_callback)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glfw.poll_events()  # Check for events

        # Set background color
        glClearColor(*background_color)
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw red dots at the positions stored in red_dots_positions
        glColor3f(1.0, 0.0, 0.0)  # Set color to red
        glPointSize(5)  # Set point size
        glBegin(GL_POINTS)
        for x, y in red_dots_positions:
            glVertex2f(x, y)
        glEnd()

        # Swap the front and back buffers
        glfw.swap_buffers(window)

    # Clean up and exit
    glfw.terminate()

if __name__ == "__main__":
    main()
