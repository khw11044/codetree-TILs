import sys


# 너비, 높이 모두 1일때 4개칸 순환
dxs=[-1,-1,1,1]
dys=[1,-1,-1,1]



def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n

def get_score(x,y,w,h):
    move_size=[w,h,w,h]
    
    total=0
    for dx,dy,length in zip(dxs,dys,move_size):
        for _ in range(length): # 처음 올라가는 대각선으로 length 만큼 옮겨봄 
            x = x+dx
            y = y+dy
            
            # 범위에 벗어나면 이 w,h에 대해서는 나가리니깐 
            # 그냥 바로 return 0으로 끝내줘 버림 
            if not in_range(x,y):
                return 0
            # 한칸 한칸 올라가면서 범위 안 벗어나면 더해주고 방향바꿔가며 시작지점까지 옴
            total += board[x][y]
    
    return total
            
    

if __name__=="__main__":
    n=int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    ans=0
    for i in range(n):          # 보드 범위, 보드 완전탐색 
        for j in range(n):
            # (i,j)일때 가능한 최대 너비(w)와 최대 높이(h)의 직사각형을 생각해보자 
            for w in range(1,n):
                for h in range(1,n):
                    #(i,j)를 시작으로 w너비와 h높이를 가지는 직사각형 점수
                    ans=max(ans, get_score(i,j,w,h))    
    
    print(ans)