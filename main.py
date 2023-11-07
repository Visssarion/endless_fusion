import pygame
from sys import exit
from os import environ
import scripts.pieces as pieces
import scripts.board as board
import scripts.config_manager as config_manager

pygame.init()

screen_x, screen_y = pygame.display.set_mode().get_size()

config_manager.load()

if config_manager.config["screen"]["fullscreen"]:
    if config_manager.config["screen"]["exclusive"]:
        final_screen = pygame.display.set_mode((screen_x, screen_y), pygame.FULLSCREEN)
    else:
        environ['SDL_VIDEO_CENTERED'] = '1'
        final_screen = pygame.display.set_mode((screen_x, screen_y), pygame.NOFRAME)
        print(final_screen.get_size())
else:
    environ['SDL_VIDEO_CENTERED'] = '0'
    screen_scale = (config_manager.config["screen"]["scale"], config_manager.config["screen"]["scale"])
    final_screen = pygame.display.set_mode((160 * screen_scale[0], 90 * screen_scale[1]), 0)

screen = pygame.Surface((160, 90))
pygame.display.set_caption("Endless Fusion")
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load("sprites/playing board.png")
game_icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(game_icon)

game_board = board.Board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            environ['SDL_VIDEO_CENTERED'] = '0'
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))

    game_board.append_piece(pieces.Piece(pieces.PieceType.GOAT, 2, 3))
    game_board.append_piece(pieces.Piece(pieces.PieceType.FROG, 1, 2))
    game_board.append_piece(pieces.Piece(pieces.PieceType.FROG, 1, 1))
    game_board.append_piece(pieces.Piece(pieces.PieceType.PENGUIN, 2, 1))

    game_board.render(screen)
    # final_screen.blit(pygame.transform.scale_by(screen, screen_scale), (0, 0))
    final_screen.blit(pygame.transform.scale(screen, final_screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
