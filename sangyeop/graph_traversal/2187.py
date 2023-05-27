from collections import deque

N, M = map(int, input().split())

G = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

Q = deque()
Q.append((0, 0))

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if G[nx][ny] == 0:
            continue
        if G[nx][ny] == 1:
            G[nx][ny] = G[x][y] + 1
            Q.append((nx, ny))

print(G[N-1][M-1])
