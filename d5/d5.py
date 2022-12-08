import sys
import re
import copy


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_input(input: str):
    return input.split("\n\n")


def parse_stacks(stacks_str: str) -> dict[list[str]]:
    stacks = {}

    for line in stacks_str.split("\n"):
        for stack, crate in enumerate(range(1, len(line), 4)):
            if not stacks.get(stack + 1, None):
                stacks[stack + 1] = []
            if line[crate].isalpha():
                stacks[stack + 1] = [line[crate]] + stacks[stack + 1]

    return stacks


def parse_commands(commands_str: str) -> list[int]:
    return list(
        map(
            lambda command: list(map(lambda instr: int(instr), re.sub(r"[^0-9| ]", "", command).split())),
            commands_str.strip().split("\n"),
        )
    )


def solve(stacks: dict[list[str]], commands: list[int], reverse: bool = True) -> str:
    for command in commands:
        if reverse:
            stacks[command[2]] += reversed(stacks[command[1]][-command[0] :])
        else:
            stacks[command[2]] += stacks[command[1]][-command[0] :]
        stacks[command[1]] = stacks[command[1]][: len(stacks[command[1]]) - command[0]]

    result = ""
    for stack in range(1, len(stacks) + 1):
        result += stacks[stack][-1]

    return result


if __name__ == "__main__":
    input = load_input()
    stacks_str, commands_str = parse_input(input)
    stacks = parse_stacks(stacks_str)
    commands = parse_commands(commands_str)
    print(solve(copy.deepcopy(stacks), commands, True))
    print(solve(copy.deepcopy(stacks), commands, False))
