import sys

def get_max_income(schedules):
    n = len(schedules)
    dp = [0] * (n+2)

    for i, schedule in enumerate(schedules):
        t, p = schedule
        if i+t+1 <= n+1:
            dp[i+t+1] = max(dp[i+t+1], dp[i+1]+p)
        if i+2 <= n+1:
            dp[i+2] = max(dp[i+1], dp[i+2])

    return dp[-1]


def sol():
    input = sys.stdin.readline
    N = int(input())
    schedules = [map(int, input().split()) for _ in range(N)]
    print(get_max_income(schedules))

sol()


def test():
    cases = [
        ([(3,10), (5,20), (1,10), (1,20), (2,15), (4,40), (2,200)], 45),
        ([(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10)], 55),
        ([(5,10), (5,9), (5,8), (5,7), (5,6), (5,10), (5,9), (5,8), (5,7), (5,6)], 20),
        ([(5, 50), (4,40), (3,30), (2,20), (1,10), (1,10), (2,20), (3,30), (4,40), (5,50)], 90)
    ]
    for i, case in enumerate(cases):
        schedule, answer = case
        max_income = get_max_income(schedule)
        if max_income != answer:
            print(f'case #{i+1} is wrong:'
                  f'the answer is expected to be {answer}, but given is {max_income}')
