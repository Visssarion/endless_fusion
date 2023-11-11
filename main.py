import pygame
from sys import exit
import scripts.pieces as pieces
import scripts.board as board
import scripts.config_manager as config_manager
import scripts.fullscreen_manager as fullscreen_manager
import scripts.mouse as mouse_util
import scripts.pieces_queue as pieces_queue
from scripts.label import Label
from scripts.meter import MeterWithBubbles
from scripts.score import ScoreManager
from scripts.vfx import ParticleHandler

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
order = pygame.image.load("sprites/order.png")
game_icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(game_icon)

font = pygame.font.Font('fonts/smallest_pixel-7.ttf', 10)
particle_handler = ParticleHandler(font)
score_manager = ScoreManager(Label(font, pygame.Color("0xbf3fb3"), (155, 2), "topright"),
                             particle_handler)

game_board = board.Board(score_manager, particle_handler)

p_queue = pieces_queue.PiecesQueue()

delta_time = 0

meter = MeterWithBubbles(pygame.mask.from_surface(pygame.image.load("sprites/meter/mask.png")),
                         pygame.image.load("sprites/meter/fluid.png"),
                         pygame.image.load("sprites/meter/bubble.png"), 5)

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
                    spawned_piece_type = p_queue.pop()
                    game_board.append_piece(pieces.Piece(spawned_piece_type, grid_pos[0], grid_pos[1]))

    screen.fill("Black")
    screen.blit(background, (0, 0))

    meter.update((score_manager.score % 50)/50)
    meter.render(screen, (94, 25))
    screen.blit(order, (100, 31))
    score_manager.render(screen)
    particle_handler.update_and_render(delta_time, screen)
    game_board.render(screen)

    p_queue.render(screen, (90, 3), 3)

    final_screen.blit(pygame.transform.scale(screen, final_screen.get_size()), (0, 0))
    pygame.display.update()

    delta_time = clock.tick(FPS) / 1000
