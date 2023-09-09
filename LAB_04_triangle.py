import glfw
from OpenGL.GL import *

# Initial color is white
color = (1.0, 1.0, 1.0)

WHITE = (1.0, 1.0, 1.0)
RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)

angle = 0.0
color = WHITE  # Initial color is white

def renderScene():
    global angle
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, glfw.get_framebuffer_size(window)[0], glfw.get_framebuffer_size(window)[1])
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = glfw.get_framebuffer_size(window)[0] / glfw.get_framebuffer_size(window)[1]
    glOrtho(-aspect_ratio, aspect_ratio, -1.0, 1.0, -1.0, 1.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glRotatef(angle, 0.0, 0.0, 1.0)
    glColor3f(*color)
    
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()
    
    angle += 0.5
    
    glfw.swap_buffers(window)

def on_key(window, key, scancode, action, mods):
    global color
    
    if action == glfw.PRESS:
        if key == glfw.KEY_R:
            color = RED
        elif key == glfw.KEY_G:
            color = GREEN
        elif key == glfw.KEY_B:
            color = BLUE

def main():
    if not glfw.init():
        return
    
    global window
    window = glfw.create_window(320, 320, "Menu Test", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    glfw.set_key_callback(window, on_key)
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        renderScene()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
