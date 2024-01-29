'''
사진 촬영을 진행했을 때 현재 코드트리 오마카세 집에 있는 사람 수와 남아 있는 초밥 수를 출력하면 됩니다.
Q 번에 걸쳐 명령을 순서대로 진행하며 알맞은 답을 출력하는 프로그램을 작성해보세요.
'''

import sys
from collections import deque

class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n


if __name__=="__main__":
    L,Q = map(int, input().split())     # L: 초발 벨트 길이, Q: 명령어의 수 
    
    # 명령들을 관리합니다.
    cmd_queries = {}
    
    seats = {}
    
    belt = [[] for _ in range(L)]
    Food_Q = deque(belt)
    
    time = 0
    total_time = 0
    people=0
    food=0
    for _ in range(Q):
        info = list(map(str, input().split()))
        cmd, t, x, name, n = -1, -1, -1, "", -1
        
        if info[0]=='100':                            # 주방장의 초밥 만들기
            cmd, tmp_t, x, name = info     # 구분, 시간, 위치, 이름    
            cmd, tmp_t, x = map(int, [cmd, tmp_t, x])
            # Food_Q[x].append(name)    
            # food+=1

            
        elif info[0]=='200':                          # 손님 입장 
            cmd, tmp_t, x, name, n = info   # 구분, 시간, 위치, 이름, 목표개수
            cmd, tmp_t, x, n = map(int, [cmd, tmp_t, x, n])
            # seats.append([x,name,n])
            # people+=1
            
        else:                                       # 사진 촬영 
            cmd, tmp_t = info                   # 구분, 시간 
            cmd, tmp_t = map(int, [cmd, tmp_t])

        if total_time < tmp_t:
            total_time = tmp_t
        
        # cmd_queries[tmp_t] = Query(cmd, tmp_t, x, name, n)
        cmd_queries[tmp_t] = [cmd, tmp_t, x, name, n]
        
    
    people_num, sushi_num = 0, 0
    for t in range(1, total_time+1):
        Food_Q.rotate(1)
        
        if cmd_queries.get(t):          # 시간 별 명령어 수행 
            cmd, tmp_t, x, name, n = cmd_queries[t]
            if cmd == 100:              # 초밥을 둠 
                if seats.get(x):
                    if seats[x][0] == name: # 초밥을 둘 위치에 해당하는 사람이 있으면 
                        seats[x][1] -= 1
                        if seats[x][1] == 0:
                            people_num -= 1
                            seats.pop(x, None)   # 자리에 사람 제거 
                else:                   # 아니면 
                    Food_Q[x].append(name)  # 벨트 위에 해당 이름의 초밥을 둠 
                    sushi_num += 1
                    
            elif cmd == 200:            # 사람이 앉는 명령어 
                seats[x] = [name,n]
                people_num += 1
            
        
        # else:                           # 해당 시간에 대한 명령어가 없으면 

        if len(seats) != 0:
            del_seat_list = []
            for seat in seats.items():
                k,v = seat
                cnt = len(Food_Q[k])
                while Food_Q[k]:
                    cnt -= 1
                    food = Food_Q[k].pop(0)
                    if v[0] == food:
                        v[1] -= 1
                        sushi_num -= 1
                        if v[1] == 0:
                            people_num -= 1
                            del_seat_list.append(k)
                            break
                        else:
                            seats[k][1] = v[1]
                    else:
                        Food_Q[k].append(food)
                    
                    if cnt == 0:
                        break

            for k in del_seat_list:
                seats.pop(k, None)
                            
                        
        if cmd == 300:
               print(people_num, sushi_num)             
                    
                    
    
    '''
    1. 100 초밥을 매 시간 위치에 놓고 회전시켜야함 
    2. 200 사람이 오면 자리에 앉고 목표 초밥 개수를 먹으면 떠나야함 
    3. 300 사람의 수와 초밥의 수를 출력한다. 
    *
    회전하고 초밥을 올려놓는다 
    '''