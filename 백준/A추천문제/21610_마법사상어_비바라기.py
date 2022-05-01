from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dir = [(0,0), (0,-1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1,1), (1, 0), (1, -1)]
clouds = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for _ in range(M):
    d,s = map(int, input().split())
    new_clouds = deque()
    while clouds:
        si,sj = clouds.popleft()
        temp_s = s
        # 구름을 d 방향으로 s칸 이동
        while temp_s:
            temp_s -= 1
            si = si + dir[d][0]
            sj = sj + dir[d][1]
            if si < 0:
                si = N-1
            elif si >= N:
                si = 0
            if sj < 0:
                sj = N-1
            elif sj >= N:
                sj = 0
        new_clouds.append((si,sj))
    # 비 내리기 -> 구름이 있는 칸 바구니에 저장된 물의 양 1 증가
    no_clouds = set()
    # 구름 없애기
    while new_clouds:
        si,sj = new_clouds.popleft()
        no_clouds.add((si,sj)) # 구름 없어진 칸 저장
        lst[si][sj] += 1

    for i,j in no_clouds:
        cnt = 0
        for dd in range(2, 9, 2): # 대각선 물 증가시키기
            ii = i + dir[dd][0]
            jj = j + dir[dd][1]
            if 0 <= ii < N and 0 <= jj < N and lst[ii][jj] > 0:
                cnt += 1
        lst[i][j] += cnt
    # 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 감소
    for i in range(N):
        for j in range(N):
            if lst[i][j] >= 2 and (i, j) not in no_clouds: # 구름 사라진 칸인지 확인
                clouds.append((i, j))
                lst[i][j] -= 2

ans = 0
for i in range(N):
    for j in range(N):
        ans += lst[i][j]
print(ans)