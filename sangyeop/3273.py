import sys

def answer(L, x) -> int:
    L.sort()
    l, r = 0, len(L) - 1
    cnt = 0
    while l < r:
        if L[l] + L[r] == x:
            cnt += 1
            l += 1
            r -= 1
        elif L[l] + L[r] < x:
            l += 1
        else:
            r -= 1
    return cnt

def sol() -> None:
    input = sys.stdin.readline
    n = int(input())
    L = list(map(int, input().split()))
    x = int(input())
    print(answer(L, x))

sol()

def test() -> None:
    cases = [
        [[5, 12, 7, 10, 9, 1, 2, 3, 11], 13, 3],
    ]

    for i, (L, x, expected) in enumerate(cases):
        result = answer(L, x)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()
