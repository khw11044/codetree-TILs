import sys


if __name__=="__main__":
    n,m=map(int, input().split())
    board = []
    answer = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        for i in range(n-m+1):
            if sum(row[i:i+m]) == row[i]*m:
                answer+=1
                break
                
    for cow in zip(*board):
        for i in range(n-m+1):
            if sum(cow[i:i+m]) == cow[i]*m:
                answer+=1
                break
            
    print(answer)