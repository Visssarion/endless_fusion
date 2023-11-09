class PieceCombined:
    my_index: int
    # indexes of compatible neighbors
    vertical_neighbors: list
    horizontal_neighbors: list

    score_three_in_a_row = 1
    score_four_in_a_row = 3
    score_five_in_a_row = 5

    def __init__(self, index: int):
        self.my_index = index

    def calculate_score(self):
        score: int = 0
        had_vertical_combining = True
        if len(self.vertical_neighbors) >= 4:
            score += self.score_five_in_a_row
        elif len(self.vertical_neighbors) >= 3:
            score += self.score_four_in_a_row
        elif len(self.vertical_neighbors) >= 2:
            score += self.score_three_in_a_row
        else:
            had_vertical_combining = False

        had_horizontal_combining = True
        if len(self.horizontal_neighbors) >= 4:
            score += self.score_five_in_a_row
        elif len(self.horizontal_neighbors) >= 3:
            score += self.score_four_in_a_row
        elif len(self.horizontal_neighbors) >= 2:
            score += self.score_three_in_a_row
        else:
            had_horizontal_combining = False

        if had_horizontal_combining and had_vertical_combining:
            score += 2

        return score

    def __gt__(self, other):
        return self.calculate_score() > other.calculate_score()