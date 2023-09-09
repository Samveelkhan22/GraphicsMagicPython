import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import time

def set_window(width, height):
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)

def draw_polyline_file(file_name):
    try:
        with open(file_name, 'r') as in_stream:
            glClear(GL_COLOR_BUFFER_BIT)
            numpolys = int(in_stream.readline().split()[0])
            for j in range(numpolys):
                num_lines = int(in_stream.readline())
                lines = []
                for i in range(num_lines):
                    x, y = map(int, in_stream.readline().split())
                    lines.append((x, y))
                glBegin(GL_LINE_STRIP)
                for x, y in lines:
                    glVertex2i(x, y)
                glEnd()
            glFlush()
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print("Error:", e)

def main():
    if not glfw.init():
        return

    window_width, window_height = 640, 480
    window = glfw.create_window(window_width, window_height, "DINOSAUR", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, set_window)

    set_window(window_width, window_height)

    file_name = "C:\\Users\\J.I Traders\\Downloads\\dino.dat"  # Replace with the correct file path

    while not glfw.window_should_close(window):
        draw_polyline_file(file_name)
        glfw.swap_buffers(window)
        time.sleep(0.1)  # Adjust the delay time as needed to reduce blinking

        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()

