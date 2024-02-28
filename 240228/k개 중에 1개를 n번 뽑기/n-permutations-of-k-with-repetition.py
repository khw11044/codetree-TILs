import sys 

def DFS():
    if len(ans)==N:
        print(*ans)
        return 
    else:
        for i in range(1,K+1):
            ans.append(i)
            DFS()
            ans.pop()
            
    

if __name__=="__main__":
    K,N=map(int, input().split())
    ans = []
    DFS()