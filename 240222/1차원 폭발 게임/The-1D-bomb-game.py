import sys

if __name__=="__main__":
    N,M=map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    
    while arr:
        delete_list=[]
        cnt=1
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                cnt += 1
            else:
                if cnt>=M:
                    delete_list+=list(range(i-cnt,i))
                    cnt=0
        
        if cnt>=M:
            delete_list+=list(range(len(arr)-cnt,len(arr)))
        
        if delete_list:
            new_arr=[]
            for j in range(len(arr)):
                if j in delete_list:
                    continue
                new_arr.append(arr[j])
            
            arr = new_arr
        else:
            break
    
    print(len(arr))
    if arr:
        for a in arr:
            print(a)