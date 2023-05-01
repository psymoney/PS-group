import sys

def answer(L, S):
    l, r = 0, 0
    sum = 0
    length = int(1e9)

    while True:
        if sum >= S:
            length = min(length, r - l)
            sum -= L[l]
            l += 1
        elif r == len(L):
            break
        else:
            sum += L[r]
            r += 1

    if length != int(1e9):
        return length
    return 0


def sol() -> None:
    input = sys.stdin.readline
    N, S = map(int, input().split())
    L = list(map(int, input().split()))
    print(answer(L, S))

sol()

def test() -> None:
    cases = [
        [[5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15, 2],
    ]

    for i, (L, S, expected) in enumerate(cases):
        result = answer(L, S)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()
