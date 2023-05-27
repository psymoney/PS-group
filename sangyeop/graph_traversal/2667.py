import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
G = [list(map(int, input().split('\n')[0])) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Q = deque()
group = []

for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            traversed = 0
            Q.append((i, j))
            while Q:
                x, y = Q.popleft()
                if G[x][y] == 0:
                    continue
                traversed += 1
                G[x][y] = 0
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N and G[nx][ny] == 1:
                        Q.append((nx, ny))
            group.append(traversed)

print(len(group))
for i in sorted(group):
    print(i)
