import sys
from copy import deepcopy
from functools import reduce


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_map(input: str) -> tuple[list[list[int]], tuple[int], tuple[int]]:
    start = input.replace("\n", "").find("S")
    end = input.replace("\n", "").find("E")
    input = input.replace("S", "a").replace("E", "z")
    height_map = list(map(lambda line: list(map(lambda x: ord(x), line)), input.split("\n")))
    width = len(height_map[0])
    return height_map, (start // width, start % width), (end // width, end % width)


def solve(height_map: list[list[int]], start: tuple[int], end: tuple[int]) -> int:
    height = len(height_map)
    width = len(height_map[0])

    queue = [[start[0], start[1], 0]]
    visited = {start}

    while queue:
        curr_r, curr_c, curr_step = queue.pop()

        for next_r, next_c in [
            [curr_r + 1, curr_c],
            [curr_r - 1, curr_c],
            [curr_r, curr_c + 1],
            [curr_r, curr_c - 1],
        ]:
            if next_r >= height or next_r < 0 or next_c >= width or next_c < 0:
                continue

            if end and height_map[next_r][next_c] - height_map[curr_r][curr_c] > 1:
                continue

            if end is None and height_map[next_r][next_c] - height_map[curr_r][curr_c] < -1:
                continue

            if (next_r, next_c) == end:
                return curr_step + 1

            if end is None and height_map[next_r][next_c] == ord("a"):
                return curr_step + 1

            if (next_r, next_c) in visited:
                continue

            visited.add((next_r, next_c))
            queue = [[next_r, next_c, curr_step + 1]] + queue


if __name__ == "__main__":
    input = load_input()
    height_map, start, end = parse_map(input)
    print(solve(height_map, start, end))
    print(solve(height_map, end, None))
