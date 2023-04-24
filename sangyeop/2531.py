import sys
from collections import defaultdict


def answer(A: list, k: int, c: int) -> int:
    streak = defaultdict(int)

    for i in range(k):
        streak[A[i]] += 1
    streak[c] += 1
    kinds = 0
    for i in range(len(A)):
        kinds = max(kinds, len(streak))

        streak[A[i]] -= 1
        if streak[A[i]] == 0:
            del streak[A[i]]
        streak[A[(i + k) % len(A)]] += 1

    return kinds


def sol() -> None:
    input = sys.stdin.readline
    N, d, k, c = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    print(answer(A, k, c))

sol()

def test() -> None:
    cases = [
        [[7, 9, 7, 30, 2, 7, 9, 25], 4, 30, 5],
        [[2, 7, 9, 25, 7, 9, 7, 30], 4, 7, 4]
    ]

    for i, (A, k, c, expected) in enumerate(cases):
        result = answer(A, k, c)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()

