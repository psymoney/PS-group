a=[0]*20000001
n=int(input())
for i in map(int,input().split()):
    a[10000000+i]+=1
m=int(input())
for j in map(int,input().split()):
    print(a[10000000+j],end=' ')