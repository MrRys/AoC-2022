import sys


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_elfs(input: str) -> list[list[int]]:
    return list(map(lambda elf: list(map(lambda cal: int(cal), elf.split("\n"))), input.split("\n\n")))


def solve(elfs: list[list[int]], n: int) -> int:
    return sum(sorted(map(lambda elf: sum(elf), elfs))[-n:])


if __name__ == "__main__":
    input = load_input()
    elfs = parse_elfs(input)
    print(solve(elfs, 1))
    print(solve(elfs, 3))
