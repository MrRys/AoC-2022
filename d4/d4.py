import re


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_elf_pairs(input: str) -> list[list[int]]:
    return list(map(lambda x: list(map(lambda y: int(y), re.split(r",|-", x))), input.split("\n")))


def check_overlap(pair: list[int], idx: list[int]) -> bool:
    return (pair[idx[0]] - pair[idx[1]]) * (pair[idx[2]] - pair[idx[3]]) <= 0


def solve(pairs: list[list[int]], idx: list[int]):
    return sum(map(lambda pair: check_overlap(pair, idx), pairs))


if __name__ == "__main__":
    input = load_input()
    pairs = parse_elf_pairs(input)
    print(solve(pairs, [0, 2, 1, 3]))
    print(solve(pairs, [0, 3, 1, 2]))
