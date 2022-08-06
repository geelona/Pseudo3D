import pygame
import sys
import random

pygame.init()

w = h = 800

win = pygame.display.set_mode((w, h))

circle_count = 10
circle_list = []


class Circle():
	def __init__(self):
		self.x = random.randint(0, w);
		self.y = random.randint(0, h);
		circle_list.append([self.x, self.y])
	
	def draw_circles():
		pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), 5)

def draw_bg():
	win.fill((100, 100, 100))

def draw():
	draw_bg()
	pygame.display.update()

#circle-creating--------------------
def circle_creating():
    for i in range(1, circle_count + 1):
    	i = Circle()
    	print(circle_list)
circle_creating()
#circle-creating--------------------

def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		draw()

if __name__ == "__main__":
	main()

