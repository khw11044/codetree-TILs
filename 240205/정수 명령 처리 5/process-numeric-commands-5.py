N=int(input())
arr = []
for _ in range(N):
    command = list(map(str, input().split()))
    if command[0]== 'push_back':
        arr.append(command[1])
    elif command[0]== 'get':
        # print(command[1])
        # print(int(command[1]))
        print(arr[int(command[1])-1])
    elif command[0]== 'size':
        print(len(arr))
    elif command[0]== 'pop_back':
        arr.pop()