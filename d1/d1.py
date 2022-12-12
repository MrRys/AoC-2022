def load_input() -> str:
    with open(0) as src_file:
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
