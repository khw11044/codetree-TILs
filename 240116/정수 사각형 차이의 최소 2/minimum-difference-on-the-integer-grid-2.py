import sys 

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n 

dxs=[0,1]
dys=[1,0]

def DFS(x,y):
    global ans
    if x==n-1 and y==n-1:
        ans = min(ans, abs(max(res)-min(res)))
        return ans
    for dx,dy in zip(dxs,dys):
        nx=x+dx
        ny=y+dy
        
        if in_range(nx,ny) and dp[nx][ny]==0:
            dp[nx][ny]=1
            res.append(board[nx][ny])
            DFS(nx,ny)
            dp[nx][ny]=0
            res.pop()

if __name__=="__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dp=[[0]*n for _ in range(n)]
    dp[0][0] = board[0][0]
    
    ans=sys.maxsize
    res=[board[0][0]]
    DFS(0,0)
    print(ans)