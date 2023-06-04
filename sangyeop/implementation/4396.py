import sys


def answer(n, board, player):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    answer = [['.' for _ in range(n)] for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if player[i][j] == "x":
                if board[i][j] == "*":
                    flag = True
                cnt = 0
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < n:
                        if board[x][y] == "*":
                            cnt += 1
                answer[i][j] = str(cnt)
    if flag:
        for a in range(n):
            for b in range(n):
                if board[a][b] == "*":
                    answer[a][b] = "*"
    for i in range(n):
        print(''.join(answer[i]))


def solve():
    input = sys.stdin.readline

    N = int(input())
    board = [input() for _ in range(N)]
    player = [input() for _ in range(N)]

    print(answer(N, board, player))


solve()
