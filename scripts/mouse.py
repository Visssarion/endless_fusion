from math import floor


def screen_to_game_pos(pos: tuple[int, int], screen_size: tuple[int, int],
                       game_size: tuple[int, int]) -> tuple[int, int]:
    return int(pos[0] / screen_size[0] * game_size[0]), int(pos[1] / screen_size[1] * game_size[1])


def game_to_board_pos(pos: tuple[int, int], tile_size: tuple[int, int],
                      board_offset: tuple[int, int]) -> tuple[int, int]:
    return floor((pos[0] - board_offset[0]) / tile_size[0]), floor((pos[1] - board_offset[1]) / tile_size[1])


def check_if_in_bound(pos: tuple[int, int], finish: tuple[int, int],
                      start: tuple[int, int] = (0, 0)) -> bool:
    return start[0] <= pos[0] <= finish[0] and start[1] <= pos[1] <= finish[1]