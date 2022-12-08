import sys


def load_input(src: str = None) -> str:
    with open(src, "r") if src is not None else sys.stdin as src_file:
        return src_file.read().strip()


def solve(signal: str, dist: int) -> int:
    marker = list(signal[:dist])
    for idx in range(dist, len(signal)):
        if len(set(marker)) == dist:
            return idx
        marker.remove(signal[idx - dist])
        marker.append(signal[idx])


if __name__ == "__main__":
    signal = load_input()
    print(solve(signal, 4))
    print(solve(signal, 14))
