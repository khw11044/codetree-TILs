import sys

from collections import deque

def get_length(arr):
    arr = list(arr)
    new_arr = ''
    cnt=1
    for i in range(N-1):
        if arr[i] == arr[i+1]:
            cnt += 1
        else:
            new_arr += arr[i] + str(cnt)
            cnt=1
        
        if i+1 == N-1:
            new_arr += arr[i] + str(cnt)
            
    return len(new_arr)
    

if __name__=="__main__":
    strings = list(map(str, input()))
    N = len(strings)
    strings = deque(strings)
    
    init_length = get_length(strings)
    
    for i in range(1,N):
        strings.rotate(i)
        init_length = min(init_length, get_length(strings))
        
    print(init_length)