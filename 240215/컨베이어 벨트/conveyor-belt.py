import sys

if __name__=="__main__":
    n,t=map(int, input().split())   # n:벨트길이, t=t초후 
    up=list(map(int, input().split()))
    down=list(map(int, input().split()))
    
    for i in range(1,t+1):
        tmp1=up[-1]
        tmp2=down[-1]
        for j in range(n-1):
            up[n-1-j]=up[n-2-j]
            down[n-1-j]=down[n-2-j]
        up[0]=tmp2
        down[0]=tmp1
    
    print(*up)
    print(*down)