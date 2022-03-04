# 백준 18258 큐2
# 2022-03-04
import sys

N = int(input())
queue = []
for _ in range(N):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        queue.append(c[1])
    elif c[0] == 'pop':
        if queue:
            print(queue.pop[0])
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


