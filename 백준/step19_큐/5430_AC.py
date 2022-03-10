# boj 5430_AC
# 2022-03-10
from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    p = list(input())
    n = int(input())
    q = deque(input().rstrip()[1:-1].split(","))
    e = 0
    cnt_r = 0
    if n == 0:
        q = deque()

    for c in p:
        if c=='R':
            cnt_r += 1
        elif c=='D':
            if q:
                if cnt_r % 2:
                    q.pop()
                else:
                    q.popleft()
            else:
                e =1
                break
    if e == 1:
        print('error')
    else:
        if cnt_r % 2:
            q.reverse()
        print("[" + ",".join(q) + "]")

        #print(list(map(int, q)))

