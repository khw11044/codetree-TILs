import sys

from collections import deque

def BFS(x):
    isTree = True
    Q=deque()
    Q.append(x)
    
    while Q:
        now = Q.popleft()
        if visited[now]==1:     # 연결된 노드를 타고 가다 이미 방문한적 있는 노드에 도달하면 
            isTree=False        # 그건 사이클이라는 뜻 -> 트리 아님
            
        visited[now]=1
        for e in graph[now]:
            if visited[e]==0:
                Q.append(e)
    
    return isTree

if __name__=="__main__":
    n,m=map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [0]*(n+1)
    
    treeCnt=0
    for i in range(1,n+1):
        if visited[i]==1:
            continue
        
        if BFS(i) is True:
            treeCnt += 1
            
    print(treeCnt)