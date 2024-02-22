import sys

if __name__=="__main__":
    N,M=map(int, input().split())
    arr=[]
    for i in range(N):
        boom=int(input())
        arr.append(boom)
    
    # if len(arr)==M:
    #     print(0)
    #     sys.exit()
    
    while arr:
        cnt=0
        delete_list=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                cnt+=1
            else:
                if cnt>=M-1:
                    delete_list += list(range(i-cnt,i+1))
                    cnt=0
        
        if cnt>=M-1:
            if i>0:
                delete_list += list(range(i+1-cnt,i+1+1))
            elif i==0:
                delete_list += list(range(i-cnt,i+1))
            cnt=0
        
        if not delete_list:
            break
        
        new_arr=[]
        for i in range(len(arr)):
            if i in delete_list:
                continue
            new_arr.append(arr[i])
        
        arr = new_arr
                 
            
    print(len(arr))
    if arr:
        for a in arr:
            print(a)