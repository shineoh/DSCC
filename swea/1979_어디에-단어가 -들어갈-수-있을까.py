# 1979 어디에 단어가 들어갈 수 있을까 풀이
# 2022-02-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N = 퍼즐 한변의 길이 K = 단어길이
    N,K = map(int, input().split())
    # N*N 퍼즐 입력받기
    lst = [list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+1)]

    # 답 담을 변수
    ans = 0
    for i in range(N+1):
        # 가로방향 칸과 세로방향 칸을 따로 계산
        cnt_x = 0
        cnt_y = 0

        # 각 행, 열을 순회하며
        for j in range(N+1):
            # 가로방향 칸 탐색
            if lst[i][j] == 1: # 1을 만나면 +1카운트
                cnt_x += 1
            else:              # 0을 만나면 cnt를 k와 비교
                if cnt_x == K: # cnt가 k와 같으면 ans에 +1 카운트
                    ans += 1
                cnt_x = 0      # 비교 후 후 0으로 초기화

            # 세로방향 칸 탐색
            if lst[j][i] == 1:  # 1을 만나면 +1카운트
                cnt_y += 1
            else:               # 0을 만나면 cnt를 k와 비교 후 0으로 초기화
                if cnt_y == K:  # cnt가 k와 같으면 ans에 +1 카운트
                    ans += 1
                cnt_y = 0       # 비교 후 후 0으로 초기화

    # 답 출력
    print('#{} {}' .format(tc, ans))

