import sys


if __name__=="__main__":

    # 변수 선언 및 입력:
    n, k = tuple(map(int, input().split()))
    par = [0] * (n + 1)
    
    ans = 0

    target_node_index = 0
    nodes = [0] + list(map(int, input().split()))
    for index in range(1, n + 1):
        if nodes[index] == k: 
            target_node_index = index

    # n개의 원소를 바탕으로 트리를 만들어줍니다.
    parent_node = 0
    for index in range(2, n + 1):
        if nodes[index] > nodes[index-1] + 1:
            parent_node += 1
        
        par[index] = parent_node

    for cur_node in range(1, n + 1):
        # cur_node의 부모의 부모 노드가 존재하지 않는 경우에는 패스
        if not par[par[cur_node]] or not par[par[target_node_index]]:
            continue
        
        # 부모 노드는 다르면서 and 부모의 부모 노드가 같은 경우를 찾습니다.
        if par[cur_node] != par[target_node_index] and par[par[cur_node]] == par[par[target_node_index]]:
            ans += 1        # 해당 노드들은 사촌이 됩니다.

    # 사촌 노드의 개수를 출력합니다.
    print(ans)