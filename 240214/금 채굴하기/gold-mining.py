import sys


def in_range(r,c):
    return 0<=r<n and 0<=c<n

def filter(x,y):
    ans=0
    for k in range(max_k):
        cost = k**2+(k+1)**2
        profit=0
        cnt=0
        for i in range(k):
            for j in range(y-i,y+i+1):
                if in_range(x-(k-i),j) and board[x-(k-i)][j]==1:
                    cnt+=1
                if in_range(x+(k-i),j) and board[x+(k-i)][j]==1:
                    cnt+=1
        # 마름모 가운데
        for l in range(y-k,y+k+1):
            if in_range(x,l) and board[x][l]==1:
                cnt += 1
        profit = cnt*m
        
        profit -= cost
        if profit>0:
            ans = max(ans, cnt)

    return ans

if __name__=="__main__":
    n,m=map(int, input().split())   # nxn,  m:금 하나의 가격 
    board = [list(map(int, input().split())) for _ in range(n)]
    # n이 3일때, k는 최대 2
    # n이 5일때, k는 최대 4
    max_k=n-1+1
    answer = 0
    
    for i in range(n):
        for j in range(n):
            tmp=filter(i,j)
            answer = max(answer,tmp)
            
    print(answer)