import pygame
from pygame.locals import *
import sys
from gameMethods import moveCircle

#to initialize pygame
pygame.init()

#to set the dimensions of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#to create the window/screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#to set the title of the window
pygame.display.set_caption("Practice Game")

# ----------- after this you can any methods you want -------------- just make sure to put them before the game loop

#to make rectangle
rect = pygame.Rect(100, 100, 50,50) # x, y, width, height

# initial position of circle
circle_x = 100
circle_y = 200


#to make circle -> pygame.draw.circle(surface, color, center, radius, width=0)
circle = pygame.draw.circle(screen, (255,0,0), (100,200), 50, 5) # red color

play = True
#game loop
while play:
    
    screen.fill((0, 0, 0))  # Fill the screen with white black color
    
    #to display the rectangle
    #pygame.draw.rect(screen, (255, 0, 0), rect) # Red color
    
    pygame.draw.circle(screen, (255,0,0), (circle_x, circle_y), 30) # red color
    
    #key pressed
    keys = pygame.key.get_pressed()
    # call the move_circle method
    circle_x, circle_y = moveCircle(keys, circle_x, circle_y)
    
    #to check for events
    for event in pygame.event.get():
        #to check if the user wants to quit
        if event.type == QUIT:
            play = False    
            pygame.quit()
            sys.exit()


    #to update the display
    pygame.display.update()
