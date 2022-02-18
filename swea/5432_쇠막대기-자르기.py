# 5432_쇠막대기-자르기 풀이
# 2022-02-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    cnt = 0
    ans = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if lst[i-1] == '(':
                ans += cnt
            else:
                ans += 1

    print('#{} {}' .format(tc, ans))