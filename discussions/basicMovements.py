import pygame
import sys
from pygame.locals import *
from movements import moveCircle

pygame.init()

HEIGHT, WIDTH = 600, 800

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oct 2 Discussions - BASIC MOVEMENT")

circleX, circleY = 400, 300
circleRadius = 25

clock = pygame.time.Clock()

running = True
while running:
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, PINK, (circleX, circleY), circleRadius)
    
    keys = pygame.key.get_pressed()
    circleX, circleY = moveCircle(keys, circleX, circleY)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()