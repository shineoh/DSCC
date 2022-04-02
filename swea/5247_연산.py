# 5247_연산
# 2022-04-01

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def BFS():
    global ans
    while q: #큐가 비어있지 않으면
        num, cnt = q.popleft()
        if num == M: # M을 만들었으면
            ans = cnt # ans에 cnt담아서 반환
            return
        for i in range(4): # 네가지 연산에 대해
            if i == 0:
                if 1 <= num + 1 <= 1000000 and visited[num+1] == 0: # 인덱스가 유효하고 연산결과가 방문하지 않은 수라면
                    q.append((num+1, cnt+1)) # 큐에 push하고
                    visited[num+1] = 1 # 방문 표시
            # 나머지 연산에 대해서도 반복
            elif i == 1:
                if 1 <= num - 1 <= 1000000 and visited[num-1] == 0:
                    q.append((num-1, cnt+1))
                    visited[num - 1] = 1
            elif i == 2:
                if 1 <= num * 2 <= 1000000 and visited[num*2] == 0:
                    q.append((num*2, cnt+1))
                    visited[num * 2] = 1
            elif i == 3:
                if 1 <= num - 10 <= 1000000 and visited[num-10] == 0:
                    q.append((num-10, cnt+1))
                    visited[num - 10] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = 0
    visited = [0] * 1000001 # 연산결과를 인덱스로하는 방문리스트
    q = deque() # 큐사용
    q.append((N,0))
    BFS()

    # 답출력
    print("#{} {}".format(tc, ans))