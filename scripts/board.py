from scripts.pieces import Piece, PieceType
import pygame
from scripts.board_combining_util import PieceCombined
from scripts.score import ScoreManager


class Board:
    pieces: list
    score: ScoreManager

    def __init__(self, score: ScoreManager):
        self.pieces = list()
        self.score = score

    def append_piece(self, piece: Piece):
        self.pieces.append(piece)
        self.update()

    def render(self, display: pygame.Surface):
        for piece in self.pieces:
            display.blit(piece.image, piece.to_screen_pos())

    def piece_exists_at_pos(self, pos: tuple[int, int]) -> bool:
        for piece in self.pieces:
            if piece.x == pos[0] and piece.y == pos[1]:
                return True
        return False

    def update(self):
        calculated_list: list = list()
        for i in range(len(self.pieces)):
            calculated = PieceCombined(i)
            piece_type: PieceType = self.pieces[i].piece_type
            x: int = self.pieces[i].x
            y: int = self.pieces[i].y

            calculated.vertical_neighbors = self.__vertical_neighbors_of_a_piece(piece_type, x, y)
            calculated.horizontal_neighbors = self.__horizontal_neighbors_of_a_piece(piece_type, x, y)
            calculated_list.append(calculated)

        best_combo: PieceCombined = max(calculated_list)

        if best_combo.calculate_score() > 0:
            self.score.score += best_combo.calculate_score()
            indexes: list = [best_combo.my_index] + best_combo.vertical_neighbors + best_combo.horizontal_neighbors
            indexes.sort(reverse=True)
            new_piece = Piece(self.pieces[indexes[0]].piece_type.upgrade(), self.pieces[indexes[0]].x,
                              self.pieces[indexes[0]].y)
            for index in indexes:
                self.pieces.pop(index)
            self.append_piece(new_piece)
            self.update()
            return
        else:
            if len(self.pieces) >= 25:
                self.game_over()

    def __vertical_neighbors_of_a_piece(self, piece_type: PieceType, x: int, y: int) -> list:
        result = list()
        try:
            result.append(self.pieces.index(Piece(piece_type, x, y + 1)))
            result.append(self.pieces.index(Piece(piece_type, x, y + 2)))
        except ValueError:
            pass
        try:
            result.append(self.pieces.index(Piece(piece_type, x, y - 1)))
            result.append(self.pieces.index(Piece(piece_type, x, y - 2)))
        except ValueError:
            pass
        return result

    def __horizontal_neighbors_of_a_piece(self, piece_type: PieceType, x: int, y: int) -> list:
        result = list()
        try:
            result.append(self.pieces.index(Piece(piece_type, x + 1, y)))
            result.append(self.pieces.index(Piece(piece_type, x + 2, y)))
        except ValueError:
            pass
        try:
            result.append(self.pieces.index(Piece(piece_type, x - 1, y)))
            result.append(self.pieces.index(Piece(piece_type, x - 2, y)))
        except ValueError:
            pass
        return result

    def game_over(self):
        print("GAME OVER")