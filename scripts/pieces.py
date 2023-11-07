import pygame
from enum import Enum

_piece_sprites_dict = {
    "frog": pygame.image.load("sprites/pieces/frog.png"),
    "penguin": pygame.image.load("sprites/pieces/penguin.png"),
    "axolotl": pygame.image.load("sprites/pieces/axolotl.png"),
    "cat": pygame.image.load("sprites/pieces/cat.png"),
    "goat": pygame.image.load("sprites/pieces/goat.png"),
    "capybara": pygame.image.load("sprites/pieces/capybara.png")
}

_screen_offset_x = 5
_screen_offset_y = 5

_piece_width = 16
_piece_height = 16


def _to_screen_pos(x: int, y: int):
    return x * _piece_width + _screen_offset_x, y * _piece_height + _screen_offset_y


class PieceType(Enum):
    FROG = 0
    PENGUIN = 1
    AXOLOTL = 2
    CAT = 3
    GOAT = 4
    CAPYBARA = 5

    @staticmethod
    def from_string(name: str):
        match name:
            case "frog":
                return PieceType.FROG
            case "penguin":
                return PieceType.PENGUIN
            case "axolotl":
                return PieceType.AXOLOTL
            case "cat":
                return PieceType.CAT
            case "goat":
                return PieceType.GOAT
            case "capybara":
                return PieceType.CAPYBARA
            case _:
                raise KeyError("WRONG TYPE DURING CONVERSION OF STRING -> PIECE TYPE")

    def upgrade(self):
        return PieceType((self.value + 1) % 6)

    def to_string(self):
        match self.value:
            case 0:
                return "frog"
            case 1:
                return "penguin"
            case 2:
                return "axolotl"
            case 3:
                return "cat"
            case 4:
                return "goat"
            case 5:
                return "capybara"
            case _:
                raise KeyError("WRONG TYPE DURING CONVERSION OF PIECE TYPE -> STRING")


class Piece:
    image: pygame.Surface
    x: int
    y: int
    place_time: int
    piece_type: PieceType

    def __init__(self, piece_type: PieceType, x: int, y: int):
        self.place_time = pygame.time.get_ticks()
        self.image = _piece_sprites_dict[piece_type.to_string()]
        self.x = x
        self.y = y
        self.piece_type = piece_type

    def to_screen_pos(self):
        return _to_screen_pos(self.x, self.y)

