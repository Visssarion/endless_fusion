import pygame

from scripts.label import Label
from scripts.vfx import ParticleHandler


class ScoreManager:
    label: Label
    particle_handler: ParticleHandler
    _score: int = 0

    def __init__(self, label: Label, particle_handler: ParticleHandler):
        self.label = label
        self.particle_handler = particle_handler
        self.score = 0

    # plain attributes
    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score: int):
        self.particle(score - self._score)
        self._score = score
        self.label.update(str(self._score))

    def render(self, surface: pygame.Surface):
        self.label.render(surface)

    def particle(self, delta_score):
        self.particle_handler.score_particle(delta_score)