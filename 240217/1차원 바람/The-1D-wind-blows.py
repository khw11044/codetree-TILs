import sys

from collections import deque
# BFS
# 행과 왼쪽에서 오른쪽 움직이면 1 반대면 -1 
def BFS(r,d,start):
    DQ=deque()
    DQ.append([r,d,start])
    while DQ:
        r,d,start = DQ.popleft()
        select_row = board[r]
        select_row = deque(select_row)
        select_row.rotate(d)
        board[r] = list(select_row)
        if r-1>=0 and start>=0:
            for i in range(M):
                if board[r][i] == board[r-1][i]:
                    DQ.append([r-1,-d,1])
                    break
        if r+1<N and start<=0:
            for i in range(M):
                if board[r][i] == board[r+1][i]:
                    DQ.append([r+1,-d,-1])
                    break
                
          

if __name__=="__main__":
    N,M,Q=map(int, input().split()) #  N*M 행렬, Q번 바람
    board = [list(map(int, input().split())) for _ in range(N)]
    
    for _ in range(Q):
        r,d=map(str, input().split())   # r은 행 번호, d는 L 또는 R로 왼쪽 오른쪽 
        r = int(r)-1
        if d == 'L':
            d=1
        else:
            d=-1
        BFS(r,d,0)
    
    for b in board:
        print(*b)