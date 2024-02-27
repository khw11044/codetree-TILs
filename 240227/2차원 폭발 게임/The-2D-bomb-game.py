import sys
import copy


def explosions():
    global board, answer
    did_explosion=False
    for j in range(N):
        cnt=1
        for i in range(N-1):
            if board[i][j] != 0:
                if board[i][j] == board[i+1][j]:
                    cnt+=1
                else:
                    if cnt>=M:
                        answer -= cnt
                        for l in range(cnt):
                            board[i-l][j]=0
                            did_explosion=True
                    
                        cnt=1 
        if cnt>=M:
            for l in range(cnt):
                if board[N-2+1-l][j] != 0:
                    board[N-2+1-l][j]=0
                    did_explosion=True
                    answer -= 1
    
    return did_explosion

def gravity():
    global board
    for j in range(N):
        for i in range(N-1,0,-1):
            if board[i][j]==0 and board[i-1][j]!=0: # 현재 비었으면 그 위로 0이 아닌것을 만날때까지 올라가보고 그 위에것들을 다 내린다.
                for x in range(i,N):
                    if board[x][j]==0:
                        board[x][j]=board[x-1][j]
                        board[x-1][j]=0
            

def rotation():
    global board
    new_board = copy.deepcopy(board)
    for r in range(N):
        for c in range(N):
            new_board[c][N-1-r] = board[r][c]
    
    board = new_board

def print_board(board):
    for b in board:
        print(b)
    print()

if __name__=="__main__":
    N,M,K=map(int, input().split()) # M개 이상 연속이면 터짐, K번 반복 
    board = [list(map(int, input().split())) for _ in range(N)]
    
    answer = N*N
    for _ in range(K):
        while True:
            did_explosion = explosions()
            
            gravity()
            
            did_explosion = explosions()
            
            if not did_explosion:
                break
        
        rotation()
        gravity()
    
    while True:
        did_explosion = explosions()
        if did_explosion:
            gravity()
        else:
            break
    
    print(answer)