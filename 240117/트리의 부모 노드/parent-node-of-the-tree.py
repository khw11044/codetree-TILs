from collections import deque

if __name__=="__main__":
    n=int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b=map(int, input().split())
        # graph[a].append(b)
        graph[b].append(a)
    
    for i in range(2,n+1):
        print(graph[i][0])