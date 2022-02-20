# 1860_진기의-최고급-붕어빵 풀이
# 2022-02-18

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    # 리스트 정렬_ lst.sort()
    for j in range(len(lst)):
        k = len(lst) - j
        for l in range(1, k):
            if lst[l-1] >= lst[l]:
                lst[l-1], lst[l] = lst[l], lst[l-1]

    ans = 'Possible' # 답 -> Possible로 초기화
    cnt = (lst[0]//M)*K # 붕어빵 개수 -> 첫 손님이 왔을 때(lst[0]) 로 초기화

    if cnt > 0: # 첫 손님이 올때 붕어빵이 있으면

        # for문을 통해 붕어빵 제공 가능 여부 탐색
        for i in range(1, N):
            cnt = ((lst[i]//M)*K) - i  # i번째 손님이 왔을 때의 붕어빵 수
            if cnt < 1: # 붕어빵이 없으면
                ans = 'Impossible' # 답에 Impossible 넣고 break
                break
    else: # 첫 손님이 왔을 때 붕어빵이 없으면
        ans = 'Impossible' # 붕어빵 제공 불가 (Impossible)

    # 답  출력
    print('#{} {}' .format(tc, ans))