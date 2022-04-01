# 5188_최소합
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    stack = [(0,0,lst[0][0])] # 스택(초기값 인덱스(i,j), 합)
    dir = [(1,0), (0,1)] # 방향 인덱스
    ans = 1700 # 최소값 담을 변수
    while stack:
        i,j, ssum = stack.pop()
        if i ==N-1 and j==N-1: # 도착했을경우
            if ans> ssum: # 최소값 갱신
                ans = ssum
        for di, dj in dir: # 각 방향 탐색하며
            ni = i+di
            nj = j +dj
            if 0<=ni<N and 0<=nj<N: # 인덱스가 유효할 경우
                ns = ssum + lst[ni][nj] # 합에 값 추가
                stack.append((ni, nj, ns)) # 스택에 push
    # 답출력
    print('#{} {}' .format(tc, ans))