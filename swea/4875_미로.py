# 4875_미로 풀이
# 2022-02-24

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)] # 2차원 배열로 받기
    # 시작점 찾기
    for k in range(N):
        for l in range(N):
            if lst[k][l] == 2: # 시작점 찾으면 시작 좌표에 넣어주기
                start_i = k
                start_j = l

    # 방향 (우,하,좌,상)
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(start_i, start_j)] # 스택(시작좌표 넣어서 생성)
    ans = 0 # 답 -> 0으로 초기화

    while stack:
        i, j = stack.pop()  # 좌표를 꺼내고
        lst[i][j] = 1 # 해당 좌표를 지나왔음을 표시(1)
        for di, dj in dir: # 각 방향을 돌며 갈 수 있는 방향이 있는지 탐색
            ni = i + di # 해당 방향을 이동했을 때의 좌표(ni, nj)
            nj = j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: # 유효하지 않은 인덱스일 경우 continue
                continue
            elif lst[ni][nj] == 0: # 갈 수 있으면
                stack.append((ni, nj)) # 좌표를 스택에 push
            elif lst[ni][nj] == 3: # 목적지를 찾으면
                ans = 1 # 답에 1 주고 break
                break

    # 답출력
    print('#{} {}'.format(tc, ans))
