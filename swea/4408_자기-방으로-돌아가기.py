# 4408_자기-방으로-돌아가기 풀이
# 2022-02-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst_corridor = [0]*201 # 복도리스트
    for i in range(N):
        if lst[i][0] < lst[i][1]: #
            s = (lst[i][0] + 1) // 2
            e = (lst[i][1] + 1) // 2

        else:
            s = (lst[i][1] + 1) // 2
            e = (lst[i][0] + 1) // 2

        for j in range(s, e+1):
            lst_corridor[j] += 1

    ans = 0
    for cnt in lst_corridor:
        if ans < cnt:
            ans = cnt

    print('#{} {}' .format(tc, ans))

    # for j in range(lst[i][0], lst[i][1]+1, 2):
    #     lst_corridor[((j+1)//2)-1] += 1