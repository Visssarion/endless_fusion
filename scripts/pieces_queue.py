from collections import deque
import random

import pygame.transform

from scripts.pieces import PieceType, _piece_sprites_dict


class PiecesQueue:
    starting_queue: deque = deque()
    random_queue: deque = deque()
    random_queue_size: int = 5

    def fill_starting_queue(self):
        for piece in [PieceType.FROG] * 5:
            self.starting_queue.append(piece)
        for piece in range(3):
            self.starting_queue.append(PieceType(random.randint(0, 1)))
        for piece in [PieceType.PENGUIN] * 2:
            self.starting_queue.append(piece)
        for piece in [PieceType.AXOLOTL] * 2:
            self.starting_queue.append(piece)
        for piece in range(4):
            self.starting_queue.append(PieceType(random.randint(0, 2)))
        for piece in [PieceType.CAT] * 3:
            self.starting_queue.append(piece)
        for piece in range(5):
            self.starting_queue.append(PieceType(random.randint(0, 3)))

    def fill_random_queue(self):
        while len(self.random_queue) < self.random_queue_size:
            self.random_queue.append(PieceType(random.randint(0, 5)))

    def __init__(self):
        self.fill_starting_queue()
        self.fill_random_queue()

    def pop(self):
        if self.starting_queue:
            return self.starting_queue.popleft()
        else:
            result = self.random_queue.popleft()
            self.fill_random_queue()
            return result

    def look_at(self, index):
        combined_queue = self.starting_queue + self.random_queue
        return combined_queue[index]

    def render(self, screen: pygame.Surface, pos: tuple[int, int], amount=1):
        piece_type = self.look_at(0)
        piece_image: pygame.Surface = _piece_sprites_dict[piece_type.to_string()]
        screen.blit(piece_image, pos)
        pos = (pos[0]+piece_image.get_size()[0], pos[1])
        for i in range(amount-1):
            piece_type = self.look_at(i+1)
            piece_image = _piece_sprites_dict[piece_type.to_string()]
            final_image = pygame.transform.scale_by(piece_image, 0.6)
            screen.blit(final_image, (pos[0]+(final_image.get_size()[0]+0.6)*i, pos[1]))
            # alternative/previous size = 0.5. current - 0.6


"""
        while not self.starting_queue.empty():
            print(self.starting_queue.get())
"""