import sys

def check1(r,c):
    ans11, ans12, ans13, ans14 = 0,0,0,0
    # 1번 블록의 1번자세 
    if 0<=r-1 and r<n and 0<=c and c+1<m:
        ans11 = board[r-1][c] + board[r][c] + board[r][c+1]
    
    # 1번 블록의 2번자세 
    if 0<=r and r+1<n and 0<=c and c+1<m:
        ans12 = board[r][c] + board[r][c+1] + board[r+1][c]
    
    # 1번 블록의 3번자세 
    if 0<=r and r+1<n and 0<=c-1 and c<m:
        ans13 = board[r][c-1] + board[r][c] + board[r+1][c]
        
    # 1번 블록의 4번자세 
    if 0<=r-1 and r<n and 0<=c-1 and c<m:
        ans14 = board[r-1][c] + board[r][c] + board[r][c-1]
        
    
    return max([ans11,ans12,ans13,ans14])

def check2(r,c):
    ans21, ans22 = 0,0
    # 2번 블록의 1번자세 
    if c+3<=m:
        ans21 = sum(board[r][c:c+3])
    
    # 2번 블록의 2번자세 
    if r+3<=n:
        ans22 = sum(list(row[c] for row in board[r:r+3]))
    
        
    
    return max([ans21,ans22])

if __name__=="__main__":
    n,m=map(int, input().split())   # n행 m열
    board = [list(map(int, input().split())) for _ in range(n)]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            answer = max(answer, check1(i,j), check2(i,j))
    
    print(answer)