import pygame
from pygame.locals import *
from movements import moveCircle

pygame.init()

HEIGHT, WIDTH = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sep 25 Discussion")

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

rectangle = pygame.Rect(25,25, 10,10) # x, y, width, height


def resizeBiggerRectangle(rect):
    rect.width += 1
    rect.height += 1
    return rect

circleX, circleY = 80, 100

#main game loop
play = True
while play:
    screen.fill(GREEN)  # Fill the screen with yellow color
    
    
    pygame.draw.circle(screen, RED, (circleX, circleY), 25, ) # Draw the circle in red color
    pygame.draw.rect(screen, YELLOW, rectangle) # Draw the rectangle in yellow color
    
        
    keys = pygame.key.get_pressed()
    
    circleX, circleY = moveCircle(keys, circleX, circleY)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            play = False

    pygame.display.flip() # update the full display Surface to the screen, makes the changes visible 
    pygame.display.update() # update portions of the screen for software displays
    
pygame.quit()