# 6458_삼성시의-버스-노선
# 2022-02-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst_BusStop = [0]*5001
    N = int(input())
    A_lst = [0]*N
    B_lst = [0]*N
    for i_input in range(N):
        A_lst[i_input], B_lst[i_input] = map(int, input().split())

        for i in range(A_lst[i_input] , B_lst[i_input]+1):
            lst_BusStop[i] += 1

    P = int(input())
    P_lst = [0]*P
    ans_lst = [0]*P
    for j in range(P):
        P_lst[j] = int(input())
        ans_lst[j] = lst_BusStop[P_lst[j]]

    print('#{} ' .format(tc), end='')
    print(*ans_lst)

