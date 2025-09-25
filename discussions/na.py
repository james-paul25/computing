import pygame
from pygame.locals import *
from movements import moveCircle

pygame.init()


HEIGHT, WIDTH = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sparringggg")  

PURPLE = (128, 0, 128)
RED = (255, 0, 0)

triangle_points = [(550,50), (600,150), (500, 150)]  # Define the three points of the triangle
pentagon_points = [(650, 200), (680, 250), (665, 280), (635, 280), (620, 250)]  # Define the five points of the pentagon

circleX, circleY = 80, 100



running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black color
    
    # draw triangle
    pygame.draw.polygon(screen, (0, 255, 0), triangle_points) 
    
    # draw circle
    pygame.draw.circle(screen, RED, (circleX, circleY), 20)  
    
    keys = pygame.key.get_pressed()
    
    # to move circle
    circleX, circleY = moveCircle(keys, circleX, circleY)
    
    # draw a pentagon
    pygame.draw.polygon(screen, PURPLE, pentagon_points, 2) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()  # Update the full display Surface to the screen
    pygame.display.update()  # Update portions of the screen for software displays