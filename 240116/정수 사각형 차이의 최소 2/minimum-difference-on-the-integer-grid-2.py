import sys

def check():
    d = [[1e9]*n for _ in range(n)]
    d[0][0] = board[0][0]

    for j in range(1, n):
        d[0][j] = max(d[0][j-1], board[0][j])
    
    for i in range(1, n):
        d[i][0] = max(d[i-1][0], board[i][0])

    for i in range(1, n):
        for j in range(1, n):
            d[i][j] = max(min(d[i-1][j], d[i][j-1]), board[i][j])
    
    return d[n-1][n-1]  # 1e9면 경로 없음!


if __name__=="__main__":

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    INT_MAX=sys.maxsize

    res = INT_MAX  # |최대-최소|의 최소!
    for low in range(1, 101):
        for i in range(n):
            for j in range(n):
                if board[i][j] < low:
                    board[i][j] = INT_MAX

        ans = check()
        if ans < INT_MAX:
            res = min(res, abs(ans-low))

    print(res)