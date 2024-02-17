import sys

'''
1. 회전될 직사각형 범위 확인 
2. 한번에 업데이트해야하니깐 복사된 board 필요 
3. 회전뒤 평균값 실제 보드에 업데이트 

'''


if __name__=="__main__":
    n=int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # (r,c)를 시작으로 1번 m1만큼, 2번 m2만큼, 3번 m3만큼, 4번 m4만큼, dir==0이면 반시계, dir==1이면 시계방향 
    r, c, m1, m2, m3, m4, dir = map(int, input().split())   
    r,c = r-1,c-1
    if dir==0:
        tmp=board[r][c]
        # 4번 변부터 이동 
        for _ in range(m4):
            board[r][c] = board[r-1][c-1]
            r -= 1
            c -= 1
        # 3번 변 이동 
        for _ in range(m3):
            board[r][c] = board[r-1][c+1]
            r -= 1
            c += 1
        # 2번 변이 리스트 
        for _ in range(m2):
            board[r][c] = board[r+1][c+1]
            r += 1
            c += 1
        # 1번 변이 리스트 
        for _ in range(m2):
            board[r][c] = board[r+1][c-1]
            r += 1
            c -= 1
        board[r][c]=tmp
    else:
        tmp=board[r][c]
        # 1번 변이 리스트 
        for _ in range(m2):
            board[r][c] = board[r-1][c+1]
            r -= 1
            c += 1
        # 2번 변이 리스트 
        for _ in range(m2):
            board[r][c] = board[r-1][c-1]
            r -= 1
            c -= 1
        # 3번 변 이동 
        for _ in range(m3):
            board[r][c] = board[r+1][c-1]
            r += 1
            c -= 1
        # 4번 변부터 이동 
        for _ in range(m4):
            board[r][c] = board[r+1][c+1]
            r += 1
            c += 1
        board[r][c]=tmp
        
    for b in board:
        print(*b)