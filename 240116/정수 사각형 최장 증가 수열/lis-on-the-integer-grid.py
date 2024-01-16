def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 정수값이 작은 칸부터 순서대로 보며
# 4방향에 대해 최적의 칸 수를 계산합니다.
dxs = [-1, 1,  0, 0]
dys = [ 0, 0, -1, 1]

# (x, y)에서 출발하여 조건을 만족하며
# 도달할 수 있는 칸의 수 중
# 최대 칸의 수를 구합니다.
def DFS(x, y):
    # 이미 계산해본적이 있다면
    # 그 값을 바로 반환합니다.
    if dp[x][y] != -1:
        return dp[x][y]

    # 기본값은 자기자신이 됩니다.
    best = 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and board[nx][ny] > board[x][y]:
            best = max(best, DFS(nx, ny) + 1)

    dp[x][y] = best
    return dp[x][y]

if __name__=="__main__":

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(n)]

    # 각 칸에 시작했을 떄
    # 최대로 이동할 수 있는 칸의 수 중 
    # 최댓값을 갱신합니다.
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, DFS(i, j))

    print(ans)