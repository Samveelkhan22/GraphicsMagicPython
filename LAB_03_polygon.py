import pygame
import math

def draw_regular_polygon(window, center, sides, length):
    angle = 360 / sides
    points = []
    for i in range(sides):
        x = center[0] + length * math.cos(math.radians(angle * i))
        y = center[1] + length * math.sin(math.radians(angle * i))
        points.append((x, y))

    pygame.draw.polygon(window, (0, 0, 0), points, 2)

def main():
    pygame.init()
    window_size = (640, 480)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Parameterized Regular Polygon")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 255, 255))
        draw_regular_polygon(window, (320, 240), 6, 100)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
