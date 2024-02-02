import sys
sys.setrecursionlimit(100000)


# 모든 노드의 정점을 탐색하는 DFS를 진행합니다.
def DFS(x):
    global max_dist, last_node
    
    for y, w in graph[x]:   
        if not visited[y]:      # 이미 방문한 정점이면 스킵합니다.
            visited[y] = True
            dist[y] = dist[x] + w

            # 현재 정점을 기준으로 가장 먼 노드를 찾습니다.
            if dist[y] > max_dist:
                max_dist = dist[y]
                last_node = y

            DFS(y)
        

if __name__=="__main__":
    # 변수 선언 및 입력:
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    max_dist = 0
    last_node = 0

    # n - 1개의 간선 정보를 입력받습니다.
    for _ in range(n - 1):
        x, y, w = tuple(map(int, input().split()))
        graph[x].append((y, w))
        graph[y].append((x, w))


    # DFS를 통해 가장 먼 노드를 찾습니다.
    visited[1] = True
    DFS(1)

    # 가장 먼 노드에서 시작해 다시 한번 DFS를 돌려 트리의 가장 긴 거리를 찾습니다.
    for i in range(1, n + 1):
        visited[i] = False
        dist[i] = 0

    visited[last_node] = True
    DFS(last_node)

    # 트리의 가장 긴 거리를 출력합니다.
    print(max_dist)