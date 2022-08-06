import pygame
import sys
import random

pygame.init()

w = h = 800

win = pygame.display.set_mode((w, h))

circle_count = 10
circle_list = []


class Circle:
    def __init__(self):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        circle_list.append([self.x, self.y])

    def draw_circles(self):
        pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), 5)


# circle-creating--------------------
def circle_creating():
    for i in range(1, circle_count + 1):
        Circle()


circle_creating()
# circle-creating--------------------


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        win.fill((20, 20, 20))
        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
