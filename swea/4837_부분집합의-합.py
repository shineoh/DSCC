# 4837_부분집합의 합 풀이
# 2022-02-14

import sys
sys.stdin = open('input.txt', 'r')

# 1~12를 가지는 집합
A = [num for num in range(1, 13)]


T = int(input())
for tc in range(1, T+1):
    # N = 부분집합의 원소 수, K = 부분집합의 합
    N, K = map(int, input().split())
    ans = 0 # 답(조건을 만족하는 부분집합의 수)을 담을 변수
    for i in range(1<<12):  #부분집합의 개수만큼 순회
        lst = []  # 부분집합을 담을 리스트
        sum_n = 0 # 부분집합의 합을 더할 변수
        cnt = 0   # 부분집합의 원소 수를 카운트할 변수

        for j in range(12):      # 원소의 수만큼 비트 비교
            if i & (1<<j):       # i의 j번 비트가 1인 경우
                lst.append(A[j])  # j번 원소를 부분집합 리스트에 추가
                sum_n += A[j]    # j번 원소를 합에 더하기
                cnt += 1         # 부분집합의 수에 +1 카운트

        # 부분집합의 원소 수와 부분집합의 합이 제시된 N,K와 같으면
        if cnt == N and sum_n == K:
            ans += 1  # 답에 +1 카운트

    print('#{} {}'.format(tc, ans))