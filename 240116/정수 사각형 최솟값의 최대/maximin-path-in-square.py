if __name__=="__main__":
    n=int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dp=[[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = board[0][0]
    
    # 최좌측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], board[i][0])
    
    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], board[0][j])

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), board[i][j])
    
    print(dp[n-1][n-1])