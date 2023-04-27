n,m=map(int,input().split())
ls=[*map(int,input().split())]
i,j=0,1
cnt=0
result = sum(ls[i:j])
while i<n:
    if result==m:
        cnt+=1
        i+=1
        j=i+1
        result = sum(ls[i:j])
    elif result<m and j<n:
        j+=1
        result+=ls[j-1]
    else:
        i+=1
        j=i+1
        result=sum(ls[i:j])
print(cnt)