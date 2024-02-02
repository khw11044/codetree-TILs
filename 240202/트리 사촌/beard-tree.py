import sys

def DFS(x):
    for y in graph[x]:
        if visited[y]:
            continue
        visited[y]=True
        depth[y] = depth[x]+1
        DFS(y)

if __name__=="__main__":
    n,k=map(int, input().split())
    nodes = list(map(int, input().split()))
    root = nodes[0]
    max_size = 1_000_000
    graph = [[] for _ in range(max_size+1)]
    visited = [False]*(max_size+1)
    cnt=0
    
    for i in range(1, len(nodes)-1):
        if nodes[i]+1 == nodes[i+1]:
            graph[nodes[cnt]].append(nodes[i])

        else:
            graph[nodes[cnt]].append(nodes[i])
            cnt += 1
    
    depth = [0]*(max_size+1)
    visited[root]=True
    DFS(root)
    ans=0
    for i in range(1, len(nodes)):
        if i == k:
            continue
        if depth[nodes[i]] == depth[k]:
           ans += 1 
    
    print(ans)