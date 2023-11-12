import pygame
from pygame.math import lerp

from scripts.singleton import Singleton
from scripts.time import Time


class GameOverManager(metaclass=Singleton):
    is_game_over: bool = False
    coefficient: float = 0.0
    time: float = 1.5
    game_over_screen: pygame.Surface = pygame.image.load("sprites/game over.png")

    def render(self, screen: pygame.Surface):
        if self.is_game_over:
            delta_time = Time.delta_time
            final_image: pygame.Surface = self.game_over_screen.copy().convert_alpha()
            final_image.set_alpha(int(255 * self.coefficient))

            final_image = pygame.transform.scale_by(final_image, lerp(4, 1, self.coefficient**2))

            rect = final_image.get_rect()
            setattr(rect, "center", (80, 45))

            screen.blit(final_image, rect)

            self.coefficient += delta_time / self.time
            self.coefficient = max(min(self.coefficient, 1), 0)
        else:
            self.coefficient = 0

    def animation_complete(self):
        return self.coefficient >= 1.0
