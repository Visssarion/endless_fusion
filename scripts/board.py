from scripts.pieces import Piece, PieceType
import pygame


class Board:
    pieces: list

    def __init__(self):
        self.pieces = list()

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
        # WORSE PIECE OF FUNCTION I HAVE EVER WROTE
        # SHOULD HAVE WENT WITH MATRIX INSTEAD OF A LIST
        # THIS IS ACTUALLY STUPID
        # BUT IT DOES WORK!

        # ALSO, SINCE INDEX OF THE LIST INCREASES WITH THE TIME OF THE PIECE'S CREATION
        # Piece.place_time IS NEVER USED
        # INSTEAD I JUST SORT BY BIGGEST INDEX TO GET THE NEWEST PIECE

        # xoxo -vissa

        for i in range(len(self.pieces)):
            current: Piece = self.pieces[i]
            try:
                upper = self.pieces.index(Piece(current.piece_type, current.x, current.y - 1))
            except ValueError:
                upper = -1
            try:
                lower = self.pieces.index(Piece(current.piece_type, current.x, current.y + 1))
            except ValueError:
                lower = -1
            try:
                left = self.pieces.index(Piece(current.piece_type, current.x - 1, current.y))
            except ValueError:
                left = -1
            try:
                right = self.pieces.index(Piece(current.piece_type, current.x + 1, current.y))
            except ValueError:
                right = -1

            #print([i, left, right, upper, lower])

            if right != -1 and left != -1:
                indexes = [i, left, right]
                indexes.sort(reverse=True)

                new_piece = Piece(self.pieces[indexes[0]].piece_type.upgrade(), self.pieces[indexes[0]].x, self.pieces[indexes[0]].y)

                for index in indexes:
                    self.pieces.pop(index)

                self.append_piece(new_piece)
                return

            elif upper != -1 and lower != -1:
                indexes = [i, upper, lower]
                indexes.sort(reverse=True)

                new_piece = Piece(self.pieces[indexes[0]].piece_type.upgrade(), self.pieces[indexes[0]].x, self.pieces[indexes[0]].y)

                for index in indexes:
                    self.pieces.pop(index)

                self.append_piece(new_piece)
                return

            """
        try:
            print(self.pieces.index(Piece(PieceType.FROG, 1, 1)))
        except ValueError:
            print(False)
            """
