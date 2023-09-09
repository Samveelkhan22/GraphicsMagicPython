import glfw
from OpenGL.GL import *

# Background color (initially black)
background_color = (0.0, 0.0, 0.0, 1.0)

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

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glfw.poll_events()  # Check for events

        # Set background color
        glClearColor(*background_color)
        glClear(GL_COLOR_BUFFER_BIT)

        # Swap the front and back buffers
        glfw.swap_buffers(window)

    # Clean up and exit
    glfw.terminate()

if __name__ == "__main__":
    main()
