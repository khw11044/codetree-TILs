from collections import deque 

if __name__=="__main__":
    n,m=map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for _ in range(m):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    Q=deque()
    cnt=0
    for i in range(1,n+1):
        if visited[i]==0:
            Q.append(i)
            visited[i]=1
            while Q:
                v=Q.popleft()
                for e in graph[v]:
                    Q.append(e)
                    visited[e]=1
        
        cnt+=1 
    
    print(cnt)