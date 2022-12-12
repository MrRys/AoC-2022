def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_instructions(input: str) -> list[list[str]]:
    return list(map(lambda instruction: instruction.split(), input.split("\n")))


def print_screen(screen: list[list[str]]) -> None:
    for y in range(len(screen)):
        for x in range(len(screen[0])):
            print(screen[y][x], end="")
        print()


def solve(instructions: list[list[str]]) -> int:
    cycle = 1
    regX = 1
    signal_strength = 0
    instruction = None
    in_progress = False

    screen = [["." for _ in range(40)] for _ in range(6)]
    screen[0][0] = "#"

    while len(instructions) or in_progress:

        if instruction is None:
            instruction = instructions[0]
            instructions = instructions[1:]

        match instruction[0]:
            case "noop":
                instruction = None
            case "addx":
                if in_progress:
                    regX += int(instruction[1])
                    instruction = None
                    in_progress = False
                else:
                    in_progress = True

        if cycle % 40 >= regX - 1 and cycle % 40 <= regX + 1:
            screen[cycle // 40][cycle % 40] = "#"

        cycle += 1

        if (cycle + 20) % 40 == 0:
            signal_strength += cycle * regX

    print_screen(screen)

    return signal_strength


if __name__ == "__main__":
    input = load_input()
    instructions = parse_instructions(input)
    print(solve(instructions))
