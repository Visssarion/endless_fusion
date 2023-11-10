import math
import random

from scripts.pieces import PieceType, _piece_sprites_dict
import pygame
from math import cos, sin, radians, degrees, hypot, atan2

_particle_sprites_dict = {
    "frog": pygame.image.load("sprites/particles/particle_frog.png"),
    "penguin": pygame.image.load("sprites/particles/particle_penguin.png"),
    "axolotl": pygame.image.load("sprites/particles/particle_axolotl.png"),
    "cat": pygame.image.load("sprites/particles/particle_cat.png"),
    "goat": pygame.image.load("sprites/particles/particle_goat.png"),
    "capybara": pygame.image.load("sprites/particles/particle_capybara.png")
}


def _piece_type_to_particle_image(piece_type: PieceType) -> pygame.Surface:
    return _particle_sprites_dict[piece_type.to_string()]


class Particle:
    direction: float
    lifetime: float
    velocity: float
    acceleration: float
    image: pygame.Surface
    shrink: bool
    lifetime_left: float
    x: float
    y: float

    def __init__(self, image: pygame.Surface, pos: tuple[float, float], direction: float = 0, lifetime: float = 1,
                 velocity: float = 1, acceleration: float = 1, shrink: bool = True):
        self.image = image
        self.direction = direction
        self.lifetime = lifetime
        self.velocity = velocity
        self.acceleration = acceleration
        self.shrink = shrink
        self.lifetime_left = lifetime
        self.x = pos[0]
        self.y = pos[1]

    def update_and_render(self, delta_time: float, surface: pygame.Surface):
        if self.shrink:
            scale = max(self.lifetime_left / self.lifetime, 0)
            transformed_image = pygame.transform.scale_by(self.image, scale)
        else:
            transformed_image = self.image
        rect = transformed_image.get_rect()
        self.x += self.velocity * cos(radians(self.direction)) * delta_time
        self.y += self.velocity * sin(radians(self.direction)) * delta_time
        setattr(rect, "center", (self.x, self.y))
        self.velocity += self.acceleration * delta_time
        self.lifetime_left -= delta_time
        surface.blit(transformed_image, rect)

    def is_alive(self):
        return self.lifetime_left > 0

    @staticmethod
    def from_and_to(image: pygame.Surface, pos_from: tuple[float, float], pos_to: tuple[float, float],
                    lifetime: float = 1, shrink: bool = True):
        delta_x = (pos_to[0] - pos_from[0])
        delta_y = (pos_to[1] - pos_from[1])
        direction = degrees(atan2(delta_y, delta_x))
        delta_len = hypot(delta_x, delta_y)
        velocity = delta_len / lifetime / 3 * 2
        # len = v * t + (a * t ^ 2) / 2
        # a = v / t
        # len = v * t + v * t / 2 = v * t * (3 / 2)
        # v = len / t / 3 * 2
        return Particle(
            image, pos_from, direction,
            lifetime, velocity, velocity / lifetime, True
        )


class ParticleHandler:
    particle_list: list[Particle]

    def __init__(self):
        self.particle_list = list()

    def update_and_render(self, delta_time: float, surface: pygame.Surface):
        for particle in self.particle_list:
            particle.update_and_render(delta_time, surface)
        self.particle_list = [x for x in self.particle_list if x.is_alive()]

    def spawn_appearance_particles(self, piece_type: PieceType, pos: tuple[float, float]):
        for i in range(4):
            self.particle_list.append(Particle(
                _particle_sprites_dict[piece_type.to_string()], pos, random.random() * 90.0 + i * 90.0,
                1 + random.random() * 0.3, 30, -20, True
            ))

    def spawn_combining_particle(self, piece_type: PieceType,
                                 pos_from: tuple[float, float], pos_to: tuple[float, float]):
        self.particle_list.append(Particle.from_and_to(
            _piece_sprites_dict[piece_type.to_string()], pos_from, pos_to, 0.5, True
        ))
