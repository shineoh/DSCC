# 2001 파리퇴치 풀이
# 2022-02-15

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N*N 배열 받기
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0 # 최댓값 담을 변수
    # 배열을 순회하며 구간합 구하기
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_part = 0 # 구간합 담을 변수
            # 구간합 구하기
            for k in range(M):
                for l in range(M):
                    sum_part += lst[i+k][j+l]
            # 구간합이 최댓값보다 크면 최댓값 갱신
            if max_sum < sum_part:
                max_sum = sum_part

    # 답 출력
    print('#{} {}' .format(tc, max_sum))