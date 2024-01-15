n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def find_max_sum(x, y):
    # 도착 지점에 도착하면 최대 합을 갱신해줍니다.
    if x == n - 1 and y == n - 1:
        return grid[n - 1][n - 1]
    
    dxs, dys = [1, 0], [0, 1]
    
    # 가능한 모든 방향에 대해 탐색해줍니다.
    max_sum = 0 # 주어진 숫자의 범위가 1보다 크기 때문에 항상 갱신됨이 보장됩니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if in_range(new_x, new_y):
            max_sum = max(max_sum, find_max_sum(new_x, new_y) + grid[x][y])
            
    return max_sum
                    
print(find_max_sum(0, 0))