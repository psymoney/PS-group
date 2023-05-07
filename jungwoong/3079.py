n,m=map(int,input().split())
ls=[int(input()) for _ in range(n)]
lt=0
rt=min(ls)*m
result=0
while lt<=rt:
    cnt=0
    mid=(lt+rt)//2
    for i in ls:
        cnt+=mid//i
    if cnt>=m:
        rt=mid-1
        result=mid
    else:
        lt=mid+1
print(result)