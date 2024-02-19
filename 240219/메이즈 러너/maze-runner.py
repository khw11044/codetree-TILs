import sys

dxs=[-1,1,0,0]
dys=[0,0,-1,1]

def in_range(nx,ny):
    return 0<=nx<N and 0<=ny<N

def cal_distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def players_move():
    delete_list = []
    for pid in players:
        x,y=players[pid]
        min_dis = cal_distance(x,y,tr,tc)
        mr,mc=x,y
        delete=False
        for dx,dy in zip(dxs,dys):
            nx=x+dx
            ny=y+dy
            if (nx,ny) == (tr,tc):
                players_dis[pid] += 1
                delete_list.append(pid)
                delete=True
                break
            if in_range(nx,ny) and board[nx][ny]==0:
                tmp_dis = cal_distance(nx,ny,tr,tc)
                if tmp_dis<min_dis:
                    min_dis = tmp_dis
                    mr,mc=nx,ny
                elif tmp_dis==min_dis:
                    if nx < mr:         # 만약 거리가 같으면 
                        mr,mc=nx,ny     # 상으로 움직이는 것을 더 중시
        if not delete:
            players[pid] = [mr,mc]
            if (mr,mc) != (x,y):
                players_dis[pid] += 1
    
    if delete_list:
        for did in delete_list:
            del players[did]


def set_rect():
    # 1. 출구와 참가자 최소 1명을 포함한 가장 작은 크기의 정사각형 선정하기 
    # 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
    '''
    start_r,start_c와 end_r,end_c를 구해야함 
    '''
    start_r,start_c=0,0
    tmp_r,tmp_c=N,N
    # 가장 작은 정사각형은 탈출구와 사람간의 거리가 가장 작은 거리 
    min_dis = N*N
    for pid in players:      # M -= 1
        r,c = players[pid]
        tmp_dis = cal_distance(r,c,tr,tc)
        if tmp_dis<=min_dis:
            min_dis = tmp_dis
            if r<tmp_r:
                tmp_r=r
            if c<tmp_c:
                tmp_c=c
    if tmp_r<tr:
        start_r=tmp_r
    elif tmp_r>tr:
        start_r=tr
    
    if tmp_c<tc:
        start_c=tmp_c
    elif tmp_c>tc:
        start_c=tc
    
    return start_r,start_c,start_r+min_dis,start_c+min_dis

def rotation_90(start_r,start_c,end_r,end_c):
    global board, tr,tc
    
    new_N = end_r - start_r + 1
    new_board = [[0]*new_N for _ in range(new_N)]
    for r in range(new_N):
        for c in range(new_N):
            new_board[r][c] = board[start_r+r][start_c+c]
    
    for pid in players:
        x,y=players[pid]
        if start_r<=x<=end_r and start_c<=y<=end_c:
            board[x][y] = -pid
    
    board[tr][tc]='e'
    
    for r in range(new_N):
        for c in range(new_N):
            if board[start_r+r][start_c+c] != 'e' and board[start_r+r][start_c+c] > 0:
                board[start_r+r][start_c+c] -= 1
            new_board[c][new_N-1-r] = board[start_r+r][start_c+c]
    
    for r in range(new_N):
        for c in range(new_N):
            if new_board[r][c] =='e':
                tr,tc = start_r+r,start_c+c
                new_board[r][c]=0
            if new_board[r][c] < 0:
                player_idx = -new_board[r][c]
                players[player_idx] = start_r+r,start_c+c
                new_board[r][c]=0
                
            board[start_r+r][start_c+c] = new_board[r][c]

def rotation_maze():
    # 1. 출구와 참가자 최소 1명을 포함한 가장 작은 크기의 정사각형 선정하기 
    # 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
    start_r,start_c,end_r,end_c = set_rect()
    
    # new_board = [[0]*N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         new_board[i][j]=board[i][j]
    
    rotation_90(start_r,start_c,end_r,end_c)


def print_board(board):
    for b in board:
        print(b)
    print()

if __name__=="__main__":
    N,M,K=map(int, input().split()) # 미로의 크기, 참가자 수, 게임시간 
    board = [list(map(int, input().split())) for _ in range(N)]
    
    
    players={}
    players_dis={}
    for i in range(1,M+1):
        r,c=map(int, input().split())
        players[i]=[r-1,c-1]
        players_dis[i]=0
    
    tr,tc = map(int, input().split())
    tr,tc = tr-1,tc-1
    # target=[tr,tc]
    
    for t in range(1,K+1):
        players_move()
        rotation_maze()
        if not players:
            break 
        # print_board(board)
    
    total_dis=0
    for pid in range(1,M+1):
        total_dis += players_dis[pid]
    
    print(total_dis)
    print(tr+1,tc+1)