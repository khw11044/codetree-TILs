def DFS(x):
    global answer
    visited[x]=1
    for y,weight in enumerate(graph[x]):
        if weight!=0:
            if visited[y]==0:
                visited[y]=1
                answer = max(answer, answer + weight)
                DFS(y)

if __name__=="__main__":
    n=int(input())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c=map(int, input().split())
        graph[a][b]=c
    
    visited = [0]*(n+1)
    answer = 0
    DFS(1)
    print(answer)