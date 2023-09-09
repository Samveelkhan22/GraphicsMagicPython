import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

CP = (0, 0)

def moveTo(p):
    global CP
    CP = p

def lineTo(p):
    global CP
    glBegin(GL_LINES)
    glVertex2f(CP[0], CP[1])
    glVertex2f(p[0], p[1])
    glEnd()
    CP = p

def rosette(N, radius):
    pointlist = []
    theta = 2.0 * math.pi / N

    for c in range(N):
        x = radius * math.sin(theta * c)
        y = radius * math.cos(theta * c)
        pointlist.append((x, y))

    for i in range(N):
        for j in range(N):
            moveTo(pointlist[i])
            lineTo(pointlist[j])

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(10, 10, 640, 480)
    rosette(11, 0.66)  # Generate 11 rosettes
    pygame.display.flip()

def main():
    pygame.init()
    display = (640, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        render()

if __name__ == "__main__":
    main()
