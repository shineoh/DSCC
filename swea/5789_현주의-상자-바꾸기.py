# 5789_현주의-상자-바꾸기 풀이
# 2022-02-10

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N = 상자의 개수 Q = 작업 반복 횟수 
    N, Q = map(int, input().split())
    ans = '' # 답 넣을 공간
    box_lst = [0]*N # 박스 리스트
    
    # Q회 동안 반복, 첫 번째 작업 --> i = 1
    for i in range(1, Q+1):
        L_i, R_i = map(int, input().split())

        # Q회 동안 L_i에서 R_i번 째 박스까지 i 넣어줌
        for j in range(L_i, R_i+1):
            box_lst[j-1] = i
    
    # 박스리스트의 값들을 하나씩 ans에 저장
    for ans_num in box_lst:
        ans += '{} '.format(ans_num)

    print('#{} {}'.format(tc, ans))