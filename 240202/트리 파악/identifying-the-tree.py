import sys

from collections import deque

if __name__=="__main__":
    n=int(input())
    graph=[[] for _ in range(n+1)]
    root = 1
    arr = [0]*(n+1)
    mal = [0]*(n+1)
    mal2 = deque()
    for _ in range(n-1):
        x,y = map(int, input().split())
        graph[y].append(x)
        arr[x] += 1

    # 1. 리프노드에 말 하나씩 놓기 
    for node in range(2,n+1):
        if arr[node]==0:
            mal[node]=1
            mal2.append(node)
    
    
    turn = 0
    while mal2:
        y=mal2.popleft()
        turn += 1
        for x in graph[y]:
            if x == root:
                pass
            else:
                mal2.append(x)
    
    
    if turn%2==0:
        print(0)
    else:
        print(1)