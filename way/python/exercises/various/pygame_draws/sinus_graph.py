# Python 2.7, required pygame
import pygame, sys, random, math
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
plotPoints = []

for x in range (640):
	y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
	plotPoints.append([x, y])

color = THECOLORS[random.choice(THECOLORS.keys())]
pygame.draw.lines(screen, color, False, plotPoints, 1)

pygame.display.flip()
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()
