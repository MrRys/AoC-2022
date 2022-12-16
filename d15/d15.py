import sys
from collections import defaultdict
import re


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def in_range(sensors: defaultdict, x: int, y: int) -> bool:
    for sensor in sensors:
        dist = sensors[sensor]
        if dist >= manhattan(sensor[0], sensor[1], x, y):
            return True
    return False


def parse_input(input: str) -> tuple[defaultdict, set, int, int]:
    sensors = defaultdict(lambda: 0)
    beacons = set()
    min_x = sys.maxsize
    max_x = max_dist = -sys.maxsize
    for line in input.split("\n"):
        x1, y1, x2, y2 = list(map(lambda x: int(x), re.findall(r"-?[0-9]+", line)))
        dist = manhattan(x1, y1, x2, y2)
        sensors[(x1, y1)] = dist
        beacons.add((x2, y2))

        min_x = min(min_x, x1, x2)
        max_x = max(max_x, x1, x2)
        max_dist = max(max_dist, x1, x2)
    return sensors, beacons, min_x - max_dist, max_x + max_dist


def part1(sensors: defaultdict, beacons: int, min_x: int, max_x: int, pos_y: int) -> int:
    impossible = set()

    for x in range(min_x, max_x + 1):
        for sensor in sensors:
            dist = sensors[sensor]
            if dist < manhattan(sensor[0], sensor[1], x, pos_y) or (x, pos_y) in beacons:
                continue
            impossible.add(x)

    return len(impossible)


def part2(sensors: defaultdict, limit: int) -> int:
    points = defaultdict(lambda: 0)

    for sensor in sensors:
        dist = sensors[sensor]
        pos_x1 = (sensor[0] + dist + 1, sensor[1])
        pos_y1 = (sensor[0], sensor[1] + dist + 1)
        pos_x2 = (sensor[0] - dist - 1, sensor[1])
        pos_y2 = (sensor[0], sensor[1] - dist - 1)
        x = pos_x1[0]
        y = pos_x1[1]

        for (x_sign, y_sign, pos) in [(-1, 1, pos_y1), (-1, -1, pos_x2), (1, -1, pos_y2), (1, 1, pos_x1)]:
            while (x, y) != pos:
                x += x_sign
                y += y_sign
                if 0 <= x <= limit and 0 <= y <= limit and not in_range(sensors, x, y):
                    points[(x, y)] += 1
                    if points[(x, y)] == 4:
                        return x * 4000000 + y


if __name__ == "__main__":
    input = load_input()
    sensors, beacons, min_x, max_x = parse_input(input)
    print(part1(sensors, beacons, min_x, max_x, 2000000))
    print(part2(sensors, 4000000))
