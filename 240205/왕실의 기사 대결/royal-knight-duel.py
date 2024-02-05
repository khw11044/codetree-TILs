import sys

def direction(d):
    if d == 0:
        dx,dy=-1,0
    elif d == 1:
        dx,dy=0,1
    elif d == 2:
        dx,dy=1,0
    elif d == 3:
        dx,dy=0,-1
    return dx,dy

def person_move(pid, dx,dy):
    global people_board, person_loc
    r,c,h,w,k = person_loc[pid]
    for i in range(h):
        for j in range(w):
            people_board[r+i][c+j] = 0
    for i in range(h):
        for j in range(w):
            people_board[r+i+dx][c+j+dy] = -pid
    person_loc[pid] = [r+dx,c+dy,h,w,k]

def check_wall(pid,dx,dy):
    r,c,h,w,k = person_loc[pid]
    for i in range(h):
        for j in range(w):
            if board[r+i+dx][c+j+dy] == 2:  # 벽이 하나라도 있으면 
                return False
    return True

# 연쇄반응 
def Interaction(pid, dx,dy, new_pid, move_person_list):  # 재귀함수 
    # 그 다음에 벽이 있는지 확인 
    # 기사 움직일 수 있는지 없는지 확인 
    r,c,h,w,k = person_loc[new_pid]
    
    can_move=True
    # 이동할 곳에 벽이 있는지 없는지 부터 확인 
    if not check_wall(new_pid,dx,dy):
        return False, move_person_list
    
    # 이동할 위치에 다른 기사가 있는지 확인 
    for i in range(h):
        for j in range(w):
            if people_board[r+i+dx][c+j+dy] != 0 and people_board[r+i+dx][c+j+dy] != -new_pid:    # 다른 기사가 있으면 
                can_move, move_person_list = Interaction(new_pid, dx,dy, -people_board[r+i+dx][c+j+dy], move_person_list)
                if not can_move:    # 
                    # # 연쇄작용이 안된다는 것을 알았을때, 연쇄작용으로 움직인 다른 기사를 다시 되돌려야함 
                    # temp_person_loc[pid] = person_loc[pid]
                    return can_move, move_person_list
                
    # 움직일 수 있으면 
    if can_move:
        if new_pid not in move_person_list:
            move_person_list.append(new_pid)
            temp_person_loc[new_pid] = [r+dx, c+dy, h,w,k]
    
    return can_move, move_person_list

def check_trap(pid):
    global scores
    r,c,h,w,k = temp_person_loc[pid]
    for i in range(h):
        for j in range(w):
            if board[r+i][c+j] == 1:    # 함정이 있으면 
                k-=1
                scores[pid] += 1
                if k == 0:
                    break 
        if k == 0:
            break 
        
    if k == 0:
        del person_loc[pid]
        for i in range(h):
            for j in range(w):
                people_board[r+i][c+j]=0
    else:
        person_loc[pid] = [r,c,h,w,k]
    
    
    

# 이동할 위치에 다른 기사가 있는지 확인 
def check_person(pid,dx,dy):
    can_move = True
    move_person_list=[]
    for i in range(h):
        for j in range(w):
            if people_board[r+i+dx][c+j+dy] != 0 and people_board[r+i+dx][c+j+dy] != -pid:    # 다른 기사가 있으면 
                # 연쇄작용을 확인하고 최종적으로 이동 가능하면 True 
                can_move,move_person_list = Interaction(pid, dx,dy, -people_board[r+i+dx][c+j+dy], move_person_list)
                if not can_move:
                    # # 연쇄작용이 안된다는 것을 알았을때, 연쇄작용으로 움직인 다른 기사를 다시 되돌려야함 
                    # temp_person_loc[pid] = person_loc[pid]
                    return can_move
    
    for pid in move_person_list:
        person_move(pid, dx,dy)
        check_trap(pid)
        
    return can_move

def print_board(people_board):
    for p in people_board:
        print(p)
    print('----'*5)

# 체스판 밖도 벽으로 간주합니다.
if __name__=="__main__":
    # L:체스판의 크기, N:기사의 수, Q:명령의 수 
    L,N,Q=map(int, input().split()) 
    # L×L 크기의 체스판에 대한 정보
    board = [[2]*(L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2]*(L+2)]
    people_board = [[0]*(L+2) for _ in range(L+2)]
    # 초기 기사들의 정보
    person_loc = {}
    temp_person_loc = {}
    for pid in range(1,N+1):
        r,c,h,w,k=map(int, input().split()) # 기사의 처음 위치: (r,c), h,w: 세로, 가로, k: 초기체력
        person_loc[pid] = [r,c,h,w,k]
        temp_person_loc[pid] = [r,c,h,w,k]
        for i in range(h):
            for j in range(w):
                people_board[r+i][c+j] = -pid
    
    scores = [0]*(N+1)
    # Q개의 왕의 명령 
    for _ in range(Q):
        pid,d = map(int, input().split()) # i번의 기사에게 방향 d로 한칸 이동하라는 명령 
        if person_loc.get(pid)==None:
            continue
        r,c,h,w,k = person_loc[pid]
        dx,dy = direction(d)
        
        # 기사 이동, 다른 기사들 위치 확인하고 연쇄반응일으키는지 확인, 연쇄 반응 안일으키거나 일으켜도 이동가능하면 이동 
        can_move=True
        # 이동할 곳에 벽이 있는지 없는지 부터 확인 
        can_move = check_wall(pid,dx,dy)
        
        # 이동할 곳에 벽이 없어서 이동 가능하면, 이동할 곳에 다른 기사가 있는지 확인 
        if can_move:
            can_move = check_person(pid,dx,dy)

        # 연쇄작용 다 확인했는데 이동 가능하면 최종적으로 이동 
        if can_move:
            can_move = person_move(pid,dx,dy)
        
        # 대결 대미지 적용 
        
        print_board(people_board)
        print()
    
    answer = 0
    for pid in person_loc:
        answer += scores[pid]
    
    print(answer)