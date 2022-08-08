import pygame
import sys
import random
import math

pygame.init()

size = 1000

w = size + 400
h = size 

center = (w / 2, h / 2)

win = pygame.display.set_mode((w, h))

circle_count = 50


class Circle:
    circle_list = []

    wasd_speed = 2

    def __init__(self):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)

        self.shadow_x = self.x + random.randint(-50, 50)
        self.shadow_y = self.y + random.randint(-50, 50)

        self.color = (0, random.randint(50, 255), 0)
        self.size = random.randint(10, 50)
        Circle.circle_list.append([self.x, self.y, self.color, self.size, self.shadow_x, self.shadow_y])

    @staticmethod
    def draw_circles():
        for i in range(circle_count):

            pygame.draw.circle(win, (100, 100, 100),
                               (Circle.circle_list[i][4], Circle.circle_list[i][5]),
                               Circle.circle_list[i][3])

        for i in range(circle_count):

            pygame.draw.circle(win, Circle.circle_list[i][2],
                               (Circle.circle_list[i][0], Circle.circle_list[i][1]),
                               Circle.circle_list[i][3])

    @staticmethod
    def motion():
            
        keys = pygame.key.get_pressed()

        # wasd movement ---------------------------------------------
        if keys[pygame.K_w]:
            for i in range(circle_count):
                Circle.circle_list[i][1] -= Circle.wasd_speed
                Circle.circle_list[i][5] -= Circle.wasd_speed
        
        if keys[pygame.K_s]:
            for i in range(circle_count):
                Circle.circle_list[i][1] += Circle.wasd_speed
                Circle.circle_list[i][5] += Circle.wasd_speed

        if keys[pygame.K_a]:
            for i in range(circle_count):
                Circle.circle_list[i][0] -= Circle.wasd_speed
                Circle.circle_list[i][4] -= Circle.wasd_speed

        if keys[pygame.K_d]:
            for i in range(circle_count):
                Circle.circle_list[i][0] += Circle.wasd_speed
                Circle.circle_list[i][4] += Circle.wasd_speed
        # wasd movement ---------------------------------------------

        if keys[pygame.K_LEFT]:
            for i in range(circle_count):

                rad = math.atan2(Circle.circle_list[i][1] - center[1], Circle.circle_list[i][0] - center[0])
                sin = math.sin(rad)
                cos = math.cos(rad)

                #r = ((Circle.circle_list[i][0] - center[0])**2 + (Circle.circle_list[i][1] - center[1])**2)**0.5

                Circle.circle_list[i][0] += cos
                Circle.circle_list[i][1] += sin

        if keys[pygame.K_RIGHT]:
            for i in range(circle_count):

                rad = math.atan2(Circle.circle_list[i][1] - center[1], Circle.circle_list[i][0] - center[0])
                sin = math.sin(rad)
                cos = math.cos(rad)

                #r = ((Circle.circle_list[i][0] - center[0])**2 + (Circle.circle_list[i][1] - center[1])**2)**0.5

                Circle.circle_list[i][0] -= cos
                Circle.circle_list[i][1] -= sin


# circle-creating--------------------
def circle_creating():
    for i in range(circle_count):
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

        Circle.motion()

        win.fill((20, 20, 20))
        Circle.draw_circles()
        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
