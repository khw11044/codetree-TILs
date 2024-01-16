import sys

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


if __name__=="__main__":
    n,m=map(int, input().split())
    parents = [i for i in range(n+1)]
    cycle = set()
    
    for _ in range(m):
        a,b = map(int,input().split())
        if find(a) == find(b):
            cycle.add(parents[a])
            cycle.add(parents[b])
        # 두 정점 중 하나가 사이클에 포함되는 정점이라면 나머지 정점도 사이클로 포함한다.
        if parents[a] in cycle or parents[b] in cycle: 
            cycle.add(parents[a])
            cycle.add(parents[b])
        union(a,b)
        
    for i in range(n+1):
        find(i)
    
    parents = set(parents)
    ans = sum([1 if i not in cycle else 0 for i in parents])-1
    
    print(ans)