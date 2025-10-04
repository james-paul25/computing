import pygame
from pygame.locals import *
import sys
import random

pygame.init()

HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("REACT FAST")


circleX, circleY = 250, 0
circleRadius = 20
circleDy = 5

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

paddleWidth, paddleHeight = 100, 10
paddleX, paddleY = (HEIGHT - paddleWidth) // 2, WIDTH - 50

score = 0
font = pygame.font.SysFont("Arial", 30, bold=True)
gameOver = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddleX > 0:
        paddleX -= 3
    if keys[K_RIGHT] and paddleX < HEIGHT - paddleWidth:
        paddleX += 3

    circleY += circleDy
    if circleY > WIDTH:
        circleY = 0
        circleX = random.randint(circleRadius, HEIGHT - circleRadius)

    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, GREEN, (paddleX, paddleY, paddleWidth, paddleHeight))

    if (paddleY < circleY + circleRadius < paddleY + paddleHeight) and (paddleX < circleX < paddleX + paddleWidth):
        score += 1
        circleY = 0
        circleX = random.randint(circleRadius, HEIGHT - circleRadius)  
        
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    
pygame.quit()
sys.exit()