import asyncio
import pygame
from sys import exit
import scripts.pieces as pieces
import scripts.board as board
import scripts.config_manager as config_manager
import scripts.mouse as mouse_util
import scripts.pieces_queue as pieces_queue
from scripts.ability import Ability
from scripts.game_over import GameOverManager
from scripts.label import Label
from scripts.meter import MeterWithBubbles
from scripts.score import ScoreManager
from scripts.vfx import ParticleHandler
from scripts.time import Time

print("Loading the game...\nPlease wait. :)")
pygame.init()

config_manager.load()

final_screen = pygame.display.set_mode((160 * 6, 90 * 6), 0)

screen = pygame.Surface((160, 90))
pygame.display.set_caption("Endless Fusion")
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load("sprites/playing board.png")
order = pygame.image.load("sprites/order.png")
order_activated = pygame.image.load("sprites/order activated.png")

game_icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(game_icon)

font = pygame.font.Font('fonts/smallest_pixel-7.ttf', 10)
ParticleHandler().font = font
ScoreManager().label = Label(font, pygame.Color("0xbf3fb3"), (155, 2), "topright")
ScoreManager().score = 0

ability = Ability(20)

game_board = board.Board(ability)

p_queue = pieces_queue.PiecesQueue()

meter = MeterWithBubbles(pygame.mask.from_surface(pygame.image.load("sprites/meter/mask.png")),
                         pygame.image.load("sprites/meter/fluid.png"),
                         pygame.image.load("sprites/meter/bubble.png"), 5)

game_over_manager = GameOverManager()


def restart():
    print("Restart")
    ScoreManager().score = 0
    global ability
    ability.energy = 0
    global game_board
    del game_board.pieces
    game_board = board.Board(ability)
    game_over_manager.is_game_over = False
    global p_queue
    del p_queue
    p_queue = pieces_queue.PiecesQueue()


async def main():
    global background
    global order
    global order_activated
    global screen
    global clock
    global final_screen
    global ability
    global game_board
    global p_queue
    global meter

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if not game_over_manager.is_game_over:
                    pos = mouse_util.screen_to_game_pos(pygame.mouse.get_pos(), final_screen.get_size(),
                                                        screen.get_size())
                    grid_pos = mouse_util.game_to_board_pos(pos, (16, 16), (5, 5))
                    if mouse_util.check_if_in_bound(grid_pos, (4, 4)):
                        if not game_board.piece_exists_at_pos(grid_pos):
                            spawned_piece_type = p_queue.pop()
                            game_board.append_piece(pieces.Piece(spawned_piece_type, grid_pos[0], grid_pos[1]))
                    if 100 < pos[0] < 160:
                        if 31 < pos[1] < 91:
                            if ability.can_be_activated():
                                ability.reset()
                                game_board.upgrade_all()
                                print("ABILITY USED!!!!")
                elif game_over_manager.animation_complete():
                    restart()

        screen.fill("Black")
        screen.blit(background, (0, 0))

        meter.update(ability.get_coefficient())
        meter.render(screen, (94, 25))
        if not ability.can_be_activated():
            screen.blit(order, (100, 31))
        else:
            screen.blit(order_activated, (100, 31))
        ScoreManager().render(screen)
        ParticleHandler().update_and_render(screen)
        game_board.render(screen)

        p_queue.render(screen, (90, 3), 3)
        game_over_manager.render(screen)

        final_screen.blit(pygame.transform.scale(screen, final_screen.get_size()), (0, 0))
        pygame.display.update()

        Time.delta_time = clock.tick(FPS) / 1000
        await asyncio.sleep(0)


asyncio.run(main())
