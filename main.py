import pygame
import sys
import random

pygame.init()

w = h = 800

win = pygame.display.set_mode((w, h))

circle_count = 10
circle_list = []

def circle_create_func():
	if len(circle_list) < circle_count:
		for i in range(1, circle_count + 1):
			i = Circle()
		print(circle_list)


class Circle():
	def __init__(self):
		self.x = random.randint(0, w);
		self.y = random.randint(0, h);
		circle_list.append([self.x, self.y])

def draw_bg():
	win.fill((100, 100, 100))

def draw():
	draw_bg()
	
	pygame.display.update()

def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		circle_create_func()
		draw()

if __name__ == "__main__":
	main()

