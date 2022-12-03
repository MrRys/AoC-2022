import sys
import re
from functools import reduce


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_rucksacks(input: str) -> list[str]:
    return list(
        map(
            lambda rucksack: [rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]],
            input.split("\n"),
        )
    )


def parse_groups(input: str) -> list[list[str]]:
    return list(map(lambda group: group.strip().split("\n"), re.findall(r".+\n.+\n.+\n?", input)))


def solve(groups: list[list[str]]) -> int:
    return sum(
        map(
            lambda i: ord(i) - ord("a") + 1 if i.islower() else ord(i) - ord("A") + 27,
            map(
                lambda group: list(reduce(lambda itemsA, itemsB: set(itemsA) & set(itemsB), group))[0],
                groups,
            ),
        )
    )


if __name__ == "__main__":
    input = load_input()
    rucksacks = parse_rucksacks(input)
    groups = parse_groups(input)
    print(solve(rucksacks))
    print(solve(groups))
