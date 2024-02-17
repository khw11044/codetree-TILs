import sys

import copy

'''
1. 회전될 직사각형 범위 확인 
2. 한번에 업데이트해야하니깐 복사된 board 필요 
3. 회전뒤 평균값 실제 보드에 업데이트 

'''

dxs=[-1,0,1,0]
dys=[0,1,0,-1] 

def in_range(nx,ny):
    return 0<=nx<N and 0<=ny<M

'''
4 5 2 5 6 6
2 2 1 6 1 0
5 5 2 1 6 5
4 2 8 8 6 5

4 5 2 5 6 6
2 3 1 6 1 0
5 5 2 1 6 5
4 2 8 8 6 5

'''

if __name__=="__main__":
    N,M,Q=map(int, input().split()) #  N*M 행렬, Q번 바람
    board = [list(map(int, input().split())) for _ in range(N)]
    
    new_board = copy.deepcopy(board)    # 한꺼번에 출력하기 위해 
    for _ in range(Q):
        r1,c1,r2,c2=map(int, input().split())
        r1,c1,r2,c2 =  r1-1,c1-1,r2-1,c2-1 
        grid = [[0]*M for _ in range(N)]

        
        # 윗변 
        for j in range(c1,c2):
            grid[r1][j+1] = board[r1][j]
            # 아래변
            grid[r2][j] = board[r2][j+1]
        # 오른변 
        for i in range(r1,r2):
            grid[i+1][c2] = board[i][c2]
            # 왼변
            grid[i][c1] = board[i+1][c1]
            
        # 회전한거 업데이트
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if r1+1<=i<=r2-1 and c1+1<=j<=c2-1:
                    continue
                board[i][j]=grid[i][j]
        
        # 주변값 평균 업데이트 
        new_board = copy.deepcopy(board)    # 한꺼번에 출력하기 위해 
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                ans=1
                for k in range(4):
                    ni=i+dxs[k]
                    nj=j+dys[k]
                    if in_range(ni,nj):
                        ans+=1
                        new_board[i][j] += board[ni][nj]
                        
                new_board[i][j] = new_board[i][j]//ans
        
        board = copy.deepcopy(new_board)    # 한꺼번에 출력하기 위해
        
    for b in new_board:
        print(*b)