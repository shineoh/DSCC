# 3143_가장-빠른-문자열-타이핑 풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    cnt = len(A) # 타이핑 횟수 -> A의 글자수만큼 초기화

    i = 0 # 반복문을 위한 인덱스
    # A의 문자를 순회하며
    while i <= len(A)-len(B)+1:
        if A[i] == B[0]:  # B의 첫 문자와 비교
            if A[i:i+len(B)] == B: # B의 길이만큼 B와 비교
                cnt -= (len(B)-1) # cnt에서 (B의 길이-1)만큼 빼기
                i += (len(B)-2)
        i += 1

    #답 출력
    print('#{} {}'.format(tc, cnt))
