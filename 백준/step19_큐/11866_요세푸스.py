# 백준 11866_요세푸스
# 2022-03-07
from collections import deque

N, K = map(int, input().split())
queue =deque(i for i in range(1, N+1))
i = 0
cnt = 0
ans = []
while queue:
    a = queue.popleft()
    cnt += 1
    if cnt == K:
        ans.append(a)
        cnt = 0
    else:
        queue.append(a)

print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end=', ')
print('{}>' .format(ans[-1]))
