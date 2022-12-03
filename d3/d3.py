import sys
import re


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_rucksacks(input: str) -> list[str]:
    return input.split("\n")


def parse_groups(input: str) -> list[list[str]]:
    return list(map(lambda group: group.strip().split("\n"), re.findall(r".+\n.+\n.+\n?", input)))


def part1(rucksacks: list[str]) -> int:
    return sum(
        map(
            lambda i: ord(i) - ord("a") + 1 if i >= "a" else ord(i) - ord("A") + 27,
            map(
                lambda rucksack: list(
                    filter(
                        lambda item: item in rucksack[: len(rucksack) // 2],
                        rucksack[len(rucksack) // 2 :],
                    )
                )[0],
                rucksacks,
            ),
        )
    )


def part2(groups: list[list[str]]) -> int:
    return sum(
        map(
            lambda i: ord(i) - ord("a") + 1 if i >= "a" else ord(i) - ord("A") + 27,
            map(
                lambda group: list(
                    filter(
                        lambda item: item in group[1] and item in group[2],
                        group[0],
                    )
                )[0],
                groups,
            ),
        )
    )


if __name__ == "__main__":
    input = load_input()
    rucksacks = parse_rucksacks(input)
    groups = parse_groups(input)
    print(part1(rucksacks))
    print(part2(groups))
