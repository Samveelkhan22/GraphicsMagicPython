import pygame
import math

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_arc(window, center, radius, start_angle, sweep):
    n = 30  # number of intermediate segments in arc
    angle = math.radians(start_angle)  # initial angle in radians

    angle_inc = math.radians(sweep) / n  # angle increment

    cx, cy = center.x, center.y

    pygame.draw.line(window, (0, 0, 0), (cx, cy), (cx + radius * math.cos(angle), cy + radius * math.sin(angle)))

    for k in range(1, n):
        angle += angle_inc
        end_point = (cx + radius * math.cos(angle), cy + radius * math.sin(angle))
        pygame.draw.line(window, (0, 0, 0), (cx, cy), end_point)

def main():
    pygame.init()
    window_size = (640, 480)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Arc Drawing")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 255, 255))
        draw_arc(window, Point2(320, 240), 100, 45, 90)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
