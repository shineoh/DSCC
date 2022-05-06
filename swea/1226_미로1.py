# 1226_미로1 풀이
# 2022-03-16

import sys

sys.stdin = open('input.txt', 'r')

def move(i, j):
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 방향리스트
    stack = [(i,j)]
    # 스택을 이용한 while 반복문
    while stack:
        ci, cj = stack.pop()
        for di, dj in dir: # 각 방향을 순회하며
            ni = ci + di
            nj = cj + dj
            if lst[ni][nj] == '0': # 이동 가능하면
                stack.append((ni, nj)) # 스택에 push하고
                lst[ni][nj] = '1' # 방문 표시
            elif lst[ni][nj] == '3': # 목적지에 도착하면 1 반환
                return 1

    return 0 # 목적지에 도착하지못하고 반목문 종료하면 0 반환


for _ in range(10):
    tc = int(input())
    N = 16
    lst = [list(input()) for _ in range(N)]
    ans = move(1,1) # 미로탐색 후 결과값 답에 담기
    # 답 출력
    print('#{} {}' .format(tc, ans))


