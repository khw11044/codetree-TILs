from collections import deque 

import sys


def bfs(x):
    isTree = True
    q = [x]
    while q:
        now = q.pop(0)
        if visited[now] == 1:  # 현재 정점을 이미 다른 요소를 통해 방문했다면(싸이클을 이룬다면)
            isTree = False  # 트리가 아님을 표시해준다.
        visited[now] = 1
        for j in graph[now]:
            if visited[j] == 0:
                q.append(j)
    return isTree


if __name__=="__main__":
    n,m=map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for _ in range(m):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    treeCnt = 0
    for i in range(1, n + 1):
        if visited[i] == 1:  # 방문한적 있다면 패스
            continue
        if bfs(i) is True:  # 현재의 연결 요소가 tree 라면 카운트
            treeCnt += 1
            
    print(treeCnt)