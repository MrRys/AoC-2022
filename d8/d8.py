def load_input() -> str:
    with open("d8\input.txt") as src_file:
        return src_file.read().strip()


def parse_forest(input: str) -> list[list[int]]:
    return list(
        map(lambda line: list(map(lambda tree: int(tree), line)), input.split("\n"))
    )


def solve1(forest: list[list[int]]) -> int:
    len_y = len(forest)
    len_x = len(forest[0])
    visible = [[False for _ in range(len_x)] for _ in range(len_y)]

    for y in range(1, len(forest) - 1):
        max_size = forest[y][0]
        for x in range(1, len(forest[0]) - 1):
            if max_size < forest[y][x]:
                visible[y][x] = True
                max_size = forest[y][x]

    for y in range(1, len(forest) - 1):
        max_size = forest[y][len(forest[0]) - 1]
        for x in reversed(range(1, len(forest[0]) - 1)):
            if max_size < forest[y][x]:
                visible[y][x] = True
                max_size = forest[y][x]

    for x in range(1, len(forest[0]) - 1):
        max_size = forest[0][x]
        for y in range(1, len(forest) - 1):
            if max_size < forest[y][x]:
                visible[y][x] = True
                max_size = forest[y][x]

    for x in range(1, len(forest[0]) - 1):
        max_size = forest[len(forest) - 1][x]
        for y in reversed(range(1, len(forest) - 1)):
            if max_size < forest[y][x]:
                visible[y][x] = True
                max_size = forest[y][x]

    return (
        sum(map(lambda line: sum(line), visible))
        + len_x * len_y
        - (len_x - 2) * (len_y - 2)
    )


def check_left(forest, start, end):
    result = 0
    for i in reversed(range(start, end)):

        if forest[i] < forest[end]:
            result += 1
        if forest[i] >= forest[end]:
            result += 1
            break
    return result


def check_right(forest, start, end):
    result = 0
    for i in range(start, end):
        if forest[i] < forest[start - 1]:
            result += 1
        if forest[i] >= forest[start - 1]:
            result += 1
            break
    return result


def check_up(forest, x, start, end):
    result = 0
    for i in reversed(range(start, end)):
        if forest[i][x] < forest[end][x]:
            result += 1
        if forest[i][x] >= forest[end][x]:
            result += 1
            break

    return result


def check_down(forest, x, start, end):
    result = 0
    for i in range(start, end):
        if forest[i][x] < forest[start - 1][x]:
            result += 1
        if forest[i][x] >= forest[start - 1][x]:
            result += 1
            break
    return result


def solve2(forest: list[list[int]]) -> int:

    len_y = len(forest)
    len_x = len(forest[0])
    visible = [[0 for _ in range(len_x)] for _ in range(len_y)]
    for y in range(1, len_y - 1):
        for x in range(1, len_x - 1):
            left = check_left(forest[y], 0, x)
            right = check_right(forest[y], x + 1, len_x)
            visible[y][x] = left * right

    for x in range(1, len_x - 1):
        for y in range(1, len_y - 1):
            up = check_up(forest, x, 0, y)
            down = check_down(forest, x, y + 1, len_y)
            visible[y][x] *= up * down

    return max(map(lambda line: max(line), visible))


if __name__ == "__main__":
    input = load_input()
    forest = parse_forest(input)
    print(solve1(forest))
    print(solve2(forest))
