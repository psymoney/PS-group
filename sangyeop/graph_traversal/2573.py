import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
D = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def dfs(m, n, V, G, NG):
    Q = deque()
    Q.append((m, n))

    while Q:
        x, y = Q.popleft()
        shores = 0
        for dx, dy in D:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if G[ny][nx] == 0:
                    shores += 1
                elif G[ny][nx] > 0 and not V[ny][nx]:
                    Q.append((nx, ny))
                    V[ny][nx] = True
        NG[y][x] = max(0, G[y][x] - shores)
    return 1

year = 0
while True:
    V = [[False for _ in range(M)] for _ in range(N)]
    NG = [[0] * M for _ in range(N)]
    num_glacial = 0
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if G[y][x] == 0:
                continue
            if V[y][x]:
                continue
            num_glacial += dfs(x, y, V, G, NG)
    if num_glacial > 1:
        break
    if num_glacial == 0:
        year = 0
        break
    G = NG
    year += 1

print(year)
