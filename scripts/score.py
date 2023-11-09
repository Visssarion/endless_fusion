import pygame

from scripts.label import Label


class ScoreManager:
    label: Label

    def __init__(self, label: Label):
        self.label = label
        self.score = 0

    # plain attributes
    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score
        self.label.update(str(self._score))

    def render(self, surface: pygame.Surface):
        self.label.render(surface)
