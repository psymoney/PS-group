import sys
import queue

input = sys.stdin.readline

dfs_values = []
bfs_values = []


class Node:
    def __init__(self, v):
        self.v = v
        self.visited = False
        self.adjacent = []

    def visit(self):
        self.visited = True


# different result compared with example
def dfs(root):
    if root is None:
        return
    root.visit()
    dfs_values.append(root.v)
    root.adjacent.sort(key=lambda x: x.v)

    for node in root.adjacent:
        if not node.visited:
            dfs(node)


# not even traverse all adjacent
def bfs(root):
    q = queue.Queue()
    root.visit()
    bfs_values.append(root.v)
    root.adjacent.sort(key=lambda x: x.v)
    for i in root.adjacent:
        bfs_values.append(i.v)
        i.visit()
        q.put(i)

    while not q.empty():
        a = q.get()

        a.adjacent.sort(key=lambda x: x.v)
        for node in a.adjacent:

            if not node.visited:
                node.visit()
                bfs_values.append(node.v)
                q.put(node)



n, m, v = list(map(int, input().split(' ')))

dnodes = [Node(i) for i in range(n + 1)]
bnodes = [Node(i) for i in range(n + 1)]
for i in range(m):
    i, j = list(map(int, input().split(' ')))
    dnodes[i].adjacent.append(dnodes[j])
    dnodes[j].adjacent.append(dnodes[i])

    bnodes[i].adjacent.append(bnodes[j])
    bnodes[j].adjacent.append(bnodes[i])


dfs(dnodes[v])
bfs(bnodes[v])

result = str(dfs_values[0])
for i in dfs_values[1:]:
    result += ' ' + str(i)
print(result)

result = str(bfs_values[0])
for i in bfs_values[1:]:
    result += ' ' + str(i)
print(result)
