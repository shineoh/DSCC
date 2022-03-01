# boj 4949_균형잡힌 세상 풀이



while True:
    stack = []
    sentence = input()
    if sentence == '.':
        break
    opener = ['[', '(']
    closer = [']', ')']
    ans = 'yes'
    for s in sentence:
        if s in opener:
            stack.append(s)
        if s in closer:
            if not stack:
                ans = 'no'
                break
            x = stack.pop()
            if s == ']' and x != '[':
                ans = 'no'
                break
            if s == ')' and x != '(':
                ans = 'no'
                break
    if stack:
        ans = 'no'
    print(ans)
