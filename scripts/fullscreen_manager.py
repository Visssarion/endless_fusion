import pygame
import scripts.config_manager as config_manager
from pygame._sdl2 import Window, WINDOWPOS_CENTERED

screen_x, screen_y = pygame.display.set_mode().get_size()

window = Window.from_display_module()


def exclusive_fullscreen():
    return pygame.display.set_mode((screen_x, screen_y), pygame.FULLSCREEN)


def maximized_window():
    final_screen = pygame.display.set_mode((screen_x, screen_y), pygame.NOFRAME)
    window.position = WINDOWPOS_CENTERED
    return final_screen


def windowed():
    screen_scale = (config_manager.config["screen"]["scale"], config_manager.config["screen"]["scale"])
    final_screen = pygame.display.set_mode((160 * screen_scale[0], 90 * screen_scale[1]), 0)
    window.position = WINDOWPOS_CENTERED
    return final_screen
