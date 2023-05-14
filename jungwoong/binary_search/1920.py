n=int(input())
lst=set(map(int,input().split()))
m=int(input())
src=[*map(int,input().split())]
for i in src:
    if i in lst:
        print(1)
    else:
        print(0)