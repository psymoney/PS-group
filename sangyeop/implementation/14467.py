def solve():
    n = int(input())

    arr = {}
    ans = 0

    for i in range(n):
        a, b = map(int, input().split())
        if a not in arr:
            arr[a] = b
        else:
            if arr[a] != b:
                arr[a] = b
                ans += 1

    print(ans)

solve()
