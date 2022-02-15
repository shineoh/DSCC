# 1210 ladder 풀이
# 2022-02-15

import sys

sys.stdin = open('input.txt', 'r')

# 사다리 타기 함수(인자값 : 사다리, 시작점의 열)
def riding(ladder, start):
    x, y = 0, start # 초기 좌표
    dir = 0         # 초기 방향(아래)
    while x<99:     # 사다리를 다 내려올 때까지 반복
        # 방향따라 한칸만큼 좌표이동
        x += dx[dir]
        y += dy[dir]

        if dir != 0: # 방향이 아래쪽이 아니면 시행
            # 아래로 갈 수 있으면 방향 바꾸고
            if ladder[x + dx[0]][y + dy[0]] == 1:
                dir =0
            else: # 아닐 경우 계속 진행
                continue
        # 아래로 가고 있을 경우 수평방향으로 갈 수 있을지 탐색 후 갈 수 있으면 방향 전환
        elif 0<= x+dx[1]<100 and 0<= y+dy[1]<100 and ladder[x + dx[1]][y + dy[1]] == 1:
            dir = 1
        elif 0<= x+dx[2]<100 and 0<= y+dy[2]<100 and ladder[x + dx[2]][y + dy[2]] == 1:
            dir = 2

        # 종점(사다리 탄 결과) 좌표 반환
        end = ladder[x][y]
    return end

T = 10
# 방향 설정 위한 리스트(하 우 좌)
dy = [0, 1, -1]
dx = [1, 0, 0]

for _ in range(1, T + 1):
    tc = int(input())
    ans = 0 # 답 담을 변수

    # 100*100 사다리 받기
    lst = [list(map(int, input().split())) for _ in range(100)]

    # 열의 수(100)만큼 순회하며 시행
    for i in range(100):
        if lst[0][i] == 1: # 첫번째 행 중에 1을 가지는 열을 시작점으로 하여 사다리 타기
            riding(lst, i)
            if riding(lst, i) == 2: # 종점이 2일 경우 답에 해당 시작점 담기
                ans = i

    # 답 출력
    print('#{} {}' .format(tc, ans))