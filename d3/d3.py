import re
from functools import reduce


def load_input() -> str:
    with open(0) as src_file:
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
            lambda item: ord(item) - ord("a") + 1 if item.islower() else ord(item) - ord("A") + 27,
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
