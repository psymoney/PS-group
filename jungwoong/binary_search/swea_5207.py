def binarySearch(a,key):
    global ans
    result=0
    start = 0
    end=len(a)-1
    while start<=end:
        middle = (start + end)//2
        if key == a[middle]:
            ans+=1
            return
        elif key <a[middle]:
            if result==-1:
                return
            else:
                result=-1
                end=middle-1
        else:
            if result==1:
                return
            else:
                result=1
                start=middle+1
    return

for t in range(1,int(input())+1):
    n, m = map(int, input().split())
    ans = 0
    lsA = sorted([*map(int, input().split())])
    lsB = [*map(int, input().split())]
    for i in lsB:
        binarySearch(lsA, i)
    print('#%d %d'%(t,ans))
