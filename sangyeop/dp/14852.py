def answer(n) -> int:
    m = 10 ** 9 + 7
    dp = [0] * (10 ** 6 + 1)
    dp[0] = 0
    dp[1] = 2
    dp[2] = 7
    dp[3] = 22

    if n < 4:
        return dp[n]
    for i in range(4, n + 1):
        dp[i] = (3 * dp[i - 1] + dp[i - 2] - dp[i - 3]) % m

    return dp[n]


def solve() -> None:
    n = int(input())
    print(answer(n))


solve()
