# 4248_min-max 풀이
# 2022-02-10

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 양수의 개수
    max = 0
    min = 10000000 # 양수의 개수<= 1000, 양수의 범위 <=1000000 이므로 min=10000000으로 초기화
    ans = 0 # 답 넣을 변수

    lst = list(map(int, input().split())) # 제시되는 양수리스트

    # 양수리스트를 순회하며 최댓값, 최솟값 구하기
    for i in range(N):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]

    # ans에 max와 min의 차이 할당
    ans = max-min
    # 답 출력
    print('#{} {}'.format(tc, ans))