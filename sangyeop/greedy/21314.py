import sys


def answer(num: str) -> tuple:
    MAX = ''
    MIN = ''
    m = 0

    for c in num:
        if c == 'K':
            if m == 0:
                MAX += '5'
                MIN += '5'
            else:
                MAX += str(10 ** m * 5)
                MIN += str(10 ** m + 5)
            m = 0
        else:
            m += 1

    if m != 0:
        MAX += '1' * m
        MIN += str(10 ** (m-1))

    return int(MAX), int(MIN)


def solve() -> None:
    input = sys.stdin.readline
    num = input().rstrip()
    for e in answer(num):
        print(e)

solve()

def test() -> None:
    CASES = [
        ['MKM', 501, 151],
        ['MKKMMK', 505500, 155105],
        ['MMMMMMMMMMMKKKKKKKKKKK', 5000000000005555555555, 1000000000055555555555]
    ]

    for case in CASES:
        num, expected_max, expected_min = case
        actual_max, actual_min = answer(num)
        if actual_max != expected_max or actual_min != expected_min:
            print(f'Wrong Answer in {num}\nExpected: {expected_max} {expected_min}\nActual: {actual_max} {actual_min}')


test()
