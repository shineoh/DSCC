T = int(input())
stack = []
for _ in range(1, T+1):
    c = input()
    if c == 'top':
        print(stack[-1])
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif c == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        a, b = c.split()
        stack.append(int(b))