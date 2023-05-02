import sys


def answer(T: list, M: int) -> int:
    l, r = 1, 1000000000

    while l <= r:
        m = l + (r - l) // 2

        woods = 0
        for t in T:
            if t > m:
                woods += t - m

        if woods < M:
            r = m - 1
        else:
            l = m + 1
            
    return r

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = list(map(int, input().split()))
    print(answer(T, M))

solve()
