# 1220_Magnetic 풀이
# 2022-02-18

import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 답 0으로 초기화

    # 이중for문을 통해 탐색
    # 조건 1 : 1(N자성체)이 위에 위치 --> 상단이 N극이므로 교착상태가 되기 위해서는 1-2순으로 연속되어야 함
    # 조건 2 : 1 이후에 2(S자성체)가 이어질 경우 교착
    for j in range(N):
        check = 0 # 교착 조건을 충족하는지 확인위한 변수(0으로 초기화)
        for i in range(N):
            if lst[i][j] == 1: # 1일 경우
                check = 1 # 교착조건 1 충족
            elif lst[i][j] == 2: # 2일 경우
                if check == 1: # 교착조건 1을 충족했다면
                    ans += 1 # 답에 +1 카운트
                    check = 0 # 아닐 경우 조건확인 변수 0으로 돌리기

    # 답 출력
    print('#{} {}' .format(tc, ans))