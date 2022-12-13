from functools import cmp_to_key
from ast import literal_eval


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_list_pairs(input: str) -> list[list]:
    return [[literal_eval(line) for line in pair.split("\n")] for pair in input.split("\n\n")]


def compare_pair(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    elif isinstance(left, list) and isinstance(right, list):
        for left_n, right_n in zip(left, right):
            result = compare_pair(left_n, right_n)
            if result != 0:
                return result
        return len(left) - len(right)

    else:
        return compare_pair([left], right) if isinstance(left, int) else compare_pair(left, [right])


def part1(pairs: list[list]) -> int:
    result = 0
    for pair_n, pair in enumerate(pairs):
        result += (compare_pair(pair[0], pair[1]) < 0) * (pair_n + 1)
    return result


def part2(pairs: list[list]) -> int:
    flatten = [element for pair in pairs for element in pair]
    sorted_list = sorted(flatten + [[[2]], [[6]]], key=cmp_to_key(compare_pair))
    return (sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1)


if __name__ == "__main__":
    input = load_input()
    pairs = parse_list_pairs(input)
    print(part1(pairs))
    print(part2(pairs))
