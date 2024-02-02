'''
이 문제는 시뮬레이션 처럼 푸는 것이 아니라 
모든 리프노드와 루트노드까지의 거리를 모두 구해 그 합이 홀수 인지 짝수 인지 알아보는 문제이다.

루트노드와 모든 리프노드의 말까지 거리의 합이 S라고 하자 
a가 한턴 진행하면 말 하나가 위로 올라가고 S는 -1만큼 줄어든다.
b가 한턴 진행하면 어떤 말을 하나 선택하든 역시 말 하나가 위로 올라가고 S는 -1만큼 줄어든다. 
이러한 과정을 반복하다가 S가 최초로 0이 되는 턴에 말을 움직여야 하는 사람이 진다. 

-> 따라서 루트노드에서 모든 리프노드까지의 거리를 구해야한다.

'''


import sys
sys.setrecursionlimit(100000)


# DFS를 통해 리프노드와 리프노드의 깊이를 탐색합니다.
def DFS(x):
    global ans
    
    is_leaf = True

    for y in graph[x]:
        if visited[y]:      # 이미 방문한 노드는 스킵합니다.
            continue

        visited[y] = True
        is_leaf = False     # 하나라도 자식 노드가 있다면 리프 노드가 아닙니다.
        
        # root로부터의 거리를 갱신합니다.
        depth[y] = depth[x] + 1

        DFS(y)

    # 리프노드라면, 해당 노드의 깊이를 더합니다.
    if is_leaf: 
        ans += depth[x]



if __name__=="__main__":

    # 변수 선언 및 입력:
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    # n - 1개의 간선 정보를 입력받습니다.
    for _ in range(n - 1):
        x, y = tuple(map(int, input().split()))
        graph[x].append(y)
        graph[y].append(x)

    root=1
    visited = [False]*(n + 1)
    depth = [0]*(n + 1)       # 루트노드와 리프노드간의 깊이(거리)를 저장

    # 리프노드 깊이의 총합
    ans = 0
    
    # DFS를 통해 리프노드와 리프노드의 깊이를 탐색합니다.
    visited[root] = True
    DFS(root)

    # 모든 리프노드의 깊이의 합이 짝수인지 홀수인지 판단해 정답을 출력합니다.
    if ans % 2 == 1: 
        print(1)
    else:
        print(0)