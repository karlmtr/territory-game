import pygame
from territory.game import Game

pygame.init()
COLS = 38
ROWS = 50
WIDTH, HEIGHT = 10*COLS, 10*ROWS
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
timer = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game = Game(WIDTH, HEIGHT, ROWS , COLS, 1)
run = True
while run:
    screen.fill(black)
    game.draw(screen)
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
