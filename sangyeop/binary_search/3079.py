import sys


def answer(T: list, M: int) -> int:
    l, r = 0, 10 ** 18
    result = 0
    while l <= r:
        m = l + (r - l) // 2

        cnt = 0
        for t in T:
            cnt += m // t

        if cnt < M:
            l = m + 1
        else:
            result = m
            r = m - 1

    return result


def solve() -> None:
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = [int(input()) for _ in range(N)]
    print(answer(T, M))


solve()


def test() -> None:
    CASES = [
        [[7, 10], 6, 28],
        [[3, 8, 3, 6, 9, 2, 4], 10, 8],
        [[1000000000], 1, 1000000000]
    ]

    for i, (T, M, expected) in enumerate(CASES):
        result = answer(T, M)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')


test()
