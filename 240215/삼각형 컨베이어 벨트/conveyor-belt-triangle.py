import sys


from collections import deque


if __name__=="__main__":
    n,t=map(int, input().split())   # n:벨트길이, t=t초후 
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    third = list(map(int, input().split()))
    
    total_list = deque(first + second + third)
    total_list.rotate(t)
    total_list = list(total_list)
    
    print(*total_list[:n])
    print(*total_list[n:2*n])
    print(*total_list[2*n:])