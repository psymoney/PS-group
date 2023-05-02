import sys


def answer(wires: list, N: int) -> int:
    l, r = 1, max(wires)

    while l <= r:
        m = l + (r - l) // 2
        numbers = 0
        for wire in wires:
            numbers += wire // m

        if numbers < N:
            r = m -1
        else:
            l = m + 1

    return r


def solve() -> None:
    input = sys.stdin.readline
    K, N = map(int, input().split())
    wires = [int(input()) for _ in range(K)]
    print(answer(wires, N))

solve()

def test() -> None:
    CASES = [
        [[802, 743, 457, 539], 11, 200],
    ]

    for i, (wires, N, expected) in enumerate(CASES):
        result = answer(wires, N)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()
