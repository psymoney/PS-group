n = int(input())
t = 0

for i in range(1, n + 1):
    if n - t > i:
        t += i
    elif n - t == i:
        print(i)
        break
    elif n - t < i:
        print(i - 1)
        break
