import sys

if __name__=="__main__":
    n=int(input())
    zenga = []
    for _ in range(n):
        zenga.append(int(input()))
    
    s1,e1=map(int, input().split())
    s2,e2=map(int, input().split())
    
    tmp=[]
    for i in range(n):
        if s1-1<=i<=e1-1:
            continue
        tmp.append(zenga[i])
        
    tmp2=[]
    for i in range(len(tmp)):
        if s2-1<=i<=e2-1:
            continue
        tmp2.append(tmp[i])
    
    print(len(tmp2))
    for t in tmp2:
        print(t)