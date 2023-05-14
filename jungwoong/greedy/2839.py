a=int(input())
temp=a
i=a//5
while i>=1:
    if (temp-(5*i))%3==0:
        print(i+(temp-(5*i))//3)
        break
    else:
        i-=1

if i==0:
    if temp%3==0:
        print(temp//3)
    else:
        print(-1)