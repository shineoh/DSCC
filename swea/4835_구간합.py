# 4835_구간합 풀이
# 2022-02-10

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N=배열의 길이, M=구간의 길이
    # --> 배열 내 구간의 합을 구해서 최댓값과 최솟값의 차이 구하기
    N, M = map(int, input().split())

    # 제시되는 정수의 배열 만들기
    num_lst = list(map(int, input().split()))

    min_t = 1000000 #N<= 100, 정수<=10000 이므로 1000000으로 최솟값 초기화
    max_t = 0
    ans = 0 # 답 넣을 변수

    # M-1에서부터 시작, 현재위치 j에서 앞으로 구간을 펼치면서 반복문 시행
    for i in range(M-1, N):
        sum_t = 0 # 임시로 구간합을 담을 변수

        # 구간합 구하기
        for j in range(M):
            sum_t += num_lst[i-j]

        # 도출한 구간합을 최댓값과 최솟값과 비교하여 max, min 갱신
        if sum_t < min_t:
            min_t = sum_t
        if sum_t > max_t:
            max_t = sum_t

    # 도출한 최댓값과 최솟값의 차이를 ans에 할당
    ans = max_t-min_t
    # 답 출력
    print('#{} {}'.format(tc, ans))