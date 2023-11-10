import pygame


class Label:
    antialias = False
    anchor: str
    font: pygame.font.Font
    image: pygame.Surface
    text: str
    color: pygame.Color
    position: tuple[int, int]
    rect: pygame.Rect

    def __init__(self, font: pygame.font.Font, color: pygame.Color, position: tuple[int, int], anchor: str = "topleft"):
        self.font = font
        self.color = color
        self.position = position
        self.anchor = anchor
        self.update("")
        self.rect: pygame.rect

    def update(self, text):
        self.image = self.font.render(text, self.antialias, self.color)
        self.rect = self.image.get_rect()
        setattr(self.rect, self.anchor, self.position)

    def render(self, surface):
        surface.blit(self.image, self.rect)
