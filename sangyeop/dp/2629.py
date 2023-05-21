import sys

def solve():

    input = sys.stdin.readline
    n = int(input())
    plates = list(map(int, input().split()))
    DP = [[0] * (500 * 30 + 1) for _ in range(n + 1)]

    def dfs(num, weight):
        if num > n:
            return
        if DP[num][weight]:
            return

        DP[num][weight] = 1

        dfs(num + 1, weight)
        dfs(num + 1, weight + plates[num - 1])
        dfs(num + 1, abs(weight - plates[num - 1]))


    dfs(0, 0)

    k = int(input())

    balls = list(map(int, input().split()))
    answers = []

    for ball in balls:
        if ball > 15000 or DP[-1][ball] == 0:
            answers.append('N')
        else:
            answers.append('Y')

    print(*answers)

solve()
