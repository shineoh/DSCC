# 숨바꼭질
# 2022-04-16
from collections import deque

N, K = map(int, input().split())
M = 100000
visited = [0] * (M+1)

q = deque()
q.append(N)
ans=0
while q:
    x = q.popleft()
    if x == K:
        ans = visited[x]
        break
    for i in (x+1, x-1, x*2):
        if 0<= i <= M and not visited[i]:
            visited[i] = visited[x] + 1
            q.append(i)
print(ans)