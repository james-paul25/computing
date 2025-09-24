import pygame
from pygame.locals import *
import sys

#to initialize pygame
pygame.init()

#to set the dimensions of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#to create the window/screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#to set the title of the window
pygame.display.set_caption("Practice Game")

#to make rectangle
rect = pygame.Rect(100, 100, 50,50) # x, y, width, height

#to make circle -> pygame.draw.circle(surface, color, center, radius, width=0)
circle = pygame.draw.circle(screen, (255,0,0), (100,200), 50, 5) # red color


play = True

#game loop
while play:
    
    screen.fill((0, 0, 0))  # Fill the screen with white black color
    
    #to display the rectangle
    pygame.draw.rect(screen, (255, 0, 0), rect) # Red color
    
    #pygame.draw.circle(screen, (255,0,0), (100,200), 50, 0)
    
    #key pressed
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        rect.y -= 1  # Move up
    elif keys[K_s]:
        rect.y += 1  # Move down
    elif keys[K_a]:
        rect.x -= 1  # Move left
    elif keys[K_d]:
        rect.x += 1  # Move right
    
    #to check for events
    for event in pygame.event.get():
        #to check if the user wants to quit
        if event.type == QUIT:
            play = False    
            pygame.quit()
            sys.exit()


    #to update the display
    pygame.display.update()
