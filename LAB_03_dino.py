# import glfw
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import time

# def set_window(width, height):
#     glClearColor(1.0, 1.0, 1.0, 0.0)
#     glColor3f(0.0, 0.0, 0.0)
#     glPointSize(4.0)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluOrtho2D(0.0, width, 0.0, height)

# def draw_polyline_file(file_name):
#     try:
#         with open(file_name, 'r') as in_stream:
#             glClear(GL_COLOR_BUFFER_BIT)
#             numpolys = int(in_stream.readline().split()[0])
#             for j in range(numpolys):
#                 num_lines = int(in_stream.readline())
#                 lines = []
#                 for i in range(num_lines):
#                     x, y = map(int, in_stream.readline().split())
#                     lines.append((x, y))
#                 glBegin(GL_LINE_STRIP)
#                 for x, y in lines:
#                     glVertex2i(x, y)
#                 glEnd()
#             glFlush()
#     except FileNotFoundError:
#         print("Error: File not found")
#     except Exception as e:
#         print("Error:", e)

# def main():
#     if not glfw.init():
#         return

#     window_width, window_height = 640, 480
#     window = glfw.create_window(window_width, window_height, "DINOSAUR", None, None)
#     if not window:
#         glfw.terminate()
#         return

#     glfw.make_context_current(window)
#     glfw.set_window_size_callback(window, set_window)

#     set_window(window_width, window_height)

#     file_name = "C:\\Users\\J.I Traders\\Downloads\\dino.dat"  # Replace with the correct file path

#     while not glfw.window_should_close(window):
#         draw_polyline_file(file_name)
#         glfw.swap_buffers(window)
#         time.sleep(0.1)  # Adjust the delay time as needed to reduce blinking

#         glfw.poll_events()

#     glfw.terminate()

# if __name__ == "__main__":
#     main()


#Tilling code of a dino
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import io

def drawPolyLineFile(fileName, scale=1):
    try:
        with open(fileName, 'r') as inStream:
            numpolys = int(inStream.readline().split()[0])
            lines_list = []
            for j in range(numpolys):
                num_lines = int(inStream.readline())
                lines = []
                for i in range(num_lines):
                    x, y = map(int, inStream.readline().split())
                    lines.append((x * scale, y * scale))
                lines_list.append(lines)
        return lines_list
    except FileNotFoundError:
        print("Error: File not found")
        return []
    except Exception as e:
        print("Error:", e)
        return []

def setWindow(width, height):
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)

def main():
    if not glfw.init():
        return

    window_width, window_height = 640, 440
    rows, cols = 8, 10
    grid_width, grid_height = window_width // cols, window_height // rows

    window = glfw.create_window(window_width, window_height, "Dinosaur Grid", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)
    setWindow(window_width, window_height)

    dino_lines = drawPolyLineFile("C:\\Users\\J.I Traders\\Downloads\\dino.dat", scale=2)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        for i in range(rows):
            for j in range(cols):
                glViewport(j * grid_width, i * grid_height, grid_width, grid_height)
                glPushMatrix()
                for lines in dino_lines:
                    glBegin(GL_LINE_STRIP)
                    for x, y in lines:
                        glVertex2f(x, y)
                    glEnd()
                glPopMatrix()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
