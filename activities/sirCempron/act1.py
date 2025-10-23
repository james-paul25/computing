import pygame
from pygame.locals import *
import sys

pygame.init()
font = pygame.font.SysFont("Arial",12, bold=True)

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((800, 600))


red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)


rect = pygame.Rect(50, 50, 100, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, red, rect)
    pygame.draw.circle(screen, blue, (300, 150), 40)
    
    pygame.draw.polygon(screen, green, [(500, 200), (550, 250), (450, 250)])
    
    rect_text = font.render("Rect[50,50,100,60]", True, black)
    screen.blit(rect_text, (55, 150))
    
    circle_text = font.render("Circle[300, 100 n=40]", True, black)
    screen.blit(rect_text, (250, 200))
    
    triangle_text = font.render("Triangle", True, black)
    screen.blit(triangle_text, (480, 270))
    
    zero_text = font.render("[0,0]", True, black)
    screen.blit(zero_text, (0,0))


    pygame.display.flip()

pygame.quit()
sys.exit()
