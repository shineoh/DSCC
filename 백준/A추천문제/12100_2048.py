# 12100 2048
# 2022-03-04
from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 방향
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def move(i, j, di, dj, check):
    ni, nj = i, j
    while 0 <= ni+di < N and 0 <= nj+dj < N: # 유효범위 체크
        if lst[ni+di][nj+dj] != 0: # 다음 칸이 비어있지 않을 때
            if lst[ni+di][nj+dj] == lst[i][j] and check[ni+di][nj+dj] == 0 and check[i][j] == 0 : # 다음 칸이 합쳐질 수 있는 칸이면
                lst[i][j] = lst[i][j]*2 # 합친 값 저장
                lst[ni+di][nj+dj] = 0 # 없어진칸 비우기
                check[ni+di][nj+dj] = 1 # 체크리스트에 체크
                check[i][j] = 1
                break
            else: # 합쳐질 수 없으며 칸이 비어있지않으면 break
                break
        # 한 칸씩 이동
        ni += di
        nj += dj
    lst[ni][nj], lst[i][j] = lst[i][j], lst[ni][nj] # 반복문 종료 후 현재 칸과 이동할 칸 체인지
    return 

def turn(lst, dd):
    di, dj = d[dd] # 방향 인덱스
    check = [[0] * N for _ in range(N)] # 합칠 수 있는지 여부 체크리스트
    if dd == 1 or dd == 2: # 좌나 상으로 이동 시
        for i in range(N): # 정방향 순회하며
            for j in range(N): 
                if lst[i][j] != 0: # 비어있지 않으면
                    move(i, j, di, dj, check) # 이동
    elif dd == 0 or dd == 3: # 우나 하로 이동시
        for i in range(N-1, -1, -1): # 반대로 순회하며
            for j in range(N-1, -1, -1):
                if lst[i][j] != 0: # 비어있지 않으면
                    move(i, j, di, dj, check) # 이동
    return lst # 변경된 리스트 반환

def bfs(lst): # 넓이 우선탐색
    q = deque([lst])
    ans = -1 # 답
    cycle = 0 # 반복 횟수
    while q:
        for _ in range(len(q)): # 있는 큐만큼
            lst = q.popleft() # 리스트를 빼서
            for dd in range(4): # 각 방향으로 이동시키기
                temp_lst = lst.copy() # 깊은복사
                nlst = turn(temp_lst, dd) # 해당 방향으로 이동한 리스트
                q.append(nlst) # 큐에 넣기

                # 최댓값 갱신
                for i in range(N):
                    for j in range(N):
                        if nlst[i][j] > ans:
                            ans = nlst[i][j]
        cycle += 1
        if cycle == 5: # 5번 이동시켰을때
            return ans # 답 반환

print(bfs(lst))

