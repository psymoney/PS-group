import sys
from math import inf

def answer(arr: list, k: int) -> int:
    l = 0
    cnt = 0
    min_len = inf
    for r in range(len(arr)):
        if arr[r] == 1:
            cnt += 1
            if cnt == 1:
                l = r
        if cnt == k:
            min_len = min(min_len, r - l + 1)
            l += 1
            cnt -= 1
            while arr[l] != 1:
                l += 1

    return min_len if min_len != inf else -1

def sol() -> None:
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(answer(arr, K))

def test() -> None:
    cases = [
        [[1, 2, 2, 2, 1, 2, 1, 2, 2, 1], 3, 6],
        [[2, 2, 2, 2, 1, 1, 1, 2, 2, 1], 3, 3],
        [[1, 2, 2, 2, 2, 2, 2, 2, 2, 1], 2, 10],
        [[2, 2, 2, 2], 2, -1],
        [[1, 1], 2, 2]
    ]

    for i, (arr, k, expected) in enumerate(cases):
        result = answer(arr, k)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

sol()
