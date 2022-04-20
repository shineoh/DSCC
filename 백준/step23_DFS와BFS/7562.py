# 나이트 이동
# 2022-04-20
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    ans=0
    fi, fj = map(int, input().split())
    li, lj = map(int, input().split())
    dir = [(2,1),(2, -1), (1, 2), (-1, 2), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    q = deque()
    q.append((fi,fj,0))
    lst[fi][fj] = 1
    while q:
        si, sj, cnt = q.popleft()
        if si == li and sj == lj :
            ans = cnt
            break
        for di, dj in dir:
            ni = si + di
            nj = sj + dj
            if 0<= ni < N and 0 <= nj < N and lst[ni][nj]==0:
                q.append((ni, nj, cnt + 1))
                lst[ni][nj] = 1

    print(ans)