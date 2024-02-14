import sys

def in_range(r,c):
    return 0<=r<n and 0<=c<n

def filter(x,y):
    ans=0
    for k in range(max_k):
        cost = k**2+(k+1)**2
        profit=0
        cnt=0
        for i in range(2*k+1):
            if i<=k:
                for j in range(-i,i+1):
                    if in_range(x-k+i,y+j) and board[x-k+i][y+j]==1:
                        profit+=5
                        cnt+=1
            else:
                for j in range(-(i%k),(i%k)+1):
                    if in_range(x-k+i,y+j) and board[x-k+i][y+j]==1:
                        profit+=5
                        cnt+=1
        profit -= cost
        if profit>0:
            ans = max(ans, cnt)

    return ans

if __name__=="__main__":
    n,m=map(int, input().split())   # nxn,  m:금 하나의 가격 
    board = [list(map(int, input().split())) for _ in range(n)]
    # n이 3일때, k는 최대 2
    # n이 5일때, k는 최대 4
    max_k=n-1
    answer = 0
    for i in range(n):
        for j in range(n):

            tmp=filter(i,j)
            answer = max(answer,tmp)
            
    print(answer)