import sys

if __name__=="__main__":
    
    # 변수 선언 및 입력:
    n, k = tuple(map(int, input().split()))
    par = [0] * (n + 1)
    finding_node_index = -1
    ans = 0

    # n개의 수열 원소를 입력받습니다.
    nodes = list(map(int, input().split()))
    for i in range(1, n):
        if nodes[i] == k: 
            finding_node_index = i

    # n개의 원소를 바탕으로 트리를 만들어줍니다.
    parent_node = 0
    for i in range(1, n):
        if nodes[i] > nodes[i-1]+1:
            parent_node += 1
        
        par[i] = parent_node

    for cur_node in range(1, n):
        # cur_node의 부모의 부모 노드가 존재하지 않는 경우에는 패스
        if not par[par[cur_node]] or not par[par[finding_node_index]]:
            continue
        
        # 부모 노드는 다르면서 and 부모의 부모 노드가 같은 경우를 찾습니다.
        if par[cur_node] != par[finding_node_index] and par[par[cur_node]] == par[par[finding_node_index]]:
            ans += 1    # 해당 노드들은 사촌이 됩니다.

    # 사촌 노드의 개수를 출력합니다.
    print(ans)