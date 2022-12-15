import numpy as np
from copy import deepcopy


MAP_WIDTH = 675
MAP_HEIGHT = 171
SAND_START_X = 500


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_rocks(input: str) -> list[list[int]]:
    return [
        [[int(rock.split(",")[1]), int(rock.split(",")[0])] for rock in rock_path.split(" -> ")]
        for rock_path in input.splitlines()
    ]


def sort_coord(start: list[int], end: list[int]) -> tuple[list[int]]:
    if start[0] > end[0]:
        start[0], end[0] = end[0], start[0]
    if start[1] > end[1]:
        start[1], end[1] = end[1], start[1]
    return start, end


def generate_rock_map(rocks: list[list[int]]) -> np.ndarray:
    rock_map = np.array([["." for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)])

    for rock_formation in rocks:
        num_rocks = len(rock_formation)
        for coord_idx in range(1, num_rocks):
            start = rock_formation[coord_idx - 1]
            end = rock_formation[coord_idx]
            start, end = sort_coord(start.copy(), end.copy())
            rock_map[start[0] : end[0] + 1, start[1] : end[1] + 1].fill("#")

    return rock_map


def generate_floor(rock_map: np.ndarray) -> None:
    for idx in reversed(range(len(rock_map))):
        if "#" in rock_map[idx]:
            rock_map[idx + 2].fill("#")
            break


def solve(rock_map: np.ndarray) -> int:
    start_y = np.where(rock_map[:, SAND_START_X] == "#")[0][0]
    start_x = SAND_START_X
    landed = 0
    move_up = True

    while True:
        start_y -= move_up

        sand_y, sand_x = start_y, start_x
        move_up = True

        while True:
            if sand_y + 1 >= MAP_HEIGHT or sand_y < 0 or sand_x + 1 >= MAP_WIDTH or sand_x - 1 < 0:
                return landed

            if rock_map[sand_y + 1][sand_x] == ".":
                sand_y = sand_y + 1
                move_up = False
            elif rock_map[sand_y + 1][sand_x - 1] == ".":
                sand_y, sand_x = sand_y + 1, sand_x - 1
                move_up = False
            elif rock_map[sand_y + 1][sand_x + 1] == ".":
                sand_y, sand_x = sand_y + 1, sand_x + 1
                move_up = False
            else:
                rock_map[sand_y][sand_x] = "o"
                landed += 1
                break


if __name__ == "__main__":
    input = load_input()
    rocks = parse_rocks(input)
    rock_map = generate_rock_map(rocks)
    print(solve(deepcopy(rock_map)))
    generate_floor(rock_map)
    print(solve(deepcopy(rock_map)))
