outcome_score1 = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

outcome_score2 = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_matches(input: str) -> list[str]:
    return input.split("\n")


def solve(matches: list[str], outcome_score: dict) -> int:
    return sum(map(lambda match: outcome_score[match], matches))


if __name__ == "__main__":
    input = load_input()
    matches = parse_matches(input)
    print(solve(matches, outcome_score1))
    print(solve(matches, outcome_score2))
