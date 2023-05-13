import sys

def answer(h, a):
    n = len(h)
    sa = sorted(a)

    for i in range(n-1, -1, -1):
        e = sa[i]
        h[a.index(e)] += e * i

    return sum(h)



def solve():
    input = sys.stdin.readline
    n = int(input())
    h = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(answer(h, a))

solve()

def test():
    CASES = [
        [[1, 3, 2, 4, 6], [2, 7, 3, 4, 1], 64]
    ]

    for h, a, expected in CASES:
        result = answer(h, a)
        if result != expected:
            print(f'wrong answer.\nanswer: {expected}, result: {result}')


test()
