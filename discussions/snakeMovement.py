import pygame
from pygame.locals import *
import sys
import random # new import

pygame.init()

HEIGHT, WIDTH = 600, 800

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oct 2 Discussions")

circleX, circleY = 400, 300
circleRadius = 50

# Initial movement direction (right)
dx, dy = 1, 0

running = True
while running:
    screen.fill(PINK)
    pygame.draw.circle(screen, BLUE, (circleX, circleY), circleRadius)

    # Change direction only when key is pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                dx, dy = 0, -1
            elif event.key == K_DOWN:
                dx, dy = 0, 1
            elif event.key == K_LEFT:
                dx, dy = -1, 0
            elif event.key == K_RIGHT:
                dx, dy = 1, 0

    circleX += dx
    circleY += dy

    circleX = max(circleRadius, min(WIDTH - circleRadius, circleX))
    circleY = max(circleRadius, min(HEIGHT - circleRadius, circleY))

    pygame.display.flip()

pygame.quit()
sys.exit()