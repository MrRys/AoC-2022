import sys
from copy import deepcopy
from functools import reduce


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def parse_monkeys(input: str) -> list[list]:
    monkeys = []
    for monkey in input.split("\n\n"):
        notes = monkey.split("\n")
        items = list(map(lambda item: int(item), notes[1].split(":")[1].strip().split(", ")))
        operation = notes[2].split("=")[1].strip().split("old")[1].strip()
        test = [int(notes[3].split()[-1]), int(notes[4].split()[-1]), int(notes[5].split()[-1])]
        monkeys.append([items, operation, test])
    return monkeys


def calculate_worry_level(item: int, operation: str, relief: int) -> int:
    operation = operation.split()
    operator = operation[0]
    operand = item if len(operation) == 1 else int(operation[1])

    match operator:
        case "+":
            return (item + operand) // relief
        case "*":
            return (item * operand) // relief

    return 0


def solve(monkeys: list[list], rounds: int, relief: int) -> int:
    inspections = [0 for _ in monkeys]
    mod = reduce(lambda acc, mod: acc * mod, [1] + list(map(lambda monkey: monkey[2][0], monkeys)))

    for _ in range(rounds):
        for monkey_idx, monkey in enumerate(monkeys):
            items = monkey[0]
            operation = monkey[1]
            test = monkey[2]
            for item in items:
                inspections[monkey_idx] += 1
                item = item % mod if relief == 1 else item
                item = calculate_worry_level(item, operation, relief)
                throw_to = test[2] if item % test[0] else test[1]
                monkeys[throw_to][0].append(item)
                monkey[0] = monkey[0][1:]

    inspections = sorted(inspections)
    return inspections[-1] * inspections[-2]


if __name__ == "__main__":
    input = load_input()
    monkeys = parse_monkeys(input)
    print(solve(deepcopy(monkeys), 20, 3))
    print(solve(deepcopy(monkeys), 10000, 1))
