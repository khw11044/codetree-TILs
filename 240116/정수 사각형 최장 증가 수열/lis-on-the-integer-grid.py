from collections import deque

dxs = [0,1,-1,0]
dys = [1,0,0,-1]

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n

if __name__=="__main__":
    n=int(input())
    
    board = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            visited = [[0 for _ in range(n)] for _ in range(n)]
            visited[i][j]=1
            Q=deque()
            Q.append((i,j))
            cnt=1
            while Q:
                x,y=Q.popleft()
                for dx,dy in zip(dxs,dys):
                    nx=x+dx
                    ny=y+dy
                    
                    if in_range(nx,ny) and board[nx][ny]>board[x][y] and visited[nx][ny]==0:
                        visited[nx][ny] += visited[x][y]+1
                        Q.append((nx,ny))
                        cnt+=1
            dp[i][j]=max(max(visited))
            answer = max(answer, dp[i][j])

    print(answer)