
# 경로의 난이도는 총 이동 거리가 중요한 것이 아니라 경로 중 한 번에 이동해야 하는 수직 거리의 최대 값에 의해 난이도가 결정
# 암벽의 난이도는 여러 이동 경로 중 가장 난이도가 낮은 경로에 의해 결정

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dir = [(1,0), (0,1), (-1,0), (0, -1)]
for tc in range(1, T+1):
    #  암벽의 높이 N과 너비 M
    N, M = map(int, input().split())
    # 1일 경우 발을 디딜 곳이 있는 곳이고 0일 경우 발을 디딜 곳이 없는 곳
    lst = [list(map(int, input().split())) for _ in range(N)]
    #출발 지점은 2로 주어지며 항상 높이 1의 가장 왼쪽 지점이다.
    # 목표 지점은 3으로 주어진다.

    # 출발, 도착지점 찾기
    # for i in range(N):
    #     for j in range(M):
    #         if lst[i][j] == 2:
    #             si,sj = i,j
    #         if lst[i][j] == 3:
    #             ei, ej = i,j
    k=1
    while k<N:
        visited = [[0]*M for _ in range(N)]
        visited[N-1][0] = 1
        stack = [(N - 1, 0)]
        temp = 0
        while stack:
            si, sj = stack.pop(0)
            for di, dj in dir:
                if di == 1 or di ==-1:
                    for kk in range(1, k+1):
                        ni = si+(di*kk)
                        nj = sj+(dj*kk)
                        if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 3:
                            ans = k
                            temp = 1
                            break
                        elif 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and lst[ni][nj] == 1:
                            stack.append((ni, nj))
                            visited[ni][nj] = 1
                else:
                    ni = si + di
                    nj = sj + dj
                    if 0<=ni<N and 0<=nj<M and lst[ni][nj] == 3:
                        ans = k
                        temp = 1
                        break
                    elif 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and lst[ni][nj] == 1:
                        stack.append((ni,nj))
                        visited[ni][nj] = 1
            if temp == 1:
                break
        if temp == 1:
            break
        k+=1
    ans = k

    print('#{} {}' .format(tc, ans))


