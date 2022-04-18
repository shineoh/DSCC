# 미로탐색
# 2022-04-16

N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

dir = [(1,0), (0,1), (-1, 0), (0,-1)]

q = [(0,0,1)]
lst[0][0] = 0
ans_lst = []
while q:
    si, sj, cnt = q.pop(0)
    if si == N-1 and sj == M-1 :
        ans_lst.append(cnt)
        lst[si][sj] = 1
        continue
    for di, dj in dir:
        ni = si + di
        nj = sj + dj
        if 0<= ni < N and 0 <= nj < M and lst[ni][nj]==1:
            lst[ni][nj] = 0
            q.append((ni, nj, cnt+1))

ans = min(ans_lst)
print(ans)