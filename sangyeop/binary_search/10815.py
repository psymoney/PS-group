import sys


def answer(cards: list, targets: list) -> list:
    def recursive(l, r, target) -> int:
        if l > r:
            return False

        mid = l + (r - l) // 2

        if cards[mid] == target:
            return True
        elif cards[mid] < target:
            return recursive(mid + 1, r, target)
        else:
            return recursive(l, mid - 1, target)

    cards.sort()
    results = []

    for target in targets:
        results.append(1 if recursive(0, len(cards) - 1, target) else 0)

    return results


def solve() -> None:
    input = sys.stdin.readline
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))
    results = answer(cards, targets)
    print(' '.join(map(str, results)))


solve()


def test() -> None:
    cases = [
        [[6, 3, 2, 10, -10], [10, 9, -5, 2, 3, 4, 5, -10], [1, 0, 0, 1, 1, 0, 0, 1]],
    ]

    for i, (A, B, expected) in enumerate(cases):
        result = answer(A, B)
        if result != expected:
            print(f'case #{i + 1} is wrong!\n{expected} is expected, but {result} is given')


test()
