import sys
from itertools import permutations

def sol():
    input = sys.stdin.readline
    N = int(input())
    cases = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

    for _ in range(N):
        guess, strike, ball = map(int, input().split())
        guess = [int(x) for x in str(guess)]
        removal_count = 0

        for i in range(len(cases)):
            strike_count, ball_count = 0, 0
            case = cases[i - removal_count]

            for j in range(3):
                if guess[j] == case[j]:
                    strike_count += 1
                elif guess[j] in case:
                    ball_count += 1

            if strike_count != strike or ball_count != ball:
                cases.pop(i - removal_count)
                removal_count += 1

    print(len(cases))

sol()
