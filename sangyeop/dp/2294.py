import sys
import math
inf = math.inf
input = sys.stdin.readline

[n, k] = list(map(int, input().split()))
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
dp = [inf] * (k + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])
