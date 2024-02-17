import sys

'''
두 직사각형이 겹쳐지는지 확인하는 새로운 배열을 이용하면 비교적 쉽게 계산할 수 있다. 

'''

def rect_sum(x1, y1, x2, y2):
    return sum([board[i][j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)])

def clear_board():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
            
def check_board():
    # 동일한 칸을 2개의 직사각형이 모두 포함한다면
    # 겹치게 됩니다.
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                return True
    return False

def draw(x1,y1,x2,y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            visited[i][j] += 1

def overlapped(x1,y1,x2,y2, i,j,k,l):
    clear_board()   # 모두 0으로 리셋 
    draw(x1,y1,x2,y2)
    draw(i,j,k,l)
    return check_board()
    

# 첫번째 직사각형 (x1,y1,x2,y2)를 양 꼭지점으로 할때,
# 두번째 직사각형을 겹치지 않게 잡아 
# 최대 합을 반환하는 함수 
def find_max_sum_with_rect(x1,y1,x2,y2):
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    # overlapped은 겹치면 True 
                    if not overlapped(x1,y1,x2,y2, i,j,k,l):
                        max_sum = max(max_sum, rect_sum(x1,y1,x2,y2)+rect_sum(i,j,k,l))
    return max_sum 

if __name__=="__main__":
    n,m=map(int, input().split())   # n*m 
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    INT_MIN = -sys.maxsize
    '''
    1. board에서 2 블록을 고른다. 
    2. 범위를 정한다.
    2.1 범위가 서로 안겹쳐야 한다
    3. 가장 값이 큰것을 저장한다. 
    '''
    
    max_sum = INT_MIN
    # (i,j)와 (k,l)을 양쪽 꼭지점으로 하는 첫번째 직사각형을 먼저 정하고 
    # 그 중 최댓값을 찾는다.
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i,j,k,l))
            
    print(max_sum)