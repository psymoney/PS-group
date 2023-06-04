import sys


def answer(S, D, k) -> list:
    n = len(S)

    PD = []

    for i in range(n):
        PD.append([D[i], i])

    PD.sort()

    ans = [S[i] for i in range(n)]

    for i in range(k):
        temp = []
        for d in PD:
            temp.append(ans[d[1]])
        for j in range(n):
            ans[j] = temp[j]

    return ans


def solve() -> None:
    input = sys.stdin.readline

    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    D = list(map(int, input().split()))

    print(*answer(S, D, k))
