import re
from collections import defaultdict


def load_input() -> str:
    with open("d7\input.txt") as src_file:
        return src_file.read().strip()


def parse(input: str) -> int:
    dir_size = defaultdict(lambda x: 0)
    dir_path = ""
    for command in input.split("\n"):
        if command == "$ cd /":
            dir_path = "/"
            if dir_path not in dir_size.keys():
                dir_size[dir_path] = 0
        elif command == "$ cd ..":
            dir_path = re.sub(r"[^/]+/$", "", dir_path)
        elif command.startswith("$ cd"):
            dir_path += command.split()[2] + "/"
            if dir_path not in dir_size.keys():
                dir_size[dir_path] = 0
        elif re.match(r"^[0-9]", command):
            tmp_path = dir_path
            size = int(command.split()[0])
            dir_size["/"] += size
            while tmp_path != "/":
                dir_size[tmp_path] += size
                tmp_path = re.sub(r"[^/]+/$", "", tmp_path)

    return dir_size


def solve1(dir_size):
    result = 0
    for dir in dir_size.keys():
        if dir_size[dir] <= 100000:
            result += dir_size[dir]
    return result


def solve2(dir_size):
    to_free = 30000000 - (70000000 - dir_size["/"])
    min = 70000000
    for dir in dir_size.keys():
        if dir_size[dir] >= to_free and min > dir_size[dir]:
            min = dir_size[dir]
    return min


if __name__ == "__main__":
    input = load_input()
    sizes = parse(input)
    print(solve1(sizes))
    print(solve2(sizes))
