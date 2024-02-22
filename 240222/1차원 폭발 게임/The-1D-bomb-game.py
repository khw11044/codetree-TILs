import sys

def count_explode_bomb(start, num):
    for end in range(start + 1, len(arr)):  # 현재위치 다음 위치부터 끝까지 
        if arr[end] != num:
            return end - 1
        
    return len(arr) - 1

if __name__=="__main__":
    # 변수 선언 및 입력
    n, m = tuple(map(int, input().split()))
    arr = [int(input()) for _ in range(n)]

    while True:
        did_explode = False
        
        for start, num in enumerate(arr):
            if num == 0:
                continue

            end = count_explode_bomb(start, num)
            
            if (end-start+1) >= m:
                arr[start:end + 1] = [0] * (end - start + 1)    # 터질 폭탄의 num을 0으로 만듬 
                did_explode = True
            
        arr = list(filter(lambda x: x > 0, arr))
        '''
        또는 
        new_arr=[]
        for a in arr:
            if a!=0:
                new_arr.append(a)
        arr=new_arr
        '''
        
        if not did_explode:     # 리스트 한바퀴 돌면서 터진적이 없으면 더이상 터질게 없으므로 while문 탈출
            break

    print(len(arr))
    for num in arr:
        print(num)