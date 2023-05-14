import sys
from heapq import heappush, heappop


def answer(schedules) -> int:
    schedules.sort(key=lambda x: x[0])
    result = len(schedules)
    heapq = []
    heappush(heapq, schedules[0][1])

    for i in range(1, result):
        if schedules[i][0] >= heapq[0]:
            result -= 1
            heappop(heapq)
        heappush(heapq, schedules[i][1])

    return result


def solve() -> None:
    input = sys.stdin.readline

    N = int(input())
    schedules = [tuple(map(int, input().split())) for _ in range(N)]
    print(answer(schedules))


# solve()


def test() -> None:
    CASES = [
        [[(0, 40), (15, 30), (5, 10)], 2],
        [[(10, 20), (5, 10)], 1],
        [[(0, 10), (5, 20), (15, 30)], 2],
    ]

    for candidates, expected in CASES:
        result = answer(candidates)
        if result != expected:
            print(f'wrong answer.\nanswer: {expected}, result: {result}')


test()
