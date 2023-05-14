import copy
def cal(graph):
    maxResult=1
    for i in range(n):
        temp=1
        for j in range(n-1):
            if graph[i][j]==graph[i][j+1]:
                temp+=1
                maxResult=max(maxResult,temp)
            else:
                maxResult=max(maxResult,temp)
                temp=1
    for i in range(n):
        temp=1
        for j in range(n-1):
            if graph[j][i]==graph[j+1][i]:
                temp+=1
                maxResult=max(maxResult,temp)
            else:
                maxResult=max(maxResult,temp)
                temp=1
    return maxResult
n=int(input())
graph=[]
ans=0
for i in range(n):
    temp=[]
    for j in input():
        temp.append(j)
    graph.append(temp)
for k in range(n):
    for l in range(n-1):
        tempGraph=copy.deepcopy(graph)
        tempGraph[k][l],tempGraph[k][l+1]=tempGraph[k][l+1],tempGraph[k][l]
        ans=max(ans,cal(tempGraph))
for k in range(n):
    for l in range(n-1):
        tempGraph=copy.deepcopy(graph)
        tempGraph[l][k],tempGraph[l+1][k]=tempGraph[l+1][k],tempGraph[l][k]
        ans=max(ans,cal(tempGraph))
print(ans)