# 4865_글자수 풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    # 중복 제거를 위해 set으로 받은 후 list로 변환
    str1 = list(set(input()))
    # 카운팅을 위한 카운트리스트(0으로 초기화)
    cnt_lst = [0]*len(str1)
    str2 = input()
    ans = 0 # 답 담을 변수

    # str2에 str1의 글자들이 몇개씩 있는지 카운팅
    for s in str2:
        for i in range(len(str1)): # str1의 문자를 순회하며
            if s == str1[i]: # str2의 글자와 비교 후 일치하면
                cnt_lst[i] += 1 # 카운트리스트에서 대응하는 인덱스의 값에 +1 카운트

    # 카운트리스트를 순회하며 최댓값 도출
    for n in cnt_lst:
        if ans < n:
            ans = n

    # 답 출력
    print('#{} {}'.format(tc, ans))
