import pygame
from pygame.locals import *
import sys
import random

pygame.init()

HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("October 3, 2025")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)


clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30, bold=True)
game_over = False

# methods to play game
def play_game(game_over):
    score = 0
    
    circleX, circleY = 250, 0
    circleRadius = 20
    circleDy = 3
    
    paddleWidth, paddleHeight = 100, 10
    paddleX, paddleY = (HEIGHT - paddleWidth) // 2, WIDTH - 50
    paddleSpeed = 5
    if not game_over:
        if keys[K_LEFT] and paddleX > 0:
            paddleX -= paddleSpeed
        if keys[K_RIGHT] and paddleX < WIDTH - paddleWidth:
            paddleX += paddleSpeed

    if not game_over:
        circleY += circleDy
    
        if circleY > WIDTH:
            game_over = True
            #circleY = 0
            #circleX = random.randint(circleRadius, HEIGHT - circleRadius)
        
        if (paddleY < circleY + circleRadius < paddleY + paddleHeight) and (paddleX < circleX < paddleX + paddleWidth):
            score += 1
            circleY = 0
            circleX = random.randint(circleRadius, WIDTH - circleRadius)  
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, GREEN, (paddleX, paddleY, paddleWidth, paddleHeight))
    
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))
    
    return game_over

running = True
while running:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if keys[K_SPACE]:
                game_over = play_game(game_over)
    
    if game_over:
        over_text = font.render("GAME OVER", True, RED)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(300)
    
pygame.quit()
sys.exit()