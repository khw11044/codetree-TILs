from collections import deque 

moves = [(0,1),(1,0)]

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n

if __name__=="__main__":
    n= int(input())

    board = [list(map(int,input().split())) for _ in range(n)]

    dp = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    dp[0][0] = board[0][0]
    visited[0][0] = 1
    Q=deque()
    Q.append((0,n-1))

    while Q:
        x,y = Q.popleft()
        for dx,dy in moves:
            nx=x+dx
            ny=y+dy
            if in_range(nx,ny) and visited[nx][ny]<2:
                visited[nx][ny] +=1
                dp[nx][ny] = max(dp[nx][ny], dp[x][y]+board[nx][ny])
                Q.append((nx,ny))

    print(dp[n-1][n-1])