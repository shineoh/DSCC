# 토마토
# 2022-04-17
from collections import deque

def tomato():
    while q:
        si, sj = q.popleft()
        for di, dj in dir:
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 0:
                lst[ni][nj] = lst[si][sj] + 1
                q.append((ni, nj))

M,N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dir = [(1,0), (0,1), (0,-1), (-1,0)]
q = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            q.append((i,j))

tomato()
day = 0
temp = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            temp=1
        day = max(day, lst[i][j])

if temp == 1:
    print(-1)
elif day == 1:
    print(0)
else:
    print(day-1)



