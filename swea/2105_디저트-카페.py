# 1952_수영장 풀이
# 2022-03-22

import sys
sys.stdin = open('input.txt', 'r')

def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n==2 and ans>=cnt*2:
        return
    if n>3:
        return
    if n ==3 and ci=si and cj=sj and ans<cnt:
        ans=cnt
        return

    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0<=ni<N and 0<=nj<N and lst[ni][nj] not in v:
            v.append(lst[ni][nj])
            DFS(k, ni, nj, v, cnt+1)
            v.pop()

di, dj = (1,1,-1,-1,1),(-1,1,1,-1,-1)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    ans = -1
    for si in range(N):
        for sj in range(N):
            DFS( 0, i, j, [], 0)
    print('#{} {}' .format(tc, ans))