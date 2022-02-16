# 1221_GNS 활용 풀이
# 2022-02-16

import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

# 숫자리스트
num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for _ in range(1, T+1):
    # 각 수를 카운트하기 위한 카운트리스트
    cnt_lst = [0] * 10
    # tc = 테스트 케이스, N = 테스트케이스의 길이
    tc, N = input().split()
    # 제시되는 테스트케이스 받기
    lst_alien = list(input().split())
    # 제시된 리스트를 순회하며 카운팅
    for num_alien in lst_alien:
        # 숫자리스트를 통해 해당하는 index값 화인
        for i in range(10):
            # 해당하는 index의 카운트리스트에 +1 카운트
            if num_lst[i] == num_alien:
                cnt_lst[i] += 1

    # 답 출력
    print(tc)
    for j in range(10):
        for k in range(cnt_lst[j]):
            print(num_lst[j], end=' ')
    print()


