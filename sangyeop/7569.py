import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
Q = deque()
G = []
D = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]

for h in range(H):
    temp = []
    for n in range(N):
        temp.append(list(map(int, input().split())))
        for m in range(M):
            if temp[n][m] == 1:
                Q.append((h, n, m))
    G.append(temp)

while Q:
    h, n, m = Q.popleft()
    for dh, dn, dm in D:
        nh = h + dh
        nn = n + dn
        nm = m + dm
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and G[nh][nn][nm] == 0:
            Q.append((nh, nn, nm))
            G[nh][nn][nm] = G[h][n][m] + 1

day = 0
for h in G:
    for n in h:
        for m in n:
            if m == 0:
                print(-1)
                exit(0)
        day = max(day, max(n))

print(day - 1)
