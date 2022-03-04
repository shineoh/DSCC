# 백준 2164 카드2
# 2022-03-05
from collections import deque

N = int(input())
deque = deque(list(range(1, N+1)))

while len(deque) >1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])