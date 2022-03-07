# 백준 1966_프린터큐
# 2022-03-08
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # q = deque(map(int, input().split()))
    q = list(map(int, input().split()))
    ans = M + 1
    check = 0
    cnt = 0
    while q:
        #s = q.popleft()
        s = q.pop(0)
        cnt += 1
        check += 1
        for q_num in q:
            if q_num > s:
                q.append(s)
                cnt -= 1
                if check == ans:
                    ans += len(q)
                break
        if check == ans:
            print(cnt)
            break
