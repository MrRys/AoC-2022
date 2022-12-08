import sys


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_pairs(input: str) -> list[list[int]]:
    return list(
        map(lambda x: list(map(lambda y: int(y), x.split(","))), input.replace("-", ",").split("\n"))
    )


def check_overlap(pair: list[int], indexes: list[int]) -> bool:
    return (pair[indexes[0]] - pair[indexes[1]]) * (pair[indexes[2]] - pair[indexes[3]]) <= 0


def solve(pairs: list[list[int]], indexes: list[int]):
    return sum(map(lambda x: check_overlap(x, indexes), pairs))


if __name__ == "__main__":
    input = load_input()
    pairs = parse_pairs(input)
    print(solve(pairs, [0, 2, 1, 3]))
    print(solve(pairs, [0, 3, 1, 2]))