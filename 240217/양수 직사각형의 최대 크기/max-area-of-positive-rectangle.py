import sys
def check_all_positive(x1,y1,x2,y2):
    return all(board[i][j]>0 for i in range(x1,x2+1) for j in range(y1,y2+1))
                

if __name__=="__main__":
    n,m=map(int, input().split())   # n*m 
    board = [list(map(int, input().split())) for _ in range(n)]
    INT_MIN = -sys.maxsize
    
    max_area = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if check_all_positive(i,j,k,l):
                        max_area = max(max_area, (k-i+1)*(l-j+1))
                    else:
                        break

            
    print(max_area)