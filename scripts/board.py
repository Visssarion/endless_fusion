from scripts.pieces import Piece, PieceType
import pygame


class Board:
    pieces: list

    def __init__(self):
        self.pieces = list()

    def append_piece(self, piece: Piece):
        self.pieces.append(piece)

    def render(self, display: pygame.Surface):
        for piece in self.pieces:
            display.blit(piece.image, piece.to_screen_pos())

    def piece_exists_at_pos(self, pos: tuple[int, int]) -> bool:
        for piece in self.pieces:
            if piece.x == pos[0] and piece.y == pos[1]:
                return True
        return False
