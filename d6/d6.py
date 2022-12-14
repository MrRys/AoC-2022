def load_input() -> str:
    with open(0) as src_file:
        return src_file.read().strip()


def solve(signal: str, dist: int) -> int:
    marker = list(signal[:dist])
    for idx in range(dist, len(signal)):
        if len(set(marker)) == dist:
            return idx
        marker = marker[1:]
        marker.append(signal[idx])

    return -1


if __name__ == "__main__":
    signal = load_input()
    print(solve(signal, 4))
    print(solve(signal, 14))
