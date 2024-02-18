import sys


dxs=[-1,0,1,0]
dys=[0,1,0,-1]

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n

def boom(x,y):
    power = board[x][y]
    board[x][y] = 0
    explosion=[]
    for dx,dy in zip(dxs,dys):
        for t in range(1,power):
            nx=x+dx*t
            ny=y+dy*t
            if in_range(nx,ny):
                board[nx][ny]=0
                if [nx,ny] in explosion:
                    continue
                explosion.append([nx,ny])
        

    for i,j in explosion:
        for k in range(i,0,-1):
            board[k][j] = board[k-1][j]
            board[k-1][j] = 0
    
    print_board(board)      
    
       
def print_board(board):
    for b in board:
        print(*b)  

if __name__=="__main__":
    n=int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    r,c=map(int, input().split())
    boom(r-1,c-1)