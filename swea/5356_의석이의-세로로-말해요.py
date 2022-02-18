# 5356_의석이의-세로로-말해요 풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):


    max_len =0
    lst = []
    for i_lst in range(5):
        lst.append(list(input()))

        if max_len < len(lst[i_lst]):
            max_len = len(lst[i_lst])

    ans = ''
    for j in range(max_len):
        for i in range(5):
            if len(lst[i]) <= j:
                continue
            else:
                ans += lst[i][j]


    print('#{} {}'.format(tc, ans))
