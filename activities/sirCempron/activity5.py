import pygame
from pygame.locals import *
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Activity 5")

BLACK = (0,0,0)

def drawTriangle():
    trianglePoints = [(random.randint(10, 500), random.randint(10, 400)) for _ in range(3)]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.polygon(screen, color, trianglePoints)

def drawCircle():
    circleX, circleY = random.randint(10, 500), random.randint(10, 400)
    circleRadius = random.randint(10, 100)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(screen, color, (circleX, circleY), circleRadius)

def drawRectangle():
    rectWidth, rectHeight = random.randint(10, 100), random.randint(10, 100)
    rectX, rectY = random.randint(10, 500), random.randint(10, 400)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(screen, color, (rectX, rectY, rectWidth, rectHeight))

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_c:
                drawCircle()
            elif event.key == K_r:
                drawRectangle()
            elif event.key == K_t:
                drawTriangle()
            elif event.key == K_SPACE:
                screen.fill(BLACK)
            elif event.key == K_q:
                running = False
            
    pygame.display.flip()
    pygame.display.update()
    
pygame.quit()
sys.exit()