
import sys

T = int(sys.stdin.readline())
stack = []
for _ in range(1, T+1):
    c = sys.stdin.readline().split()
    if c[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        stack.append(int(c[1]))