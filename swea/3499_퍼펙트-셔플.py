# 3499_퍼펙트-셔플 풀이
# 2022-02-18

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(input().split())
    ans_lst = [] # 셔플 결과를 담을 리스트
    i = 0 # 분리 시 첫 덱의 인덱스(0으로 초기화)

    if N % 2: # 덱이 홀 수일 경우
        j = N // 2 + 1 # 분리 시 두번째 덱의 인덱스 -> N//2+1
        # while 반복문을 통해 셔플(첫 째 덱이 한 장 더 많음)
        while i < N // 2 + 1:  # 첫째 덱의 범위내에서 순서대로
            ans_lst.append(lst[i])  # 첫째 덱 카드 뽑기
            if j == N: # 첫 째덱 다뽑았을 때 break
                break
            ans_lst.append(lst[j]) # 두번째 덱 카드 뽑기
            i += 1
            j += 1
    else: # 덱이 짝 수일 경우
        j = N // 2 # 분리 시 두번째 덱의 인덱스 -> N//2
        while i < N // 2 and j < N: # 각 덱의 범위내에서 순서대로
            ans_lst.append(lst[i]) # 첫째 덱 카드 뽑기
            ans_lst.append(lst[j]) # 두번째 덱 카드 뽑기
            i += 1
            j += 1
    
    # 답 출력
    print('#{}' .format(tc), end=' ')
    print(*ans_lst)

