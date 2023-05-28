import sys
import copy
from collections import deque


class Solve:
    max_area = 0

    def __init__(self):
        input = sys.stdin.readline
        self.N, self.M = map(int, input().split())
        self.G = [list(map(int, input().split())) for _ in range(self.N)]
        self.D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.place_wall(0)
        print(self.max_area)

    def predict_area(self):
        Q = deque()
        CG = copy.deepcopy(self.G)

        for y in range(self.N):
            for x in range(self.M):
                if CG[y][x] == 2:
                    Q.append((x, y))

        while Q:
            x, y = Q.popleft()

            for dx, dy in self.D:
                nx = x + dx
                ny = y + dy

                if 0 <= ny < self.N and 0 <= nx < self.M:
                    if CG[ny][nx] == 0:
                        CG[ny][nx] = 2
                        Q.append((nx, ny))

        area = 0
        for y in range(self.N):
            for x in range(self.M):
                if CG[y][x] == 0:
                    area += 1

        self.max_area = max(self.max_area, area)

    def place_wall(self, count):
        if count == 3:
            self.predict_area()
            return
        for y in range(self.N):
            for x in range(self.M):
                if self.G[y][x] == 0:
                    self.G[y][x] = 1
                    self.place_wall(count + 1)
                    self.G[y][x] = 0


Solve()
