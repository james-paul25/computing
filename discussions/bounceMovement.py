import pygame
from pygame.locals import *
import sys
import random # new import

pygame.init()

# we will add a sound effect when the ball bounces
pygame.mixer.init()


HEIGHT, WIDTH = 600, 800

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oct 2 Discussions - BOUNCE MOVEMENT")

circleX, circleY = 400, 300
circleRadius = 50

clock = pygame.time.Clock()

# Initial movement direction (right)
dx, dy = 1, 0

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, PINK, (circleX, circleY), circleRadius)

    
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

    # Bounce off the edges
    if circleX - circleRadius <= 0 or circleX + circleRadius >= WIDTH:
        dx *= -1
    if circleY - circleRadius <= 0 or circleY + circleRadius >= HEIGHT:
        dy *= -1

    pygame.display.flip()
    

pygame.quit()
sys.exit()