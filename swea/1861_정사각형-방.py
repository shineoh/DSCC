# 1861_정사각형-방 풀이
# 2022-03-17

import sys

sys.stdin = open('input.txt', 'r')

def move(i, j):
    cnt = 0
    stack = [(i, j, cnt)]
    max_cnt = 0
    while stack:
        ti, tj, cnt = stack.pop()
        if max_cnt < cnt:
            max_cnt = cnt
        for di, dj in dir:
            ni = ti+di
            nj = tj+dj
            if 0<= ni <N and 0<=nj<N and lst[ni][nj] == lst[ti][tj]+1:
                stack.append((ni,nj, cnt+1))
    return i, j, max_cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    ans = 0
    for i in range(N):
        for j in range(N):
            temp_i, temp_j, temp_ans = move(i,j)

            if ans < temp_ans:
                ans = temp_ans
                room_num = lst[i][j]
            elif ans == temp_ans:
                if room_num > lst[temp_i][temp_j]:
                    room_num = lst[temp_i][temp_j]

    print('#{} {} {}' .format(tc, room_num, ans+1))


