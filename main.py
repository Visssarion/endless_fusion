import pygame
from sys import exit
import scripts.pieces as pieces
import scripts.board as board
import scripts.config_manager as config_manager
import scripts.fullscreen_manager as fullscreen_manager
import scripts.mouse as mouse_util
import scripts.pieces_queue as pieces_queue

print("Loading the game...\nPlease wait. :)")
pygame.init()

config_manager.load()

if config_manager.config["screen"]["fullscreen"]:
    if config_manager.config["screen"]["exclusive"]:
        final_screen = fullscreen_manager.exclusive_fullscreen()
    else:
        final_screen = fullscreen_manager.maximized_window()
else:
    final_screen = fullscreen_manager.windowed()

screen = pygame.Surface((160, 90))
pygame.display.set_caption("Endless Fusion")
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load("sprites/playing board.png")
game_icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(game_icon)

game_board = board.Board()

p_queue = pieces_queue.PiecesQueue()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = mouse_util.screen_to_game_pos(pygame.mouse.get_pos(), final_screen.get_size(), screen.get_size())
            grid_pos = mouse_util.game_to_board_pos(pos, (16, 16), (5, 5))
            if mouse_util.check_if_in_bound(grid_pos, (4, 4)):
                if not game_board.piece_exists_at_pos(grid_pos):
                    game_board.append_piece(pieces.Piece(p_queue.pop(), grid_pos[0], grid_pos[1]))

    screen.blit(background, (0, 0))

    game_board.render(screen)

    p_queue.render(screen, (90, 3), 0.5, 1, 3)

    final_screen.blit(pygame.transform.scale(screen, final_screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
