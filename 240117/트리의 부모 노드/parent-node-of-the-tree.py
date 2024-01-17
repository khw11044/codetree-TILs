# 트리 순회를 진행합니다.
# DFS 방식으로 진행하며,
# 진행되는 간선에 대해 (부모, 자식) 관계를 정의해줍니다.
def traversal(x):   # 노드 x에 연결된 자식들을 살펴본다
    # 부모는 x, 자식이 y가 됩니다.
    for y in graph[x]:
        # 아직 방문해본적이 없는 노드라면
        # 트리의 부모-자식 관계가 결정됩니다.
        if not visited[y]:
            visited[y] = True
            parent[y] = x   # y의 부모는 x 

            # 추가적으로 탐색을 더 진행합니다.
            traversal(y)    # 다음 y의 자식들을 살펴본다

if __name__=="__main__":
    # 변수 선언 및 입력:
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)

    # n - 1개의 간선 정보를 입력받습니다.
    for _ in range(n - 1):
        a, b = tuple(map(int, input().split()))
        # 간선 정보를 인접리스트에 넣어줍니다.
        graph[b].append(a)
        graph[a].append(b)


    # 1번부터 트리 순회를 진행합니다.
    visited[1] = True
    traversal(1)

    # 부모 노드를 출력합니다.
    for i in range(2, n + 1):
        print(parent[i])