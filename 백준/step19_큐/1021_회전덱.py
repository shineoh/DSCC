# 백준 1021_회전덱
# 2022-03-08
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst_find = list(map(int, input().split()))
q = deque(i for i in range(1, N+1))
cnt = 0
for j in lst_find:
    while True:
        if q[0] == j:
            q.popleft()
            break
        else:
            if q.index(j) < len(q)/2:
                while q[0] != j:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != j:
                    q.appendleft(q.pop())
                    cnt += 1
print(cnt)