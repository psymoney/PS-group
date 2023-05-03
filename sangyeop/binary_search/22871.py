import sys


def answer(L: list) -> int:
    dp = [0] + [int(1e9)] * (len(L) - 1)
    L = L

    for i in range(0, len(L)-1):
        for j in range(i+1, len(L)):
            dp[j] = min(dp[j], max((1 + abs(L[j] - L[i])) * (j - i), dp[i]))

    return dp[-1]


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    L = list(map(int, input().split()))
    print(answer(L))

solve()

def test() -> None:
    CASES = [
        [[1, 4, 1, 3, 1], 2],
        [[1, 5, 2, 1, 6], 6]
    ]

    for i, (L, expected) in enumerate(CASES):
        result = answer(L)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')

test()
