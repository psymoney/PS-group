import sys

def answer(T: list, K: int) -> int:
    l, r = 0, 0
    sub_total = T[0]
    result = -int(1e9)

    while r < len(T) - 1:
        if r-l+1 < K:
            r += 1
            sub_total += T[r]
        if r-l+1 == K:
            result = max(result, sub_total)
            sub_total -= T[l]
            l += 1

    return result

def sol() -> None:
    input = sys.stdin.readline
    N, K = map(int, input().split())
    T = list(map(int, input().split()))
    print(answer(T, K))

sol()

def test() -> None:
    cases = [
        [[3, -2, -4, -9, 0, 3, 7, 13, 8, -3], 2, 21],
        [[3, -2, -4, -9, 0, 3, 7, 13, 8, -3], 5, 31],
    ]

    for i, (T, K, expected) in enumerate(cases):
        result = answer(T, K)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()
