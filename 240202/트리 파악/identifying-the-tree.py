import sys

sys.setrecursionlimit(100_000)

# DFS를 통해 리프노드와 리프노드의 깊이를 탐색합니다.
def DFS(x):
    global S
    
    is_leaf=True
    for y in graph[x]:
        if visited[y]:          # 이미 방문한 노드는 스킵합니다.
            continue
        is_leaf=False           # 하나라도 자식 노드가 있다면 리프 노드가 아닙니다.
        visited[y]=True         # 방문 체크
        depth[y] = depth[x]+1   # root로부터의 거리를 갱신합니다.
        DFS(y)
        
    if is_leaf:                 # 리프노드라면, 해당 노드의 깊이를 더합니다.
        S += depth[x]

if __name__=="__main__":
    n = int(input())
    graph=[[] for _ in range(n+1)]
    visited = [False]*(n+1)
    depth = [0]*(n+1)                   # 루트노드와 리프노드간의 깊이(거리)를 저장
    for _ in range(n-1):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    
    S=0                                 # 리프노드 깊이의 총합
    root = 1
    visited[root]=True 
    DFS(root)                           # DFS를 통해 리프노드와 리프노드의 깊이를 탐색합니다.
    
    # 모든 리프노드의 깊이의 합이 짝수인지 홀수인지 판단해 정답을 출력합니다.
    if S%2==1:
        print(1)
    else:
        print(0)