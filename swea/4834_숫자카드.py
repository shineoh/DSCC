# 4834_숫자-카드 풀이
# 2022-02-10

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N = 카드 장수
    # max_num = 가장 많은 카드에 적힌 숫자
    # cnt_max_num = 가장 많은 카드의 개수
    N = int(input())
    max_num = 0
    cnt_max_num = 0

    # 입력받은 수를 리스트에 하나씩 담기
    num_lst = []
    num_lst.extend(input())
    num_lst = list(map(int, num_lst))

    # 카드 수 카운트를 위한 리스트
    cnt_lst = [0] * 10

    # 카드리스트를 순회하며 해당 수에 대응되는 카운트리스트에 +1카운트
    for num in num_lst:
        cnt_lst[num] += 1

    # 카운트리스트를 순회하며 가장 많이 있는 카드에 적힌 숫자와 카드 수 구하기
    for i in range(10):
        if cnt_lst[i] >= cnt_max_num:
            cnt_max_num = cnt_lst[i] # 가장 많이 있는 카드의 수
            max_num = i # 가장 많이 있는 카드에 적힌 숫자

    # 답 출력
    print('#{} {} {}'.format(tc, max_num, cnt_max_num))
