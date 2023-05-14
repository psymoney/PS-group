n,k=map(int,input().split())
ls=[*map(int,input().split())]
maxx=0
last=0
for i in range(n-k+1):
    if i ==0:
        maxx=sum(ls[i:i+k])
        last=maxx+0
    else:
        last=last-ls[i-1]+ls[i+k-1]
        maxx=max(maxx,last)
print(maxx)