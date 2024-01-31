import sys 
import heapq
# sys.stdin=open('input.txt','r')
input=sys.stdin.readline

# 상, *상우, 우, *우하, 하, *하좌, 좌, *좌상 
cdxs=[-1,-1,0, 1, 1, 1, 0, -1]
cdys=[0, 1, 1, 1, 0, -1,-1,-1]

# 상우하좌 
pdxs=[-1, 0, 1,  0]
pdys=[0,  1, 0, -1]

def in_range(nx,ny):
    return 0<nx<N+1 and 0<ny<N+1

def print_board(board):
    for b in board:
        print(b)
    print('--------------')

def Distance(r1,c1, r2,c2):
    return (r1-r2)**2 + (c1-c2)**2

def Interaction(nx,ny,dx,dy):
    global all_in_board
    origin_player_id=board[nx][ny]
    origin_player_loc=players_loc[origin_player_id]
    opx,opy=origin_player_loc
    nx=opx+dx
    ny=opy+dy
    if not in_range(nx,ny):
        players_loc[origin_player_id]=[-1,-1]
        del playerIdToIndx[origin_player_id] # 삭제 
        all_in_board-=1
        return
    
    if board[nx][ny]>0: # 튕겨져나간 새 위치에 또 참가자가 있으면 
        Interaction(nx,ny,dx,dy)
    
    board[nx][ny]=origin_player_id
    players_loc[origin_player_id]=[nx,ny]
    

# 충돌 1. 소가 참가자를 박음 
def crush_cow_to_player(t,cx,cy,dir):
    global board, cow_loc, players_loc, players_score, all_in_board
    pid=board[cx][cy]
    px,py=players_loc[pid]
    if players_loc[pid]!=[cx,cy]:
        raise Exception('Error')
    players_score[pid]+=C           # C만큼 점수를 얻음 
    panic_time[pid]=t+1
    px,py=players_loc[pid]
    nx,ny=px,py
    dx=cdxs[dir]               # 반대방향 
    dy=cdys[dir]

    nx=nx+dx*C
    ny=ny+dy*C
    if not in_range(nx,ny):     # 격자를 벗어남
        players_loc[pid]=[-1,-1]
        board[px][py]=0         # 그 위치에 있던 사람은 없어지고 
        del playerIdToIndx[pid] # 삭제 
        all_in_board-=1
        return
    
    if board[nx][ny]>0: # 튕겨져 나간 곳에 사람이 있으면 
        Interaction(nx,ny,dx,dy)
    
    # 기존사람이 있든 없든 튕겨진 사람은 새로운 위치로  
    players_loc[pid]=[nx,ny]
    board[px][py]=0         # 기존 위치는 비우고 
    board[nx][ny]=pid        
            
    

# 충돌 2. 참가자가 소를 박음 
def crush_player_to_cow(t,pid,dir):
    global board, cow_loc, players_loc, players_score, all_in_board
    px,py=players_loc[pid]
    nx,ny=cow_loc
    players_score[pid]+=D       # D만큼 점수를 얻음 
    panic_time[pid]=t+1
    dx=-pdxs[dir]               # 반대방향 
    dy=-pdys[dir]
    

    nx=nx+dx*D
    ny=ny+dy*D
    if not in_range(nx,ny):     # 튕겨져 나간곳이 격자 밖이면 
        players_loc[pid]=[-1,-1]
        board[px][py]=0
        del playerIdToIndx[pid] # 삭제 
        all_in_board-=1
        return 
            
    
    if board[nx][ny]>0: # 튕겨져 나간 곳에 사람이 있으면 
        Interaction(nx,ny,dx,dy)
    
    # 아니면 튕겨져나간곳이 새로운 그사람 위치 
    players_loc[pid]=[nx,ny]
    board[px][py]=0
    board[nx][ny]=pid

    
    
    

def player_move(t,pid):
    global board, cow_loc, players_loc

    cx,cy=cow_loc
    px,py=players_loc[pid]
    possible_loc=[]
    cur_dis=Distance(px,py, cx,cy)
    for dir in range(4):
        nx=px+pdxs[dir]
        ny=py+pdys[dir]
        if in_range(nx,ny) and board[nx][ny]<=0: 
            dis=Distance(nx,ny, cx,cy)
            if dis<cur_dis:
                priority=[dis,dir,nx,ny]
                heapq.heappush(possible_loc,priority)
            
    if len(possible_loc)==0:             # 4가지 경우 중 모두 없는 경우 끝냄 
        return

    dis,dir,nx,ny=heapq.heappop(possible_loc)
    board[px][py]=0
    if (nx,ny)==(cx,cy):    # 참가자가 소를 박음 
        crush_player_to_cow(t,pid,dir)
    else:
        # 참가자가 소를 박은게 아니라면 
        # 참가자 이동 
        board[nx][ny]=pid
        players_loc[pid]=[nx,ny]
            
def cow_move(t):
    global board, cow_loc
    x,y=cow_loc
    
    final_possible_loc=[]
    # if t == 2:
    #     print('here')
    # # 상하좌우 한칸씩만 갈때 참가자가 있는경우가 가장 가까운 경우 
    # for dir in range(0,8,2):
    #     nx=x+cdxs[dir]
    #     ny=y+cdys[dir]
    #     if in_range(nx,ny) and board[nx][ny]>0:
    #         priority=[0,-nx,-ny,dir,nx,ny]
    #         heapq.heappush(final_possible_loc,priority)
            
    # if len(final_possible_loc)!=0:             # 8가지 경우중 모두 없는 경우, 격자를 벗어나는 경우 끝냄 
        
    #     dis,px,py,dir,nx,ny=heapq.heappop(final_possible_loc) 
    #     crush_cow_to_player(t,nx,ny,dir)
    #     # 참가자랑 박치기를 하든 안하든 소가 이동만 한다 
    #     board[x][y]=0
    #     board[nx][ny]=-1
    #     cow_loc=[nx,ny]
    #     return
    
    
    for dir in range(8):
        nx=x+cdxs[dir]
        ny=y+cdys[dir]
        one_box_dis=Distance(nx,ny, x,y)
        possible_loc=[]
        if in_range(nx,ny):
            # if board[nx][ny]>0: # 바로 사람이 있는  경우
            #     crush_cow_to_player(t,nx,ny,dir)
            #     # 참가자랑 박치기를 하든 안하든 소가 이동만 한다 
            #     board[x][y]=0
            #     board[nx][ny]=-1
            #     cow_loc=[nx,ny]
            #     return
                
            for pid in range(1,P+1):
                px,py=players_loc[pid]
                dis=Distance(nx,ny, px,py)# +one_box_dis
                # if dis==0:
                priority=[dis,one_box_dis,-px,-py,dir,nx,ny]
                heapq.heappush(possible_loc,priority)
            
            heapq.heappush(final_possible_loc, heapq.heappop(possible_loc))
    
    # 8가지 방향중 가장 가까운 참가자에거 감 
    if len(final_possible_loc)==0:             # 8가지 경우중 모두 없는 경우, 격자를 벗어나는 경우 끝냄 
        return
    dis,_,px,py,dir,nx,ny=heapq.heappop(final_possible_loc)
    px*=-1
    py*=-1
    target_player_id=board[px][py]
    if (px,py)==(nx,ny):
        crush_cow_to_player(t,nx,ny,dir)

    
    # 참가자랑 박치기를 하든 안하든 소가 이동만 한다 
    board[x][y]=0
    board[nx][ny]=-1
    cow_loc=[nx,ny]
        
                
        

def simulation(t):
    cow_move(t)
    # print('cow_move')
    # print_board(board)
    # 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
    if len(playerIdToIndx)==0:
        return 
    for pid in range(1,P+1):  
        if playerIdToIndx.get(pid)==None or players_loc[pid]==[-1,-1]:
            continue
        if panic_time[pid]<t:
            player_move(t, pid)
        # print_board(board)
        # 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
        if len(playerIdToIndx)==0:
            return
    # 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여합니다.
    for pid in playerIdToIndx:
        players_score[pid]+=1

if __name__=="__main__":
    # N:게임격자, M: 게임턴수, P:산타개수, C:루돌프 힘, D: 산타의 힘 
    N, M, P, C, D = map(int, input().split())
    cow_loc=list(map(int, input().split()))
    
    board=[[0]*(N+1) for _ in range(N+1)]
    board[cow_loc[0]][cow_loc[1]]=-1
    
    playerIdToIndx={}
    
    players_loc=[[0,0] for _ in range(P+1)]
    players_score=[0]*(P+1)
    all_in_board=P
    panic_time=[0]*(P+1)
    
    for _ in range(1,P+1):
        pid,x,y,=map(int, input().split())
        board[x][y]=pid
        players_loc[pid]=[x,y]
        playerIdToIndx[pid]=[x,y]
        
    # print_board(board)
    
    for t in range(1,M+1):
        # print('<<<<<<<<<<<<<<<<<')
        # print('time:',t)
        simulation(t)
        # print('players moved')
        # print(players_loc[1:])
        # print(players_score[1:])
        # print()
        # print_board(board)
        # print('>>>>>>>>>>>>>>>>>')
        if all_in_board==0:
            break

    print(*players_score[1:])