n,m=map(int,input().split())
i,j=0,0
ls=[*map(int,input().split()),10**10]
ls2=[*map(int,input().split()),10**10]
while i<=n and j <=m:
    if ls[i]<=ls2[j]:
        if ls[i]!=10**10:
            print(ls[i],end=' ')
        i+=1
    else:
        if ls2[j]!=10**10:
            print(ls2[j],end=' ')
        j+=1