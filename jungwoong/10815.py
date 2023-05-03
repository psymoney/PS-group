from bisect import bisect_left

a=int(input())
first=sorted(list(map(int,input().split())))
b=int(input())
second=map(int,input().split())

ans = []
for i in second:
    idx = bisect_left(first,i)
    if idx < len(first) and first[idx]==i:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)