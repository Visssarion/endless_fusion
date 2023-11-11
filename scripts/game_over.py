import pygame

from scripts.singleton import Singleton
from scripts.time import Time


class GameOverManager(metaclass=Singleton):
    is_game_over: bool = False
    coefficient: float = 0.0
    time: float = 1.0
    game_over_screen: pygame.Surface = pygame.image.load("sprites/game over.png")

    def render(self, screen: pygame.Surface):
        if self.is_game_over:
            delta_time = Time.delta_time
            transparent_vignette: pygame.Surface = self.game_over_screen.copy().convert_alpha()
            transparent_vignette.set_alpha(int(255 * self.coefficient))
            screen.blit(transparent_vignette, (0, 0))

            self.coefficient += delta_time / self.time
            self.coefficient = max(min(self.coefficient, 1), 0)
