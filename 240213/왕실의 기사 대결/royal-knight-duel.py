import sys
from collections import deque

moves = [(-1,0),(0,1),(1,0),(0,-1)]


def in_range(nx,ny,h,w):
    return 1<=nx<=L+1-h and 1<=ny<=L+1-w

def try_move(pid,d):
    KQ=deque()
    KQ.append(pid)
    is_moved[pid]=True 
    
    # 초기화 단계 
    for i in range(1,N+1):
        dmg[i]=0
        is_moved[i]=False
        new_r[i]=r[i]
        new_c[i]=c[i]
    
    while KQ:
        x=KQ.popleft()
        new_r[x] += moves[d][0]
        new_c[x] += moves[d][1]
        
        # 범위 넘어가는지 확인 
        if not in_range(new_r[x],new_c[x],h[x],w[x]):
            return False
        
        # 함정이거나 벽인지 확인 
        for i in range(new_r[x],new_r[x]+h[x]):
            for j in range(new_c[x],new_c[x]+w[x]):
                if board[i][j]==1:  # 함정이면 
                    dmg[x]+=1
                if board[i][j]==2:  # 벽이면 
                    return False
        
        # 다른 기사와 충돌하는지 확인 
        for idx in range(1,N+1):
            if is_moved[idx] or k[idx]<=0:  # 체력없는 pid 기사는 안움직임 
                continue
            # 다른기사의 위치가 현재 기사의 새로운 위치 범위보다 멀면, 
            # 또는 현재 기사의 새로운 위치가 다른기사 범위 밖에 있으면, 즉 연쇄반응이 안일어나면 
            if (r[idx]>new_r[x]+h[x]-1) or (new_r[x] > r[idx]+h[idx]-1):
                continue
            if (c[idx]>new_c[x]+w[x]-1) or (new_c[x] > c[idx]+w[idx]-1):
                continue
            
            is_moved[idx]=True 
            KQ.append(idx)
    
    dmg[pid]=0
    return True
            

def move(pid,d):
    if k[pid]<=0:
        return
    
    if try_move(pid, d):
        for idx in range(1,N+1):
            r[idx]=new_r[idx]
            c[idx]=new_c[idx]
            k[idx] -= dmg[idx]
        

if __name__=="__main__":
    L,N,Q=map(int, input().split())
    board = [[0]*(L+2)] + [[2] + list(map(int, input().split())) + [0] for _ in range(L)] + [[0]*(L+2)]
    MAX_N = 31  # 최대 기사 수 
    MAX_L = 41  # 최대 체스판 크기 
    
    r=[0]*31    # 기사 위치 행 
    c=[0]*31    # 기사 위치 열 
    h=[0]*31    # 기사 범위 세로
    w=[0]*31    # 기사 범위 가로 
    k=[0]*31    # 초기 체력 k 
    new_r=[0]*31
    new_c=[0]*31
    dmg=[0]*31
    is_moved=[False]*31
    init_k = [0]*31
    
    for pid in range(1,N+1):
        r[pid],c[pid],h[pid],w[pid],k[pid]=map(int, input().split())
        init_k[pid]=k[pid]
    
    # 왕의 명령 
    for _ in range(Q):
        i,d=map(int, input().split())   # i번 기사에게 방향 d 
        move(i,d)
    
    # 생존한 기사들이 총 받은 대미지의 합을 출력
    ans = sum([init_k[i] - k[i] for i in range(1,N+1) if k[i]>0])
    print(ans)