import sys 

def is_beautiful(n):
    idx = 0       
    # 연달아 같은 숫자가 나오는 시작 위치를 잡는다. 
    while idx < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 즉 현재 위치(idx)에서 seq[idx]개 만큼 점프할건데 그걸 n자리수를 넘어가면
        # 아름다운 수 조건에 위배됨 
        if idx + seq[idx] - 1 >= n:
            return False
        
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인
        for j in range(idx, idx + seq[idx]):
            if seq[j] != seq[idx]:  # 연속하는가?
                return False
            
        idx += seq[idx]     # idx는 idx번째 수 만큼 점프함 
                            # 예) idx가 0이고 seq[0]가 2면 2칸씩 연속한지 확인할 것임 
    return True


def DFS(cnt):
    global ans
    
    if cnt == n:
        if is_beautiful(n): # n자리 수가 정해지면 그게 아름다운 수인지 확인
            ans += 1
        return
	
    # 1이상 4이하의 숫자로만 이루어져 있으면서, 
    for i in range(1, 5):   # 예) 111에서 444까지
        seq.append(i)
        DFS(cnt + 1)
        seq.pop()

if __name__=="__main__":
    n = int(input())        # n자리 
    ans = 0
    seq = []
    DFS(0)
    print(ans)