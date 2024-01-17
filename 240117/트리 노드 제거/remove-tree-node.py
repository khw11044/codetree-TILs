# DFS를 통해 x 아래의 리프노드의 개수를 찾아줍니다.
def DFS(x):
    global ans
    
    if is_deleted[x]:   # (루트 노드가 삭제되었을 때) 삭제된 노드는 스킵합니다.
        return

    # x번 노드가 리프노드인지 판단합니다. 자신의 자식 노드가
    # 하나라도 남아 있을 경우 x번 노드는 리프노드가 아닙니다.
    is_leaf = True
    if graph[x]:
        for y in graph[x]:
            # 삭제된 노드는 스킵합니다.
            if is_deleted[y]: 
                continue
            DFS(y)

            is_leaf = False

    # 자신 노드가 리프 노드일 경우 답을 갱신합니다.
    if is_leaf: 
        ans += 1

if __name__=="__main__":
    n = int(input())
    par = list(map(int, input().split()))   # n개의 간선 정보를 입력받습니다.
    target = int(input())   # 제거할 노드 

    root = -1
    graph = [[] for _ in range(n)]
    is_deleted = [False] * (n)

    for x,y in enumerate(par):
        if y == -1:         # -1이 입력된 경우 루트 노드로 지정합니다.
            root = x        # root는 0번째 노드 
            continue
        graph[y].append(x)  # 간선 정보를 인접리스트에 넣어줍니다.

    # 노드를 제거하는 방법에는 간선을 직접 끊어주는 등 여러 방법이 있습니다.
    # 여기서는 삭제되었는지 여부를 배열로 관리합니다.
    is_deleted[target] = True   # 일단 제거할 노드부터 삭제 

    ans = 0
    DFS(root)   # root 정점으로부터 리프노드의 개수를 찾습니다.
    print(ans)