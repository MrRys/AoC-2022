from copy import deepcopy


def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def parse_moves(input: str) -> list[list]:
    return list(
        reversed(
            list(map(lambda move: [move.split()[0], int(move.split()[1]), 0, True], input.split("\n")))
        )
    )


def execute_step(knot: list[int], move: list) -> None:
    match move[0]:
        case "L":
            knot[0] -= 1
            move[1] -= 1
        case "R":
            knot[0] += 1
            move[1] -= 1
        case "D":
            knot[1] -= 1
            move[1] -= 1
        case "U":
            knot[1] += 1
            move[1] -= 1


def adjacent(knot1: list[int], knot2: list[int]) -> bool:
    return abs(knot1[0] - knot2[0]) <= 1 and abs(knot1[1] - knot2[1]) <= 1


def to_string(knot: list[int]) -> str:
    return str(knot[0]) + "," + str(knot[1])


def generate_moves(knots: list[list[int]], idx: int) -> list[list]:
    diff = [knots[idx][0] - knots[idx + 1][0], knots[idx][1] - knots[idx + 1][1]]

    match diff:
        case [0, 2]:
            return [["U", 1, idx + 1, True]]
        case [2, 0]:
            return [["R", 1, idx + 1, True]]
        case [0, -2]:
            return [["D", 1, idx + 1, True]]
        case [-2, 0]:
            return [["L", 1, idx + 1, True]]
        case [2, 1]:
            return [["R", 1, idx + 1, True], ["U", 1, idx + 1, False]]
        case [1, 2]:
            return [["R", 1, idx + 1, True], ["U", 1, idx + 1, False]]
        case [2, -1]:
            return [["R", 1, idx + 1, True], ["D", 1, idx + 1, False]]
        case [1, -2]:
            return [["R", 1, idx + 1, True], ["D", 1, idx + 1, False]]
        case [-2, 1]:
            return [["L", 1, idx + 1, True], ["U", 1, idx + 1, False]]
        case [-1, 2]:
            return [["L", 1, idx + 1, True], ["U", 1, idx + 1, False]]
        case [-2, -1]:
            return [["L", 1, idx + 1, True], ["D", 1, idx + 1, False]]
        case [-1, -2]:
            return [["L", 1, idx + 1, True], ["D", 1, idx + 1, False]]
        case [2, 2]:
            return [["R", 1, idx + 1, True], ["U", 1, idx + 1, False]]
        case [-2, 2]:
            return [["L", 1, idx + 1, True], ["U", 1, idx + 1, False]]
        case [2, -2]:
            return [["R", 1, idx + 1, True], ["D", 1, idx + 1, False]]
        case [-2, -2]:
            return [["L", 1, idx + 1, True], ["D", 1, idx + 1, False]]


def simulate(moves: list[list[int]], knots_n: int) -> int:
    knots = [[0, 0] for _ in range(knots_n + 1)]
    visited = {"0,0"}

    while len(moves) != 0:
        move = moves.pop()
        knot_idx = move[2]
        valid_move = move[3]

        execute_step(knots[knot_idx], move)

        if move[1] > 0:
            moves.append(move)

        if valid_move and knot_idx < knots_n and not adjacent(knots[knot_idx], knots[knot_idx + 1]):
            moves += generate_moves(knots, knot_idx)

        if valid_move and knot_idx == knots_n:
            visited.add(to_string(knots[knot_idx]))

    return len(visited)


if __name__ == "__main__":
    input = load_input()
    moves = parse_moves(input)
    print(simulate(deepcopy(moves), 1))
    print(simulate(deepcopy(moves), 9))
