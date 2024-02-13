import sys


if __name__=="__main__":
    N=int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    h=3
    w=3
    ans=0
    for i in range(0,N-h+1):
        for j in range(0,N-w+1):
            tmp_ans = 0
            for row in board[i:i+h]:
                tmp_ans += sum(row[j:j+w])
            ans = max(ans, tmp_ans)
            
    print(ans)