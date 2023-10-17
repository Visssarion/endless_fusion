import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Endless Fusion")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        pygame.display.update()