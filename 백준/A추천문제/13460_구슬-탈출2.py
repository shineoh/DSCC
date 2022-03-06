# 13460_구슬-탈출2 풀이
# 2022-03-02

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] # 방문리스트 -> 4차원으로 구현 [빨강][파랑]


# '.' = 빈 칸, '#' = 벽, 'O'= 구멍, 'R'= 빨간 구슬, 'B'= 파란 구슬
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'R':
            ri, rj = i, j
        elif lst[i][j] == 'B':
            bi, bj = i, j
queue = [(ri, rj, bi, bj, 1)]
visited[ri][rj][bi][bj] = 1

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ans = 0
while queue:
    ri, rj, bi, bj, cycle = queue.pop(0)
    if cycle > 10:  # 10번 반복하면 실패
        break
    for di, dj in dir:  # 4방향에 대해
        rcnt = bcnt = 0
        nri, nrj, nbi, nbj = ri, rj, bi, bj
        while lst[nri+di][nrj+dj] != '#' and lst[nri][nrj] != 'O': # 막히거나 구멍이 나올때까지 빨간공 이동
            nri += di
            nrj += dj
            rcnt += 1
        while lst[nbi+di][nbj+dj] != '#' and lst[nbi][nbj] != 'O': # 막히거나 구멍이 나올때까지 파란공 이동
            nbi += di
            nbj += dj
            bcnt += 1

        if lst[nbi][nbj] == 'O': # 파란공이 구멍에 빠지면 실패
            continue
        else:
            if lst[nri][nrj] == 'O': # 빨간공이 구멍에 위치하면 성공 표시하고 break
                ans = 1
                break
            # 벽에 막힌 경우
            if nri == nbi and nrj == nbj: # 겹치면 이동거리가 먼 것을 한 칸 전으로 이동
                if rcnt > bcnt:
                    nri -= di
                    nrj -= dj
                else:
                    nbi -= di
                    nbj -= dj
            # 다른 조건없이 벽에 막혔으면
            if visited[nri][nrj][nbi][nbj] == 0: # 방문 표시하기
                visited[nri][nrj][nbi][nbj] = 1
                queue.append((nri, nrj, nbi, nbj, cycle + 1)) # 큐에 현 좌표 추가하기

    if ans == 1: # 성공해서 for 문 나온거면 while문도 break
        break


if ans == 1: # 성공 시
    print(cycle)

else: # 실패 시
    print(-1)

