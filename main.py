import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((160, 90))
pygame.display.set_caption("Endless Fusion")
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load("sprites/playing board.png")
game_icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(game_icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(FPS)
