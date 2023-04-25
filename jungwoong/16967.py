h,w,x,y=map(int,input().split())
grid=[[*map(int,input().split())] for i in range(h+x)]
for j in range(h+x):
    for k in range(w+y):
        if j>=x and k>=y:
            grid[j][k]-=grid[j-x][k-y]
subgrid=[row[:w] for row in grid[:h]]
for l in subgrid:
    print(*l)