import pygame


class Label:

    antialias = False
    anchor = "topright"
    font: pygame.font.Font
    image : pygame.Surface
    text: str
    color: pygame.Color
    position: tuple[int, int]
    rect: pygame.Rect

    def __init__(self, font, color, position):
        self.font = font
        self.color = color
        self.position = position
        self.update("")

    def update(self, text):
        self.image = self.font.render(text, self.antialias, self.color)
        self.rect = self.image.get_rect()
        setattr(self.rect, self.anchor, self.position)

    def render(self, surface):
        surface.blit(self.image, self.rect)

