import sys

dxs = [-1,1,0,0]
dys = [0,0,1,-1]

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n

def gravity(x,y):
    for row in range(x,0,-1):
        board[row][y] = board[row-1][y]
        board[row-1][y] = 0
    

def explosion(x,y,power):
    board[x][y]=0
    if power==1:
        return
    for d in range(4):
        for p in range(1,power):
            nx = x+dxs[d]*p
            ny = y+dys[d]*p
            if in_range(nx,ny) and board[nx][ny]!=0:
                board[nx][ny]=0
                if d == 2 or d == 3:
                    gravity(nx,ny)

def print_board(board):
    for b in board:
        print(*b)
    print()

if __name__=="__main__":
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    for _ in range(m):
        col=int(input())
        col-=1
        for i in range(n):
            if board[i][col] != 0:
                power = board[i][col]
                explosion(i,col,power)
                break
                
    print_board(board)