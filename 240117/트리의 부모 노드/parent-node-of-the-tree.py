from collections import deque

if __name__=="__main__":
    n=int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b=map(int, input().split())
        graph[a].append(b)
        # graph[b].append(a)
    
    Q = deque()
    Q.append(1)

    while Q:
        x = Q.popleft()
        for e in graph[x]:
            print(x)
            Q.append(e)