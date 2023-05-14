import sys


def answer(candidates) -> int:
    candidates.sort(key=lambda x: x[0])
    result = len(candidates)
    top = candidates[0][1]

    for i in range(1, result):
        if candidates[i][1] > top:
            result -= 1
        top = min(top, candidates[i][1])

    return result


def solve() -> None:
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        candidates = [tuple(map(int, input().split())) for _ in range(N)]
        print(answer(candidates))


# solve()


def test() -> None:
    CASES = [
        [[(3, 2), (1, 4), (4, 1), (2, 3), (5, 5)], 4],
        [[(3, 6), (7, 3), (4, 2), (1, 4), (5, 7), (2, 5), (6, 1)], 3],
        [[(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3), (9, 2), (10, 1)], 10],
    ]

    for candidates, expected in CASES:
        result = answer(candidates)
        if result != expected:
            print(f'wrong answer.\nanswer: {expected}, result: {result}')


test()
