import sys

def DFS(x):
    global ans 
    
    if is_deleted[x]:
        return
    
    is_leaf=True

    for y in graph[x]:
        if is_deleted[y]:
            continue
        DFS(y)
        is_leaf=False
            
    if is_leaf:
        ans += 1


if __name__=="__main__":
    n=int(input())
    par = list(map(int,input().split()))
    
    graph = [[] for _ in range(n+1)]
    is_deleted = [False]*n
    root = -1
    for x,y in enumerate(par):
        if y==-1:
            root=x
            continue
        
        graph[y].append(x)
    
    target = int(input())
    
    is_deleted[target]=True 
    
    ans=0
    DFS(root)
    print(ans)