from functools import cmp_to_key
from ast import literal_eval


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_list_pairs(input: str) -> list[list]:
    return [[literal_eval(line) for line in pair.split("\n")] for pair in input.split("\n\n")]


def check_pair(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):
        for left_n, right_n in zip(left, right):
            result = check_pair(left_n, right_n)
            if result != 0:
                return result

        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0

    else:
        return check_pair([left], right) if isinstance(left, int) else check_pair(left, [right])


def solve(pairs: list[list]) -> int:
    result = 0
    for pair_n, pair in enumerate(pairs):
        check = check_pair(pair[0], pair[1])
        if check > 0:
            result += (pair_n + 1) * check
    return result


if __name__ == "__main__":
    input = load_input()
    pairs = parse_list_pairs(input)
    print(solve(pairs))

    flatten = [element for pair in pairs for element in pair]
    sorted_list = sorted(flatten + [[[2]], [[6]]], key=cmp_to_key(check_pair), reverse=True)
    print((sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1))
