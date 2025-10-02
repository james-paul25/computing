import pygame
from pygame.locals import *
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Activity 5")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

circleX, circleY = random.randint(10, 500), random.randint(10, 400)
circleRadius = random.randint(10, 100)

rectWidth, rectHeight = random.randint(10, 100), random.randint(10, 100)

trianglePoints = [(random.randint(10, 500), random.randint(10, 400)) for _ in range(3)]
triangleSpeed = [1, 1] 
triangleColor = (255, 0, 0)

clock = pygame.time.Clock()

rectX, rectY = random.randint(10, 500), random.randint(10, 400)

rectangle_list = []
triangle_list = []
circle_list = []

running = True
show_green_circle = False 
show_red_triangle = False
show_blue_rectangle = False
clear_screen = False

while running:
    
    screen.fill(BLACK)
    
    for c in circle_list:
        pygame.draw.circle(screen, GREEN, (c[0], c[1]), c[2])
    for r in rectangle_list:
        pygame.draw.rect(screen, BLUE, (r[0], r[1], r[2], r[3]))
    for t in triangle_list:
        pygame.draw.polygon(screen, triangleColor, t)
    
    keys = pygame.key.get_pressed()
    
    if keys[K_c]:
        circleX, circleY = random.randint(10, 800), random.randint(10, 600)
        circle_list.append((circleX, circleY, circleRadius))
    elif keys[K_r]:
        rectX, rectY = random.randint(10, 800), random.randint(10, 600)
        rectangle_list.append((rectX, rectY, rectWidth, rectHeight))
    elif keys[K_t]:
        trianglePoints = [(random.randint(10, 800), random.randint(10, 600)) for _ in range(3)]
        triangle_list.append(trianglePoints)
    elif keys[K_SPACE]:
        clear_screen = True
       
    if clear_screen:
        screen.fill(BLACK)
        show_green_circle = False
        show_blue_rectangle = False
        show_red_triangle = False
        clear_screen = False
        circle_list.clear()
        rectangle_list.clear()
        triangle_list.clear()
        
   

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    pygame.display.flip()
    clock.tick(60)
    
    
pygame.quit()
sys.exit()