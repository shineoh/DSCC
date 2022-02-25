# boj 9012_괄호 풀이
# 2022-02-25


T = int(input())
for _ in range(1, T+1):
    stack = []
    parenthesis = input()
    ans = 'YES'
    for p in parenthesis:
        if p =='(':
            stack.append(p)
        else:
            if not stack:
                ans = 'NO'
                break
            else:
                stack.pop()

    if stack:
        ans = 'NO'

    print(ans)
