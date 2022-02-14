# 1954_달팽이-숫자 풀이
# 2022-02-14

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 방향 결정 -> 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    path = [[0]*N for _ in range(N)]
    direction = 0 # 방향(dx,dy의 인덱스 값)
    x, y = 0, 0 # 현재 좌표

    # 1부터 N*2까지 순회하며 시행
    for num in range(1, N**2+1):
        path[x][y] = num    # 해당 위치에 숫자 넣기
        x += dx[direction]  # x좌표 값 더해주기
        y += dy[direction]  # y좌표 값 더해주기

        # 인덱스 범위가 유효한지, 예정된 좌표가 0인지 확인
        if 0 <= x+dx[direction] < N and 0 <= y+dy[direction] <N and path[x+dx[direction]][y+dy[direction]]==0: #조건 맞으면 continue
            continue
        else: # 조건이 안맞으면 방향바꾸기
            if direction < 3:
               direction += 1
            else:
               direction = 0

    # 답 출력
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(path[i][j], end=' ')
        print()






