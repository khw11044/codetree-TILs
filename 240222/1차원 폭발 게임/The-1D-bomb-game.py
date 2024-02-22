import sys


if __name__=="__main__":
    N,M=map(int, input().split())
    arr=[]
    for i in range(N):
        boom=int(input())
        if arr:
            if arr[-1] == boom:
                arr.pop()
            else:
                arr.append(boom)
        else:
            arr.append(boom)
    print(len(arr))
    if arr:
        for a in arr:
            print(a)