import sys


def answer(w, blocks):
    amount = 0

    for i in range(1, w - 1):
        l = max(blocks[:i])
        r = max(blocks[i + 1:])
        m = min(l, r)

        if m > blocks[i]:
            amount += m - blocks[i]

    return amount


def solve():
    input = sys.stdin.readline

    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))

    print(answer(W, blocks))


solve()
