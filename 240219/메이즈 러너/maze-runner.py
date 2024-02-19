import sys


# 모든 참가자를 이동시킵니다.
def move_all_traveler():
    global exits, ans
    # M명의 모든 참가자들에 대해 이동을 진행시킨다. 
    for i in range(1,M+1):      # 1번 참가자부터 M번 참가자까지
        if traveler[i]==exits:  # 이미 ㅑ번 참가자가 탈출구 위치에 있으면  
            continue            # 스킵하고 다음 참가자 보기 
        
        tx,ty=traveler[i]
        ex,ey=exits
        
        tx, ty = traveler[i]
        ex, ey = exits

        # 1. 우선순위인 행이 다른 경우 행을 위 아래로 이동시켜본다. 
        if tx!=ex:
            nx,ny=tx,ty
            if ex>nx:   # 만약 탈출구가 더 아래 있으면 
                nx+=1
            else:
                nx-=1

            if not board[nx][ny]:           # 새 위치가 벽이 아니라 이동 가능한 곳이면 
                traveler[i] = (nx, ny)      # i번 참가자 nx,ny로 이동 
                ans += 1                    # 이동 거리 증가 
                continue                    # 이동했으면 이제 다음 참가자 보자 

        # 2. 행은 같은데 열이 다른 경우 
        if ty!=ey:       
            nx,ny=tx,ty
            if ey>ny:
                ny+=1
            else:
                ny-=1

            if not board[nx][ny]:           # 새 위치가 벽이 아니라 이동 가능한 곳이면 
                traveler[i] = (nx, ny)      # i번 참가자 nx,ny로 이동 
                ans += 1                    # 이동 거리 증가 
                continue                    # 이동했으면 이제 다음 참가자 보자 


# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
def find_minimum_square():
    global exits, sx, sy, square_size
    ex,ey=exits

    # 발상의 전환!! 가장 작은 정사각형부터 모든 정사각형을 만들어 본다 
    for sz in range(2,N+1):                 # 변의 길이가 2인 정사각형부터 N인 정사각형까지 
        for x1 in range(1, N-sz+2):         # x위치가 1에서 변의 길이를 고려한 x위치  가장 좌상단 조건 때문
            for y1 in range(1, N-sz+2):     # y위치가 1에서 변의 길이를 고려한 y위치  가장 좌상단 조건 때문
                x2=x1+sz-1
                y2=y1+sz-1
 
                if not (x1 <= ex <= x2 and y1 <= ey <= y2): # 만약 출구가 해당 정사각형에 없으면 
                    continue                                # 다음 위치 또는 크기의 정사각형 확인하기 

                # 해당 정사각형에 탈출구는 있고 한명 이상의 참가자가 있는지 확인 
                is_traveler_in = False
                for l in range(1, M + 1):
                    tx, ty = traveler[l]
                    if x1 <= tx <= x2 and y1 <= ty <= y2:
                        if not (tx == ex and ty == ey):     # 탈출구위에 참가자 있는 참가자는 제외
                            is_traveler_in = True

                # 해당 정사각형에 탈출구도 있고 참가자도 한명이상 있으면 
                if is_traveler_in:      # 회전시킬 정사각형 정보 갱신하고 회전하러 종료 
                    sx = x1
                    sy = y1
                    square_size = sz
                    return


# 4. 정사각형 내부의 벽의 내구도 감소시키고 회전시킨다.
def rotate_square():
    # 1. 회전시킬 정사각형에 있는 벽들 모두 내구도 감소시킴
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if board[x][y]: 
                board[x][y] -= 1

    # 2. 정사각형을 시계방향으로 90도 회전 
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            ox, oy = x - sx, y - sy
            rx, ry = oy, square_size - ox - 1
            next_board[rx + sx][ry + sy] = board[x][y]

    # next_board 값을 현재 board에 옮겨줍니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            board[x][y] = next_board[x][y]


# 모든 참가자들 및 출구를 회전시킵니다.
def rotate_traveler_and_exit():
    global exits
    # 1. 모든 참가자 확인하고 회전
    for i in range(1, M + 1):
        tx,ty=traveler[i]
        # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전
        if sx<=tx<sx+square_size and sy<=ty<sy+square_size:
            ox,oy=tx-sx,ty-sy
            rx,ry=oy,square_size-ox-1
            traveler[i]=(rx+sx,ry+sy)

    # 2. 탈출구 회전
    ex,ey=exits
    if sx<=ex<sx+square_size and sy<=ey<sy+square_size:
        ox,oy=ex-sx,ey-sy
        rx,ry=oy,square_size-ox-1
        exits=(rx + sx, ry + sy)

if __name__=="__main__":
    
    N,M,K=map(int, input().split())     # 미로의크기, 참가자 수, 게임시간
    board=[[0]*(N+1)]
    for _ in range(N):
        board.append([0]+list(map(int, input().split())))
        
    # 회전 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해 준다. 
    next_board=[[0]*(N+1) for _ in range(N+1)]
    
    # 참가자의 위치 정보를 기록해줍니다.
    traveler = [(-1, -1)] + [list(map(int, input().split())) for _ in range(M)]
    
    # 출구의 위치 정보를 기록해줍니다.
    exits=list(map(int, input().split()))
    
    # 정답(모든 참가자들의 이동 거리 합)을 기록해줍니다.
    ans = 0
    
    # 회전해야 하는 최소 정사각형을 찾아 기록해줍니다.
    sx, sy, square_size = 0, 0, 0

    # 모두 탈출한게 아니면 K시간 동안 진행되고 K시간 전에 모두 탈출하면 그만 하면 된다. 
    for _ in range(K):
        # 1. 모든 참가자를 이동시킨다
        move_all_traveler()
        
        # 2. 모든 참가자 중에 탈출했는지 판단한다
        is_all_escape=True
        for i in range(1,M+1):
            if traveler[i]!=exits:  # 한명이라도 탈출 안했으면 
                is_all_escape=False
        # 2-1. 만약 모든 사람이 탈출했으면 바로 종료한다.  
        if is_all_escape:
            break
        
        # 3. 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾는다. 
        find_minimum_square()
        
        # 4. 정사각형 내부의 벽의 내구도 감소시키고 회전시킨다. # 4-1. 참가자들 및 출구를 회전시킨다.
        rotate_square()
        rotate_traveler_and_exit()
        
    
    
    print(ans)      # 모든 참가자들 최종 이동 거리 정답
    print(*exits)   # 마지막 탈출구 위치