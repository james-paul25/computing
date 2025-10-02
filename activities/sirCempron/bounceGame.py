import pygame
from pygame.locals import *
import sys

pygame.init()

#COLORS
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MINT_GREEN = (152, 255, 152)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

HEIGHT, WIDTH = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Game")
clock = pygame.time.Clock()

#ball settings
ballX, ballY = WIDTH // 2, HEIGHT // 2
ballRadius = 20
ballDX, ballDY = 5, 5

#paddle settings
paddleWidth, paddleHeight = 100, 15
paddleX, paddleY = WIDTH // 2 - paddleWidth // 2, HEIGHT - 40
paddleSpeed = 10

#score
score = 0

#movements method
def movements(keys, paddleX):
    if keys[K_LEFT] and paddleX > 0:
        paddleX -= paddleSpeed
    if keys[K_RIGHT] and paddleX < WIDTH - paddleWidth:
        paddleX += paddleSpeed
    return paddleX

clock = pygame.time.Clock()
running = True
while running:
    
    screen.fill(BLACK)
    
    pygame.draw.circle(screen, PINK, (ballX, ballY), ballRadius)
    pygame.draw.rect(screen, YELLOW, (paddleX, paddleY, paddleWidth, paddleHeight))
    
    keys = pygame.key.get_pressed()
    paddleX = movements(keys, paddleX)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
     
    pygame.display.flip()
           