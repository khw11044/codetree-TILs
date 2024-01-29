import sys 


def DFS(start,a):
    for b,w in graph[a]:
        if visited[b]:  # 이미 방문한 노드는 스킵 
            continue
        
        visited[b] = True   # a노드에 연결된 b 노드들 모두 방문 
        dist[start][b] = dist[start][a] + w     # "시작노드부터 b 노드까지 거리" == "시작노드부터 a노드까지 간거리 + w" 
        DFS(start, b)

if __name__=="__main__":
    n,m=map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    dist = [[0]*(n+1) for _ in range(n+1)]
    
    for _ in range(n-1):
        a,b,w=map(int, input().split())
        graph[a].append((b,w))
        graph[b].append((a,w))
        
    
    for i in range(1,n+1):
        for j in range(1, n+1):
            visited[j] = False
            
        visited[i] = True 
        DFS(i,i)    # dist를 통해 모든 i부터 i까지의 거리를 업데이트 

    for _ in range(m):
        a,b = map(int, input().split()) # a에서 b까지 가는데 간선의 거리 
        print(dist[a][b])