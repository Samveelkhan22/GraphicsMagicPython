import pygame
import math

def parametric_curve(window, equation, start_t, end_t, step=0.01):
    t = start_t
    while t <= end_t:
        x, y = equation(t)
        pygame.draw.circle(window, (0, 0, 0), (int(x), int(y)), 1)
        t += step

def main():
    pygame.init()
    window_size = (640, 480)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Parametric Curves")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 255, 255))

        # Example of parametric curves
        # You can replace these equations with your desired parametric equations
        def equation1(t):
            x = 200 + 100 * math.cos(t)
            y = 240 + 100 * math.sin(t)
            return x, y

        def equation2(t):
            x = 440 + 50 * math.cos(3*t)
            y = 240 + 50 * math.sin(2*t)
            return x, y

        # Draw the parametric curves
        parametric_curve(window, equation1, 0, 2 * math.pi)
        parametric_curve(window, equation2, 0, 2 * math.pi)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
