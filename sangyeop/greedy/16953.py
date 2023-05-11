import sys

def answer(a, b) -> int:
    cnt = 1

    while b != 0:
        if b == a:
            return cnt
        rem = b % 2
        last_num = int(str(b)[-1])

        if last_num == 1:
            b = int(b // 10)
        elif rem == 0:
            b = int(b / 2)
        else:
            return -1

        cnt += 1

    return -1


def solve() -> None:
    input = sys.stdin.readline
    a, b = map(int, input().split())
    print(answer(a, b))

solve()

def test() -> None:
    CASES = [
        [2, 162, 5],
        [4, 42, -1],
        [100, 40021, 5],
        [1, 1688, 7],
    ]

    for a, b, expected in CASES:
        result = answer(a, b)
        if result != expected:
            print(f'Wrong answer. Case: {a, b}, result: {result}, expected: {expected}')


test()
