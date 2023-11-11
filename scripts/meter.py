import random

import pygame


class Meter:
    mask: pygame.mask.MaskType
    texture: pygame.Surface
    animated_texture: pygame.Surface
    image: pygame.Surface
    filled_by: float

    def __init__(self, mask: pygame.mask.MaskType, texture: pygame.Surface):
        self.mask = mask
        self.texture = texture
        self.update(0)

    def animate(self):
        self.animated_texture = self.texture

    def update(self, filled_by):
        filled_by = min(max(filled_by, 0), 1)
        self.animate()
        surf_w, surf_h = self.mask.get_size()
        self.filled_by = filled_by
        self.image = pygame.Surface(self.mask.get_size())
        self.image.blit(self.animated_texture,
                        (0,
                         int(surf_h * (1 - filled_by))
                         )
                        )
        self.image = self.image.convert_alpha()
        for x in range(surf_w):
            for y in range(surf_h):
                if self.mask.get_at((x, y)) == 0:
                    self.image.set_at((x, y), pygame.Color(0, 0, 0, 0))

    def render(self, screen: pygame.Surface, at: tuple[int, int]):
        #self.update(self.filled_by)
        screen.blit(self.image, at)


class MeterWithBubbles(Meter):
    bubble: pygame.surface
    bubbles_pos: list[tuple[float, float]]

    def __init__(self, mask: pygame.mask.MaskType, texture: pygame.Surface, bubble: pygame.Surface, amount: int):
        self.bubble = bubble
        w, h = mask.get_size()
        self.bubbles_pos = list()
        for i in range(amount):
            self.bubbles_pos.append((w * random.random(), h / amount * i))
        super().__init__(mask, texture)

    def animate(self):
        self.animated_texture = self.texture.copy()
        for i in range(len(self.bubbles_pos)):
            self.animated_texture.blit(self.bubble, self.bubbles_pos[i])
            self.bubbles_pos[i] = ((self.bubbles_pos[i][0]+0.25*random.random())%self.mask.get_size()[0],
                                   (self.bubbles_pos[i][1]-0.25)%self.mask.get_size()[1])





