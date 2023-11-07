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
